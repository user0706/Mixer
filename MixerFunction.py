# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import random
import csv
import re
import operator

def setColortoRow(table, rowIndex, color):
    '''
    :Paints the background of the desired row (rowIndex) of the table in the desired color.
    '''
    for j in range(table.columnCount()):
        table.item(rowIndex, j).setBackground(color)

class Dictlist(dict):
    '''
    :Creates a dictionary whose value is a list. For each same key with the same or different value, 
    :   its value is added as a new element to the list of that dictionary whose key is the same key.

    Example: 
    1.  Let the input key be good, and its value Positive
    2.  The output dictionary will be {"good": ["Positive"]}
    3.  Let the same (good) input key appear again, whose value is the same again (Positive)
    4.  The output dictionary will be {"good": ["Positive", "Positive"]}
    5.  Let the same (good) input key reappear again, but this time the value is different (Negative)
    6.  The output dictionary will be {"good": ["Positive", "Positive", "Negative"]}
    '''
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

def exists(obj, chain):
    _key = chain.pop(0)
    if _key in obj:
        return exists(obj[_key], chain) if chain else obj[_key]

def Punctuation(inSentence):
    '''
    :Removes all punctuation marks except apostrophes (') from the string
    '''
    inSentence = inSentence.replace('?', '')
    return re.sub(r"[^\w\d'\s]+", '', inSentence)

def LowerCase(inSentence):
    '''
    :Converts all characters of a string to a lowercase
    '''
    return inSentence.lower()

def StopWords(inSentence, S_Word_List):
    '''
    :Removes stop words from the string
    '''
    if S_Word_List:
        temp = [Sent_Word for Sent_Word in inSentence.split(' ') for S_Word in S_Word_List if Sent_Word == S_Word]
        return " ".join(temp)
    else:
        pass

def OpenDocument(File_Path):
    '''
    :Used to load the database.
    :Returns a 2D database. Example: [[...], [...], ...]
    :The elements of the internal list are the sentence at the zero position and the label at the first.
    '''
    csvread = pd.read_csv((File_Path).strip(), encoding='utf8')
    csvread = csvread.values.tolist()

    to_dict = dict(csvread)
    temp_list = []
    for k, v in to_dict.items():
        temp_list.append([k,v])
    return temp_list

def Preprocess(In_Data, L_Case=False, Pun=False, S_Word=False):
    '''
    :Applies functions to convert characters to lowercase as well as to punctuation.
    '''
    temp = {}
    for item in In_Data:
        if L_Case:
            item[0] = LowerCase(str(item[0]))
        if Pun:
            item[0] = Punctuation(str(item[0]))

    return In_Data

def Assigning(inputData):
    dictlist = Dictlist()
    '''
    :It goes through each line and applies the logic explained for the Dictlist function
    '''
    for item in inputData:
        item[0] = item[0].split(" ")
        for word in item[0]:
            dictlist[word] = item[1]
    print(dictlist)
    return dictlist

def LabelValuating(In_Data):
    '''
    :Calculates values for each different label for each word
    :It counts how many times each of the unique labels for the current word is repeated
    :Label value is obtained when the number of times a label is repeated is divided by 
     the total number of all labels for that (current) word.

    Example for "today is a great day":
    ===================================
    {'today':   {'neg': 0.5, 'pos': 0.5}, 
     'is':      {'neg': 0.333, 'neut': 0.333, 'pos': 0.333}, 
     'a':       {'neg': 0.666, 'pos': 0.333}, 
     'great':   {'neut': 1.0}, 
     'day':     {'neut': 1.0}
    }
    '''
    outdict = {}
    for word, labelsList in In_Data.items():
        uniqueLabel, counts = np.unique(labelsList, return_counts = True)
        temp_list = []
        for number in counts:
            temp_list.append(number/(len(labelsList)))
            outdict[word] = dict(zip(uniqueLabel, temp_list))
    return outdict

def LiveTrainModel(Data):
    '''
    :Model training
    :A trained model is nowhere saved as a backup
    '''
    Data = Assigning(Data)
    Data = LabelValuating(Data)
    return Data

def GetUniqueLabels(Data):
    '''
    :Search for all possible (unique / different) labels at the level of the entire database
    '''
    All_Labels = []
    for word, l_values in Data.items():
        for label in l_values.keys():
            All_Labels.append(label)
    All_Labels = list(set(All_Labels))
    return All_Labels

def CollectingLabelsValue(Data, Sample):
    '''
    :Checks if the word from the test sentence exists in the trained model
    :Depending on that, the current word from the test sentence will be 
     assigned a value as from the trained model for that word if it exists 
     Otherwise the value will be 0
    '''
    Sample = Punctuation(Sample)
    Sample = LowerCase(Sample)

    if Data:
        All_Labels = GetUniqueLabels(Data)

        dictlist = Dictlist()
        for S_Word in Sample.split(' '):
            for D_Word in Data.keys():
                if S_Word == D_Word:
                    for label in All_Labels:
                        if label in exists(Data, [S_Word]).keys():
                            dictlist[label] = exists(Data, [S_Word, label])
                        else:
                            dictlist[label] = 0
    return dictlist

def Test(Data, Sample):
    '''
    :Calculates the value for each of the unique labels at the test sentence level
    '''
    dictlist = CollectingLabelsValue(Data, Sample)

    outdict = {}
    for Word, Walue_List in dictlist.items():
        outdict[Word] = sum(Walue_List)/len(Walue_List)
    return outdict

def TestSamples(Data, TestNumber = 10):
    '''
    :Calculates how many sentences will be tested for accuracy
    '''
    temp = [row[0] for row in Data]
    return random.sample(temp,TestNumber)

def Accuracy(OriginalData, LabelData, SampleData, TestNumber = 10):
    '''
    :It tests a certain number of database sentences and checks whether the predicted 
     answer matches the previously defined one.
    :Based on that, a calculation is performed, based on which it is seen how accurate
     the algorithm with added filters is
    '''
    counter = 0
    for sentence in SampleData:
        temp1 = Test(LabelData, sentence)
        maxlabel = max(temp1.items(), key=operator.itemgetter(1))[0]
        maxlabel = [k for k,v in temp1.items() if v == temp1[maxlabel]]
        for row in OriginalData:
            for label in maxlabel:
                if sentence == row[0] and label == row[1]:
                    counter += 1
    acc = (counter/TestNumber)*100
    return acc
