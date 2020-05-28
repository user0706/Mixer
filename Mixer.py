from design import *
from MixerFunction import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import os.path
import sys
import json
import string
import os
import time
import datetime
import webbrowser


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        #Brojac predstavlja index slobodnog elementa baze
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        '''
        ###Additional GUI modifications for the basic information table of the database
        :A header is set, which is the same as in the label table, to keep the width of the columns the same.
        :For aesthetic reasons, the header is hidden. Not just a horizontal header but also a vertical header
        :As mentioned. The columns are set to adjust. So the right column adjusts to the width of the heading 
         for that column in the header. The left column elongates and takes up all the remaining width.
        '''
        self.ui.BassicLabelInfoTableWidget.setHorizontalHeaderLabels(['Name', 'Number'])

        self.ui.BassicLabelInfoTableWidget.horizontalHeader().setVisible(False)
        self.ui.BassicLabelInfoTableWidget.verticalHeader().setVisible(False)

        self.ui.BassicLabelInfoTableWidget.setRowCount(0)
        
        header = self.ui.BassicLabelInfoTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)  
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)


        '''
        ###Additional GUI modifications for the information view table for labels from the database.
        :Everything is identical to the basic information table
        '''
        self.ui.LabelTableWidget.setHorizontalHeaderLabels(['Name', 'Number'])
        
        self.ui.LabelTableWidget.horizontalHeader().setVisible(False)
        self.ui.LabelTableWidget.verticalHeader().setVisible(False)

        self.ui.LabelTableWidget.setRowCount(0)
        
        header = self.ui.LabelTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)  
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)


        '''
        ###Additional GUI modifications for the database overview table.
        :The header is placed in two columns (Sentence and Label).
        :For aesthetic reasons, the scroll bar is hidden.
        :The rest is the same as the table for reviewing basic database information.
        '''
        self.ui.DatasetTableWidget.setHorizontalHeaderLabels(['Sentence', 'Label'])
        #self.ui.DatasetTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.ui.DatasetTableWidget.setRowCount(0)

        header = self.ui.DatasetTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)  
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)



        self.ui.ResultLabelableWidget.setHorizontalHeaderLabels(['Name', 'Number'])
        
        self.ui.ResultLabelableWidget.horizontalHeader().setVisible(False)
        self.ui.ResultLabelableWidget.verticalHeader().setVisible(False)

        self.ui.ResultLabelableWidget.setRowCount(0)
        
        header = self.ui.ResultLabelableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)  
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)


        '''
        ###Button initialization.
        '''
        self.ui.actionOpen_File.triggered.connect(self.FileOpen)
        self.ui.LoadFileButton.clicked.connect(self.FileOpen)

        self.ui.actionExport_Model.triggered.connect(self.ExportModel)
        self.ui.ExportModelButton.clicked.connect(self.ExportModel)

        self.ui.actionLoad_Model.triggered.connect(self.LoadModel)

        self.ui.actionClear_All.triggered.connect(self.ClearAll)

        self.ui.actionExit.triggered.connect(self.ExitFunction)

        self.ui.DefineStopWordsButton.clicked.connect(self.StopWordsFileOpen)
        self.ui.DefineModelButton.clicked.connect(self.ModelFileOpen)

        self.ui.DefineDefaultPathButton.clicked.connect(self.DefinePathsToDefault)

        self.ui.TrainModelButton.clicked.connect(self.TrainModelPopup)

        self.ui.TestButton.clicked.connect(self.Test)

        self.ui.TestDataSizeButton.clicked.connect(self.GetTestDataSize)

        self.ui.TestLineEdit.returnPressed.connect(self.Test)

        self.ui.actionAbout.triggered.connect(self.About)


        self.PunctuationCBValue = False
        self.LowerCaseCBValue = False
        self.StopWordsCBValue = False
        self.AccuracyActivationCBValue = False

        self.ui.PunctuationCheckBox.stateChanged.connect(self.PunctuationCB)
        self.ui.LowerCaseCheckBox.stateChanged.connect(self.LowerCaseCB)
        self.ui.AccuracyCheckBox.stateChanged.connect(self.AccuracyActivationCB)

        self.ui.treeView.customContextMenuRequested.connect(self.FileTreeMenu)


        self.ui.StopWordsComboBox.currentIndexChanged.connect(self.StopWordsSelection)

        '''
        ###Initialization of variables used between functions.
        '''
        self.data = []
        self.tempData = []
        self.tempLabels = []
        self.bassicInfo = []
        self.AllLabels = {}
        self.DefaultPaths = {"StopWordsFname": ".\\stopwords.json", "ModelFname": "C:\\Users\\Public\\Documents\\MixerModelDataBackup"}
        self.DefinePaths = {}
        self.FileTreePath = "C:\\Users\\Public\\Documents\\MixerModelDataBackup"
        self.FilterLog = {"Punctuation": False, "LowerCase": False, "StopWords": "Disable"}


        self.StopWordsOptions = []

        self.StopWordsData = {}

        self.ModelValue = {}
        self.TestSentence = ""
        self.TestOutput = {}
        self.ExecutionTime = ""
        self.DataAndTime = ""
        self.TestSamplesData = []
        self.Data2 = []
        self.Accuracy = ""
        self.TestDataSizeValue = 10
        self.Temp_Data = []
        self.TestNumber = 10
        self.AccuracyToWrite = ""
        self.TestNumberToWrite = ""
        self.CollectedMainInfo = {}
        self.SentencesNumber = 0
        self.BassicLabelsNumber = 0
        self.UnlabeledNumber = 0
        self.LabeledNumber = 0
        self.LabelsNumber = []
        self.MainData = []
        self.StopWordsSelectedData = []
        self.FileTreeSelectedPath = ""
        self.LoadedModelData = []
        self.TrainModelCounter = 0
        self.LoadModelCounter = 0


        self.StopWordsItemsUpdate()

        self.LabelCounterTabel()
        self.BassicLabelInfoTable()
        self.PathChecker()
        self.FileTree()

        #self.main()
            
        self.LoadStopWordsList()

        self.StopWordsItemsUpdate()

        if not os.path.exists("C:\\Users\\Public\\Documents\\MixerModelDataBackup"):
            os.makedirs("C:\\Users\\Public\\Documents\\MixerModelDataBackup")

    ### MAIN ###

    def ExitFunction(self):
        self.close()
    
    def ClearAll(self):
        self.ui.DatasetTableWidget.setRowCount(0);
        self.ui.BassicLabelInfoTableWidget.setRowCount(0);
        self.ui.LabelTableWidget.setRowCount(0);
        self.ui.ResultLabelableWidget.setRowCount(0);

        self.ModelValue = {}
        self.TestSentence = ""
        self.TestOutput = {}
        self.ExecutionTime = ""
        self.DataAndTime = ""
        self.TestSamplesData = []
        self.Data2 = []
        self.data = []
        self.tempData = []
        self.tempLabels = []
        self.bassicInfo = []
        self.AllLabels = {}
        self.Temp_Data = []
        self.AccuracyToWrite = ""
        self.TestNumberToWrite = ""
        self.CollectedMainInfo = {}
        self.SentencesNumber = 0
        self.BassicLabelsNumber = 0
        self.UnlabeledNumber = 0
        self.LabeledNumber = 0
        self.LabelsNumber = []
        self.MainData = []
        self.StopWordsSelectedData = []
        self.TrainModelCounter = 0
        self.LoadModelCounter = 0
        self.LoadedModelData = []

        self.ui.DataAndTimeNumber.setText("None")
        self.ui.TestedNumber.setText("None")
        self.ui.AccuracyNumber.setText("None")
        self.ui.ExecutionTimeNumber.setText("None")

        self.ui.TestLineEdit.setText("")



    def FileOpen(self):
        '''
        ###The function with which data is collected and processed, for the first card (Main).
        :All the previous states of all the tables in the main tab are deleted and represent 
         the preparation for displaying new data.
        :FileDialog is initiated and the selected database opens.
        :Labels from the database are analyzed and converted to reasonable meaning.
         By modifying the initial database.
        :The functions that are performed when selecting a database, are called.
        '''
        self.ClearAll()

        self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Data files (*csv)")
        try:
            self.data = OpenDocument(self.fname[0])
        except:
            pass

        if self.data:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("Dataset loaded successfully. Please wait a while for the dataset to fully load.")
            msg.setIcon(QMessageBox.Information)
            msg.setInformativeText("(The waiting time depends on the amount of contents of the loaded dataset)")
            x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText('Dataset not loaded. The answer to the problem may be in the Mixer description (in the Menu -> About).')
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

        self.DataSetTable()
        self.BassicLabelInfoTable()
        self.LabelCounterTabel()
        self.data = Preprocess(self.data, self.FilterLog["Punctuation"], self.StopWordsSelectedData)
        self.CollectedMainInfo.update({"Data": [[row[0], row[1]] for row in self.data]})


        self.TestNumber = int((len(self.data)/100)*int(self.TestDataSizeValue))

        self.TestSamplesData = TestSamples(self.data, self.TestNumber)

        

    def LoadModelSupport(self):
        try:
            self.ModelValue = self.LoadedModelData["Model"]
            self.ExecutionTime = self.LoadedModelData["ExecutionTime"]
            self.DataAndTime = self.LoadedModelData["DataAndTime"]
            self.AccuracyToWrite = self.LoadedModelData["Accuracy"]
            self.TestNumberToWrite = self.LoadedModelData["TestedNumber"]

            self.SentencesNumber = self.LoadedModelData["Sentences"]
            self.BassicLabelsNumber = self.LoadedModelData["BassicLabels"]
            self.LabeledNumber = self.LoadedModelData["Labeled"]
            self.UnlabeledNumber = self.LoadedModelData["Unlabeled"]
            self.LabelsNumber = self.LoadedModelData["LabelsAndCount"]
            self.MainData = self.LoadedModelData["MainData"]

        
            if self.SentencesNumber == 0:
                pass
                #self.bassicInfo = [['Sentences','None'], ['Labels','None'], ['Labeled','None'], ['Unlabeled','None']]
            else:
                self.ui.BassicLabelInfoTableWidget.setRowCount(0);
                self.bassicInfo = [['Sentences',self.SentencesNumber], ['Labels',self.BassicLabelsNumber], ['Labeled',self.LabeledNumber], ['Unlabeled',self.UnlabeledNumber]]
            for rowNumber, rowData in enumerate(self.bassicInfo):
                self.ui.BassicLabelInfoTableWidget.insertRow(rowNumber)
                for colNumber, colData in enumerate(rowData):
                    self.ui.BassicLabelInfoTableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))
            
            self.ui.LabelTableWidget.setRowCount(0);
            for rowNumber, rowData in enumerate(self.LabelsNumber):
                self.ui.LabelTableWidget.insertRow(rowNumber)
                for colNumber, colData in enumerate(rowData):
                    self.ui.LabelTableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))
            
            self.ui.DatasetTableWidget.setRowCount(0);
            for rowNumber, rowData in enumerate(self.MainData):
                self.ui.DatasetTableWidget.insertRow(rowNumber)
                for colNumber, colData in enumerate(rowData):
                    self.ui.DatasetTableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))
        
        except:
            pass

    def LoadModel(self):
        
        try:
            self.ClearAll()

            if self.FileTreeSelectedPath is not "":
                with open(self.FileTreeSelectedPath, "r") as json_file:
                    self.LoadedModelData = json.load(json_file)
            else:
                fname = QFileDialog.getOpenFileName(self, 'Load Model', 'C:\\Users\\Public\\Documents\\MixerModelDataBackup', "Data files (*json)")
                with open(str(fname[0]), "r") as json_file:
                    self.LoadedModelData = json.load(json_file)
            self.LoadModelSupport()

            self.ui.DataAndTimeNumber.setText(self.DataAndTime)
            self.ui.TestedNumber.setText(self.TestNumberToWrite)
            self.ui.AccuracyNumber.setText(self.AccuracyToWrite)
            self.ui.ExecutionTimeNumber.setText(self.ExecutionTime)
            self.LoadModelCounter = 1
        except:
            pass
        
        self.FileTreeSelectedPath = ""


    def BassicLabelInfoTable(self):
        '''
        ###The loaded database is processed and basic information is extracted.
        :Basic information values are created.
        :The basic information is displayed in the table
        '''
        self.SentencesNumber = len(self.data)
        DataToDict = {item[0]:item[1] for item in self.data}
        self.AllLabels = [i for value in DataToDict.values() for i in value.split(', ')]
        self.BassicLabelsNumber = len([i for i in list(set(self.AllLabels)) if i is not ''])
        self.UnlabeledNumber = len([i for i in self.AllLabels if i is ''])
        self.LabeledNumber = self.SentencesNumber - self.UnlabeledNumber

        try:
            if self.SentencesNumber == 0:
                pass
                #self.bassicInfo = [['Sentences','None'], ['Labels','None'], ['Labeled','None'], ['Unlabeled','None']]
            else:
                self.ui.BassicLabelInfoTableWidget.setRowCount(0);
                self.bassicInfo = [['Sentences',self.SentencesNumber], ['Labels',self.BassicLabelsNumber], ['Labeled',self.LabeledNumber], ['Unlabeled',self.UnlabeledNumber]]
            for rowNumber, rowData in enumerate(self.bassicInfo):
                self.ui.BassicLabelInfoTableWidget.insertRow(rowNumber)
                for colNumber, colData in enumerate(rowData):
                    self.ui.BassicLabelInfoTableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))
            
            self.CollectedMainInfo.update({'Sentences': self.SentencesNumber, 'BassicLabels': self.BassicLabelsNumber, 'Labeled': self.LabeledNumber, 'Unlabeled': self.UnlabeledNumber})
        except:
            pass

    def LabelCounterTabel(self):
        '''
        ###The label information from the database is displayed.
        :Basic information about the labels themselves is analyzed at the entire database level.
        :Label information is displayed in the table
        '''
        LabelCounter = dict(zip(self.AllLabels,[self.AllLabels.count(i) for i in self.AllLabels]))
        self.LabelsNumber = [[k, v] for k, v in LabelCounter.items() if k is not '']
        #Prikaz baze u listi
        try:
            self.ui.LabelTableWidget.setRowCount(0);
            for rowNumber, rowData in enumerate(self.LabelsNumber):
                self.ui.LabelTableWidget.insertRow(rowNumber)
                for colNumber, colData in enumerate(rowData):
                    self.ui.LabelTableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))
            self.CollectedMainInfo.update({"LabelsNumber": self.LabelsNumber})
        except:
            pass

    def DataSetTable(self):
        '''
        ###The database itself is displayed in a table.
        '''
        try:
            for rowNumber, rowData in enumerate(self.data):
                self.ui.DatasetTableWidget.insertRow(rowNumber)
                for colNumber, colData in enumerate(rowData):
                    self.ui.DatasetTableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))
        except:
            pass

    def FileTree(self, tree=False):
        '''
        ###View created models from a previously defined folder.
        '''
        self.PathChecker()
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(self.FileTreePath))
        self.ui.treeView.setSortingEnabled(False)

        for i in range(1, self.ui.treeView.model().columnCount()):
            self.ui.treeView.header().hideSection(i)

    def FileTreeMenu(self):
        menu = QtWidgets.QMenu()
        openMenu = menu.addAction("Load")
        openMenu.triggered.connect(self.openMenuFunftion)
        deleteMenu = menu.addAction("Delete")
        deleteMenu.triggered.connect(self.deleteMenuFunftion)
        folderMenu = menu.addAction("Open Containing Folder...")
        folderMenu.triggered.connect(self.folderMenuFunftion)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def openMenuFunftion(self):
        indexItem = self.ui.treeView.currentIndex()
        self.FileTreeSelectedPath = self.model.filePath(indexItem)
        self.LoadModel()

    def deleteMenuFunftion(self):
        indexItem = self.ui.treeView.currentIndex()
        Path = self.model.filePath(indexItem)
        os.remove(Path)

    def folderMenuFunftion(self):
        indexItem = self.ui.treeView.currentIndex()
        Path = self.model.filePath(indexItem)
        Path = "/".join(Path.split("/")[:-1])
        os.startfile(Path)


    ### INITIALIZATION ###
    def StopWordsFileOpen(self):
        '''
        ###
        '''
        self.LoadDefinedPath()

        self.StopWordsFname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Data files (*.json)")
        
        with open(self.StopWordsFname[0], 'r')as json_file:
            self.StopWords = json.load(json_file)
        self.DefinePaths.update({'StopWordsFname': self.StopWordsFname[0]})

        with open('.\\PathGuard.json', 'w') as outfile:
            json.dump(self.DefinePaths, outfile)

        self.ui.DefineStopWordsPath.setText(self.DefinePaths['StopWordsFname'])
        self.LoadStopWordsList()
        self.StopWordsItemsUpdate()

    def ModelFileOpen(self):
        '''
        ###
        '''
        self.LoadDefinedPath()

        self.ModelFname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        self.DefinePaths.update({'ModelFname': self.ModelFname})
        self.ui.DefineModelPath.setText(self.ModelFname)

        with open('.\\PathGuard.json', 'w') as outfile:
            json.dump(self.DefinePaths, outfile)

        self.ui.DefineModelPath.setText(self.DefinePaths['ModelFname'])

        msg = QMessageBox()
        msg.setWindowTitle("Notification")
        msg.setText("You need to restart the program to see the full effect.")
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()


    def LoadDefinedPath(self):
        '''
        ###
        '''
        with open('.\\PathGuard.json', 'r')as json_file:
            self.DefinePaths = json.load(json_file)

    def PathChecker(self):
        '''
        ###
        '''
        self.LoadDefinedPath()

        if self.LoadDefinedPath is None or self.LoadDefinedPath is {}:
            self.ui.DefineStopWordsPath.setText(self.DefaultPaths['StopWordsFname'])
            self.ui.DefineModelPath.setText(self.DefaultPaths['ModelFname'])

            self.FileTreePath = self.DefaultPaths['ModelFname']
        else:
            try:
                if os.path.isfile(self.DefinePaths['StopWordsFname']):
                    self.ui.DefineStopWordsPath.setText(self.DefinePaths['StopWordsFname'])
                else:
                    self.ui.DefineStopWordsPath.setText('Path not defined. The default path is used')
            except:
                self.ui.DefineStopWordsPath.setText('Path not defined. The default path is used')
            try:
                if os.path.isdir(self.DefinePaths['ModelFname']):
                    self.ui.DefineModelPath.setText(self.DefinePaths['ModelFname'])
                else:
                    self.ui.DefineModelPath.setText('Path not defined. The default path is used')

                self.FileTreePath = self.DefinePaths['ModelFname']
            except:
                self.ui.DefineModelPath.setText('Path not defined. The default path is used')

    def DefinePathsToDefault(self):
        '''
        ###
        '''
        self.DefinePaths = {}

        with open('.\\PathGuard.json', 'w') as outfile:
            json.dump(self.DefinePaths, outfile)

        self.ui.DefineStopWordsPath.setText('Path not defined. The default path is used')
        self.ui.DefineModelPath.setText('Path not defined. The default path is used')

        self.DefinePaths = self.DefaultPaths

        msg = QMessageBox()
        msg.setWindowTitle("Notification")
        msg.setText("You need to restart the program to see the full effect.")
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

    def LoadStopWordsList(self):
        with open('.\\PathGuard.json', 'r')as json_file:
            self.DefinePaths = json.load(json_file)
        try:
            with open(self.DefinePaths["StopWordsFname"], 'r')as json_sw_file:
                self.StopWordsData = json.load(json_sw_file)
        except:
            with open(".\\stopwords.json", 'r')as json_sw_file:
                self.StopWordsData = json.load(json_sw_file)
        

    ### FILTERS ###

    def GetStopWordsLanguageList(self):
        for lang in self.StopWordsData:
            self.StopWordsOptions.append(lang["language"])
    
    def LowerCaseCB(self, state):
        '''
        ###
        '''
        if state == QtCore.Qt.Checked:
            self.FilterLog["LowerCase"] = True

        else:
            self.FilterLog["LowerCase"] = False

    def PunctuationCB(self, state):
        '''
        ###
        '''
        if state == QtCore.Qt.Checked:
            self.FilterLog["Punctuation"] = True
        else:
            self.FilterLog["Punctuation"] = False

    def AccuracyActivationCB(self, state):
        '''
        ###
        '''
        if state == QtCore.Qt.Checked:
            self.AccuracyActivationCBValue = True

        else:
            self.AccuracyActivationCBValue = False

    def StopWordsItemsUpdate(self):
        '''
        ###
        '''
        self.GetStopWordsLanguageList()
        for option in self.StopWordsOptions:
            self.ui.StopWordsComboBox.addItem(option)

    def StopWordsSelection(self):
        '''
        ###
        '''
        selectedStopWords = str(self.ui.StopWordsComboBox.currentText())
        if selectedStopWords == "Disable":
            self.FilterLog["StopWords"] = "Disable"
        else:
            self.FilterLog["StopWords"] = selectedStopWords
        try:
            for i_dict in self.StopWordsData:
                if i_dict['language'] == self.FilterLog["StopWords"]:
                    self.StopWordsSelectedData = i_dict["words"]
        except:
            self.StopWordsSelectedData = False
        

    def GetTestDataSize(self):
        self.TestDataSizeValue = self.ui.TestDataSizeLineEdit.text()


    def Test(self):
        try:
            self.TestSentence = self.ui.TestLineEdit.text()
            self.TestOutput = Test(self.ModelValue, self.TestSentence)

            self.TestSentence = " ".join(self.TestSentence.split())


            AdaptedData = [[k, v] for k, v in self.TestOutput.items() if k is not '']

            #MaxValue = max([v for v in self.TestOutput.values()])
            MaxValue = max(self.TestOutput.items(), key=operator.itemgetter(1))[0]
            MaxValue = [k for k,v in self.TestOutput.items() if v == self.TestOutput[MaxValue]]
            
            MaxValuesIndex = [AdaptedData.index(i) for i in AdaptedData for j in MaxValue if j in i]
            
            #Prikaz baze u listi
            self.ui.ResultLabelableWidget.setRowCount(0)

            PunctuationList = string.punctuation
        
            if self.TestSentence == "" or self.TestSentence in PunctuationList:
                pass
            else:
                for rowNumber, rowData in enumerate(AdaptedData):
                    self.ui.ResultLabelableWidget.insertRow(rowNumber)
                    for colNumber, colData in enumerate(rowData):
                        self.ui.ResultLabelableWidget.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(colData)))
                for MaxValueRowNumber in MaxValuesIndex:
                    self.ui.ResultLabelableWidget.item(MaxValueRowNumber, 0).setBackground(QtGui.QColor(0, 255, 0))
                    self.ui.ResultLabelableWidget.item(MaxValueRowNumber, 1).setBackground(QtGui.QColor(0, 255, 0))
                #setColortoRow(AdaptedData, MaxValueRowNumber, "#00ff00")
        except:
            pass

    def TrainModelPopup(self):
        if self.TrainModelCounter == 1 or self.LoadModelCounter == 1:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("The model has already been trained.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec_()
        elif self.TrainModelCounter == 0:
            msg0 = QMessageBox()
            msg0.setWindowTitle("Notification")
            msg0.setText("This may take some time, depending on the size of the database and the accuracy option (On = longer / Off = fast).")
            msg0.setIcon(QMessageBox.Information)
            msg0.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg0.setInformativeText("Are you sure you want to continue?")
            msg0.buttonClicked.connect(self.TrainModel)

            x = msg0.exec_()
        


    def TrainModel(self, selection):
        if str(selection.text()) == "&No":
            pass
        elif str(selection.text()) == "&Yes":
            start = time.time()
            self.ModelValue = LiveTrainModel(self.data)
            end = time.time()
            self.ExecutionTime = str(datetime.timedelta(seconds=int(end-start)))
            self.ui.ExecutionTimeNumber.setText(self.ExecutionTime)
            self.DataAndTime = "\n".join(str(datetime.datetime.now()).split(" "))
            self.ui.DataAndTimeNumber.setText(self.DataAndTime)
            self.Temp_Data = [[" ".join(row[0]), row[1]] for row in self.data]
            if self.AccuracyActivationCBValue:
                self.Accuracy = Accuracy(self.Temp_Data, self.ModelValue, self.TestSamplesData, self.TestNumber)
                self.AccuracyToWrite = str(int(self.Accuracy))+"%"
                self.ui.AccuracyNumber.setText(self.AccuracyToWrite)
                self.TestNumberToWrite = str(int(self.TestNumber))
                self.ui.TestedNumber.setText(self.TestNumberToWrite)
            else:
                self.AccuracyToWrite = "Disabled"
                self.ui.AccuracyNumber.setText(self.AccuracyToWrite)
                self.TestNumberToWrite = "Disabled"
                self.ui.TestedNumber.setText(self.TestNumberToWrite)
            
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("The training is complete.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec_()
            self.TrainModelCounter = 1
        else:
            pass

    def ExportModel(self):
        try:
            ToWrite = {}
            ToWrite.update({"Sentences": self.SentencesNumber})
            ToWrite.update({"BassicLabels": self.BassicLabelsNumber})
            ToWrite.update({"Labeled": self.LabeledNumber})
            ToWrite.update({"Unlabeled": self.UnlabeledNumber})
            ToWrite.update({"LabelsAndCount": self.LabelsNumber})
            ToWrite.update({"Accuracy": self.AccuracyToWrite})
            ToWrite.update({"ExecutionTime": self.ExecutionTime})
            ToWrite.update({"DataAndTime": self.DataAndTime})
            ToWrite.update({"TestedNumber": self.TestNumberToWrite})
            ToWrite.update({"MainData": self.CollectedMainInfo["Data"]})
            ToWrite.update({"Model": self.ModelValue})



            SaveFileName = QFileDialog.getSaveFileName(self, 'Save Model', 'C:\\Users\\Public\\Documents\\MixerModelDataBackup', "Data files (*json)")
            if SaveFileName:
                try:
                    if SaveFileName[0].split(".")[-1] == "json":
                        with open(SaveFileName[0], 'w') as outfile:
                            json.dump(ToWrite, outfile)
                    else:
                        with open(SaveFileName[0]+".json", 'w') as outfile:
                            json.dump(ToWrite, outfile)
                except:
                    with open(SaveFileName[0]+".json", 'w') as outfile:
                            json.dump(ToWrite, outfile)
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Notification")
            msg.setText("The model cannot be exported. Either a previously exported model is used or the database is not imported.")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec_()
        
    def About(self):
        webbrowser.open('https://github.com/user0706/Transcriptor', new=2)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())