# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import random
import csv
import re
import operator

def setColortoRow(table, rowIndex, color):
    for j in range(table.columnCount()):
        table.item(rowIndex, j).setBackground(color)

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

def exists(obj, chain):
    # Accessing Multidimensional Dictationary Elements
    _key = chain.pop(0)
    if _key in obj:
        return exists(obj[_key], chain) if chain else obj[_key]

def Punctuation(inSentence):
    inSentence = inSentence.replace('?', '')
    return re.sub(r"[^\w\d'\s]+", '', inSentence)

def LowerCase(inSentence):
    return inSentence.lower()

def StopWords(inSentence, S_Word_List):
    if S_Word_List:
        temp = [Sent_Word for Sent_Word in inSentence.split(' ') for S_Word in S_Word_List if Sent_Word == S_Word]
        return " ".join(temp)
    else:
        pass

def OpenDocument(File_Path):
    csvread = pd.read_csv((File_Path).strip(), encoding='utf8')
    csvread = csvread.values.tolist()

    to_dict = dict(csvread)
    temp_list = []
    for k, v in to_dict.items():
        temp_list.append([k,v])
    return temp_list

def Preprocess(In_Data, L_Case=False, Pun=False, S_Word=False):
    temp = {}
    for item in In_Data:
        if L_Case:
            item[0] = LowerCase(str(item[0]))
        if Pun:
            item[0] = Punctuation(str(item[0]))

    return In_Data

def Assigning(inputData):
    dictlist = Dictlist()
    #Prolazi kroz svaku u bazi
    for item in inputData:
        item[0] = item[0].split(" ")
        for word in item[0]:
            dictlist[word] = item[1]
    return dictlist

def LabelValuating(In_Data):
    outdict = {}
    for word, labelsList in In_Data.items():
        #Prebrojava se koliko koliko se puta ponavlja svaka od
        # unikatnih labela za trenutnu rec
        uniqueLabel, counts = np.unique(labelsList, return_counts = True)
        temp_list = []
        for number in counts:
            # Trenutni broj, koliko se puta ponavlja svaka 
            # unikatna labela podeljen sa ukupnim brojem
            # labela za trenutnu rec se dodaje u privremenu listu
            temp_list.append(number/(len(labelsList)))
            '''
            {'dobar': {'neg': 0.5, 'pos': 0.5}, 
            'je': {'neg': 0.333, 'neut': 0.333, 'pos': 0.333}, 
            'dan': {'neg': 0.666, 'pos': 0.333}, 
            'sve': {'neut': 1.0}, 
            'uobicajeno': {'neut': 1.0},
            'los': {'neg': 1.0}, 
            'nije': {'neg': 1.0}}
            '''
            outdict[word] = dict(zip(uniqueLabel, temp_list))
    return outdict

def LiveTrainModel(Data):
    Data = Assigning(Data)
    Data = LabelValuating(Data)
    return Data

def GetUniqueLabels(Data):
    All_Labels = []
    for word, l_values in Data.items():
        for label in l_values.keys():
            All_Labels.append(label)
    All_Labels = list(set(All_Labels))
    return All_Labels

def CollectingLabelsValue(Data, Sample):
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
    dictlist = CollectingLabelsValue(Data, Sample)

    outdict = {}
    for Word, Walue_List in dictlist.items():
        outdict[Word] = sum(Walue_List)/len(Walue_List)
    return outdict

def TestSamples(Data, TestNumber = 10):
    temp = [row[0] for row in Data]
    return random.sample(temp,TestNumber)

def Accuracy(OriginalData, LabelData, SampleData, TestNumber = 10):
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

#if __name__ == '__main__':
#    main()

#print(OpenDocument('F:/Diplomski/TestData.csv'))