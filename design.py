# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 645)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/MixerLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-background-color: #0023FF;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.MainTab)
        self.frame_2.setStyleSheet("max-width:200px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.BassicOverviewLabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BassicOverviewLabel.setFont(font)
        self.BassicOverviewLabel.setStyleSheet("min-width:150px;\n"
"max-width:150px;")
        self.BassicOverviewLabel.setObjectName("BassicOverviewLabel")
        self.verticalLayout_4.addWidget(self.BassicOverviewLabel)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setStyleSheet("min-width:150px;\n"
"max-width:150px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.BassicLabelInfoTableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.BassicLabelInfoTableWidget.setMaximumSize(QtCore.QSize(200, 160))
        self.BassicLabelInfoTableWidget.setStyleSheet("border:0px;")
        self.BassicLabelInfoTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.BassicLabelInfoTableWidget.setShowGrid(False)
        self.BassicLabelInfoTableWidget.setColumnCount(2)
        self.BassicLabelInfoTableWidget.setObjectName("BassicLabelInfoTableWidget")
        self.BassicLabelInfoTableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.BassicLabelInfoTableWidget)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.MainTab)
        self.frame.setStyleSheet("max-width:200px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LabelsOvervieLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LabelsOvervieLabel.setFont(font)
        self.LabelsOvervieLabel.setStyleSheet("min-width:150px;\n"
"max-width:150px;")
        self.LabelsOvervieLabel.setObjectName("LabelsOvervieLabel")
        self.verticalLayout_5.addWidget(self.LabelsOvervieLabel)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setStyleSheet("min-width:150px;\n"
"max-width:150px;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.LabelTableWidget = QtWidgets.QTableWidget(self.frame)
        self.LabelTableWidget.setMinimumSize(QtCore.QSize(0, 280))
        self.LabelTableWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LabelTableWidget.setStyleSheet("border:0px;")
        self.LabelTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.LabelTableWidget.setShowGrid(False)
        self.LabelTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.LabelTableWidget.setColumnCount(2)
        self.LabelTableWidget.setObjectName("LabelTableWidget")
        self.LabelTableWidget.setRowCount(0)
        self.verticalLayout_5.addWidget(self.LabelTableWidget)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.DatasetTableWidgetLayout = QtWidgets.QVBoxLayout()
        self.DatasetTableWidgetLayout.setObjectName("DatasetTableWidgetLayout")
        self.DatasetTableWidget = QtWidgets.QTableWidget(self.MainTab)
        self.DatasetTableWidget.setStyleSheet("border:0px")
        self.DatasetTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.DatasetTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.DatasetTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.DatasetTableWidget.setColumnCount(2)
        self.DatasetTableWidget.setObjectName("DatasetTableWidget")
        self.DatasetTableWidget.setRowCount(0)
        self.DatasetTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.DatasetTableWidgetLayout.addWidget(self.DatasetTableWidget)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.DatasetTableWidgetLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_4.addLayout(self.DatasetTableWidgetLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.LoadFileButton = QtWidgets.QPushButton(self.MainTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.LoadFileButton.setFont(font)
        self.LoadFileButton.setStyleSheet("QPushButton{ \n"
"    background-color: #FF5001;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #FF5001; }\n"
"QPushButton:hover{ background-color: #eb4900; }")
        self.LoadFileButton.setObjectName("LoadFileButton")
        self.horizontalLayout.addWidget(self.LoadFileButton)
        self.TrainModelButton = QtWidgets.QPushButton(self.MainTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.TrainModelButton.setFont(font)
        self.TrainModelButton.setStyleSheet("QPushButton{ \n"
"    background-color: #0023FF;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #0023FF; }\n"
"QPushButton:hover{ background-color: #001cc9; }")
        self.TrainModelButton.setObjectName("TrainModelButton")
        self.horizontalLayout.addWidget(self.TrainModelButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.MainTab, "")
        self.ResultsTab = QtWidgets.QWidget()
        self.ResultsTab.setObjectName("ResultsTab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.ResultsTab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.AccuracyLabel = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.AccuracyLabel.setFont(font)
        self.AccuracyLabel.setStyleSheet("min-height:20px;\n"
"max-height:20px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.AccuracyLabel.setObjectName("AccuracyLabel")
        self.verticalLayout_15.addWidget(self.AccuracyLabel)
        self.AccuracyNumber = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AccuracyNumber.setFont(font)
        self.AccuracyNumber.setStyleSheet("min-height:35px;\n"
"max-height:35px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.AccuracyNumber.setObjectName("AccuracyNumber")
        self.verticalLayout_15.addWidget(self.AccuracyNumber)
        self.verticalLayout_8.addLayout(self.verticalLayout_15)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_19.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.ExecutionTimeLabel = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ExecutionTimeLabel.setFont(font)
        self.ExecutionTimeLabel.setStyleSheet("min-height:20px;\n"
"max-height:20px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.ExecutionTimeLabel.setObjectName("ExecutionTimeLabel")
        self.verticalLayout_16.addWidget(self.ExecutionTimeLabel)
        self.ExecutionTimeNumber = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ExecutionTimeNumber.setFont(font)
        self.ExecutionTimeNumber.setStyleSheet("min-height:35px;\n"
"max-height:35px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.ExecutionTimeNumber.setObjectName("ExecutionTimeNumber")
        self.verticalLayout_16.addWidget(self.ExecutionTimeNumber)
        self.verticalLayout_9.addLayout(self.verticalLayout_16)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem11)
        self.horizontalLayout_19.addLayout(self.verticalLayout_9)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem12)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.DataAndTimeLabel = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DataAndTimeLabel.setFont(font)
        self.DataAndTimeLabel.setStyleSheet("min-height:20px;\n"
"max-height:20px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.DataAndTimeLabel.setObjectName("DataAndTimeLabel")
        self.verticalLayout_19.addWidget(self.DataAndTimeLabel)
        self.DataAndTimeNumber = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DataAndTimeNumber.setFont(font)
        self.DataAndTimeNumber.setStyleSheet("min-height:35px;\n"
"max-height:35px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.DataAndTimeNumber.setObjectName("DataAndTimeNumber")
        self.verticalLayout_19.addWidget(self.DataAndTimeNumber)
        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem13)
        self.horizontalLayout_19.addLayout(self.verticalLayout_18)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem14)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.TestedLabel = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.TestedLabel.setFont(font)
        self.TestedLabel.setStyleSheet("min-height:20px;\n"
"max-height:20px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.TestedLabel.setObjectName("TestedLabel")
        self.verticalLayout_17.addWidget(self.TestedLabel)
        self.TestedNumber = QtWidgets.QLabel(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TestedNumber.setFont(font)
        self.TestedNumber.setStyleSheet("min-height:35px;\n"
"max-height:35px;\n"
"min-width:110px;\n"
"max-width:110px;")
        self.TestedNumber.setObjectName("TestedNumber")
        self.verticalLayout_17.addWidget(self.TestedNumber)
        self.verticalLayout_10.addLayout(self.verticalLayout_17)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem15)
        self.horizontalLayout_19.addLayout(self.verticalLayout_10)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem16)
        self.verticalLayout_13.addLayout(self.horizontalLayout_19)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.TestLineEdit = QtWidgets.QLineEdit(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.TestLineEdit.setFont(font)
        self.TestLineEdit.setStyleSheet("max-width:500px;\n"
"min-width:500px;\n"
"max-height:20px;\n"
"min-height:20px;")
        self.TestLineEdit.setObjectName("TestLineEdit")
        self.verticalLayout_12.addWidget(self.TestLineEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TestButton = QtWidgets.QPushButton(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.TestButton.setFont(font)
        self.TestButton.setStyleSheet("QPushButton{ \n"
"    background-color: #0023FF;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #0023FF; }\n"
"QPushButton:hover{ background-color: #001cc9; }")
        self.TestButton.setObjectName("TestButton")
        self.verticalLayout_12.addWidget(self.TestButton, 0, QtCore.Qt.AlignHCenter)
        self.ResultLabelableWidget = QtWidgets.QTableWidget(self.ResultsTab)
        self.ResultLabelableWidget.setStyleSheet("max-height:200px;\n"
"min-height:200px;\n"
"border:0px")
        self.ResultLabelableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ResultLabelableWidget.setTabKeyNavigation(False)
        self.ResultLabelableWidget.setProperty("showDropIndicator", False)
        self.ResultLabelableWidget.setDragDropOverwriteMode(False)
        self.ResultLabelableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.ResultLabelableWidget.setShowGrid(False)
        self.ResultLabelableWidget.setColumnCount(2)
        self.ResultLabelableWidget.setObjectName("ResultLabelableWidget")
        self.ResultLabelableWidget.setRowCount(0)
        self.verticalLayout_12.addWidget(self.ResultLabelableWidget, 0, QtCore.Qt.AlignHCenter)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem17)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem18)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem19)
        self.ExportModelButton = QtWidgets.QPushButton(self.ResultsTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ExportModelButton.setFont(font)
        self.ExportModelButton.setStyleSheet("QPushButton{ \n"
"    background-color: #0023FF;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #0023FF; }\n"
"QPushButton:hover{ background-color: #001cc9; }")
        self.ExportModelButton.setObjectName("ExportModelButton")
        self.horizontalLayout_20.addWidget(self.ExportModelButton)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem20)
        self.verticalLayout_13.addLayout(self.horizontalLayout_20)
        self.tabWidget.addTab(self.ResultsTab, "")
        self.FiltersTab = QtWidgets.QWidget()
        self.FiltersTab.setObjectName("FiltersTab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.FiltersTab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem21)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.FiltersLabel = QtWidgets.QLabel(self.FiltersTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.FiltersLabel.setFont(font)
        self.FiltersLabel.setObjectName("FiltersLabel")
        self.verticalLayout_20.addWidget(self.FiltersLabel)
        self.line_3 = QtWidgets.QFrame(self.FiltersTab)
        self.line_3.setStyleSheet("min-width: 150px;\n"
"max-width: 150px;\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_20.addWidget(self.line_3)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.PunctuationCheckBox = QtWidgets.QCheckBox(self.FiltersTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.PunctuationCheckBox.setFont(font)
        self.PunctuationCheckBox.setObjectName("PunctuationCheckBox")
        self.verticalLayout_21.addWidget(self.PunctuationCheckBox)
        self.LowerCaseCheckBox = QtWidgets.QCheckBox(self.FiltersTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.LowerCaseCheckBox.setFont(font)
        self.LowerCaseCheckBox.setObjectName("LowerCaseCheckBox")
        self.verticalLayout_21.addWidget(self.LowerCaseCheckBox)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.FiltersTab)
        self.label_2.setStyleSheet("min-width:50px;\n"
"max-width:50px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.StopWordsComboBox = QtWidgets.QComboBox(self.FiltersTab)
        self.StopWordsComboBox.setObjectName("StopWordsComboBox")
        self.horizontalLayout_8.addWidget(self.StopWordsComboBox)
        self.verticalLayout_21.addLayout(self.horizontalLayout_8)
        self.verticalLayout_20.addLayout(self.verticalLayout_21)
        self.FiltersLabel_2 = QtWidgets.QLabel(self.FiltersTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.FiltersLabel_2.setFont(font)
        self.FiltersLabel_2.setStyleSheet("padding-top:15px;")
        self.FiltersLabel_2.setObjectName("FiltersLabel_2")
        self.verticalLayout_20.addWidget(self.FiltersLabel_2)
        self.line_4 = QtWidgets.QFrame(self.FiltersTab)
        self.line_4.setStyleSheet("min-width: 150px;\n"
"max-width: 150px;\n"
"")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_20.addWidget(self.line_4)
        self.AccuracyCheckBox = QtWidgets.QCheckBox(self.FiltersTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.AccuracyCheckBox.setFont(font)
        self.AccuracyCheckBox.setObjectName("AccuracyCheckBox")
        self.verticalLayout_20.addWidget(self.AccuracyCheckBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.TestDataSizeLineEdit = QtWidgets.QLineEdit(self.FiltersTab)
        self.TestDataSizeLineEdit.setStyleSheet("max-height:20px;\n"
"min-height:20px;")
        self.TestDataSizeLineEdit.setObjectName("TestDataSizeLineEdit")
        self.horizontalLayout_6.addWidget(self.TestDataSizeLineEdit)
        self.TestDataSizeButton = QtWidgets.QPushButton(self.FiltersTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.TestDataSizeButton.setFont(font)
        self.TestDataSizeButton.setStyleSheet("QPushButton{ \n"
"    background-color: #0023FF;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #0023FF; }\n"
"QPushButton:hover{ background-color: #001cc9; }")
        self.TestDataSizeButton.setObjectName("TestDataSizeButton")
        self.horizontalLayout_6.addWidget(self.TestDataSizeButton)
        self.verticalLayout_20.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_20)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem23)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem24)
        self.tabWidget.addTab(self.FiltersTab, "")
        self.InitializationTab = QtWidgets.QWidget()
        self.InitializationTab.setObjectName("InitializationTab")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.InitializationTab)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.DefineStopWordsFrame = QtWidgets.QFrame(self.InitializationTab)
        self.DefineStopWordsFrame.setStyleSheet("")
        self.DefineStopWordsFrame.setObjectName("DefineStopWordsFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.DefineStopWordsFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.DefineStopWordsLabel = QtWidgets.QLabel(self.DefineStopWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.DefineStopWordsLabel.setFont(font)
        self.DefineStopWordsLabel.setObjectName("DefineStopWordsLabel")
        self.verticalLayout_7.addWidget(self.DefineStopWordsLabel)
        self.line_6 = QtWidgets.QFrame(self.DefineStopWordsFrame)
        self.line_6.setStyleSheet("min-width:63px;\n"
"max-width:63px;")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_7.addWidget(self.line_6)
        self.DefineStopWordsDescription = QtWidgets.QLabel(self.DefineStopWordsFrame)
        self.DefineStopWordsDescription.setObjectName("DefineStopWordsDescription")
        self.verticalLayout_7.addWidget(self.DefineStopWordsDescription)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.DefineStopWordsPath = QtWidgets.QLabel(self.DefineStopWordsFrame)
        self.DefineStopWordsPath.setStyleSheet("")
        self.DefineStopWordsPath.setObjectName("DefineStopWordsPath")
        self.horizontalLayout_13.addWidget(self.DefineStopWordsPath)
        self.DefineStopWordsButton = QtWidgets.QPushButton(self.DefineStopWordsFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DefineStopWordsButton.setFont(font)
        self.DefineStopWordsButton.setStyleSheet("QPushButton{ \n"
"    background-color: #0023FF;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #0023FF; }\n"
"QPushButton:hover{ background-color: #001cc9; }")
        self.DefineStopWordsButton.setObjectName("DefineStopWordsButton")
        self.horizontalLayout_13.addWidget(self.DefineStopWordsButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.verticalLayout_14.addWidget(self.DefineStopWordsFrame)
        self.DefineModelFrame = QtWidgets.QFrame(self.InitializationTab)
        self.DefineModelFrame.setObjectName("DefineModelFrame")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.DefineModelFrame)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.DefineModelLabel = QtWidgets.QLabel(self.DefineModelFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.DefineModelLabel.setFont(font)
        self.DefineModelLabel.setObjectName("DefineModelLabel")
        self.verticalLayout_24.addWidget(self.DefineModelLabel)
        self.line_9 = QtWidgets.QFrame(self.DefineModelFrame)
        self.line_9.setStyleSheet("min-width:33px;\n"
"max-width:33px;")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_24.addWidget(self.line_9)
        self.DefineModelDescription = QtWidgets.QLabel(self.DefineModelFrame)
        self.DefineModelDescription.setObjectName("DefineModelDescription")
        self.verticalLayout_24.addWidget(self.DefineModelDescription)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.DefineModelPath = QtWidgets.QLabel(self.DefineModelFrame)
        self.DefineModelPath.setObjectName("DefineModelPath")
        self.horizontalLayout_15.addWidget(self.DefineModelPath)
        self.DefineModelButton = QtWidgets.QPushButton(self.DefineModelFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DefineModelButton.setFont(font)
        self.DefineModelButton.setStyleSheet("QPushButton{ \n"
"    background-color: #0023FF;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #0023FF; }\n"
"QPushButton:hover{ background-color: #001cc9; }")
        self.DefineModelButton.setObjectName("DefineModelButton")
        self.horizontalLayout_15.addWidget(self.DefineModelButton)
        self.verticalLayout_24.addLayout(self.horizontalLayout_15)
        self.verticalLayout_14.addWidget(self.DefineModelFrame)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem25)
        self.DefineDefaultPathButton = QtWidgets.QPushButton(self.InitializationTab)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DefineDefaultPathButton.setFont(font)
        self.DefineDefaultPathButton.setStyleSheet("QPushButton{ \n"
"    background-color: #FF5001;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: beige;\n"
"    max-width: 75px;\n"
"    min-width: 75px;\n"
"    max-height:25px;\n"
"    min-height:25px;\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:pressed{ background-color: #FF5001; }\n"
"QPushButton:hover{ background-color: #eb4900; }")
        self.DefineDefaultPathButton.setObjectName("DefineDefaultPathButton")
        self.verticalLayout_14.addWidget(self.DefineDefaultPathButton, 0, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.InitializationTab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setMouseTracking(True)
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_3.addWidget(self.treeView, 0, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExport_Model = QtWidgets.QAction(MainWindow)
        self.actionExport_Model.setObjectName("actionExport_Model")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionInitialization = QtWidgets.QAction(MainWindow)
        self.actionInitialization.setObjectName("actionInitialization")
        self.actionLoad_Model = QtWidgets.QAction(MainWindow)
        self.actionLoad_Model.setObjectName("actionLoad_Model")
        self.actionClear_All = QtWidgets.QAction(MainWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionOpen_File)
        self.menuMenu.addAction(self.actionLoad_Model)
        self.menuMenu.addAction(self.actionExport_Model)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionClear_All)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mixer"))
        self.BassicOverviewLabel.setText(_translate("MainWindow", "Basic overview"))
        self.LabelsOvervieLabel.setText(_translate("MainWindow", "Labels overview"))
        self.LoadFileButton.setText(_translate("MainWindow", "Load File"))
        self.TrainModelButton.setText(_translate("MainWindow", "Train"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), _translate("MainWindow", "Main"))
        self.AccuracyLabel.setText(_translate("MainWindow", "Accuracy"))
        self.AccuracyNumber.setText(_translate("MainWindow", "None"))
        self.ExecutionTimeLabel.setText(_translate("MainWindow", "Execution Time"))
        self.ExecutionTimeNumber.setText(_translate("MainWindow", "None"))
        self.DataAndTimeLabel.setText(_translate("MainWindow", "Data and Time"))
        self.DataAndTimeNumber.setText(_translate("MainWindow", "None"))
        self.TestedLabel.setText(_translate("MainWindow", "Tested"))
        self.TestedNumber.setText(_translate("MainWindow", "None"))
        self.TestButton.setText(_translate("MainWindow", "Test"))
        self.ExportModelButton.setText(_translate("MainWindow", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ResultsTab), _translate("MainWindow", "Results"))
        self.FiltersLabel.setText(_translate("MainWindow", "Filters"))
        self.PunctuationCheckBox.setText(_translate("MainWindow", "Punctuations"))
        self.LowerCaseCheckBox.setText(_translate("MainWindow", "Lower Case"))
        self.label_2.setText(_translate("MainWindow", "Stop Words"))
        self.FiltersLabel_2.setText(_translate("MainWindow", "Accuracy"))
        self.AccuracyCheckBox.setText(_translate("MainWindow", "Activation"))
        self.TestDataSizeButton.setText(_translate("MainWindow", "Ok"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FiltersTab), _translate("MainWindow", "Filters"))
        self.DefineStopWordsLabel.setText(_translate("MainWindow", "Stop words"))
        self.DefineStopWordsDescription.setText(_translate("MainWindow", "Select the file containing the stop words. For an example of the structure, see About under the \"stop word\" section."))
        self.DefineStopWordsPath.setText(_translate("MainWindow", "The path is not defined"))
        self.DefineStopWordsButton.setText(_translate("MainWindow", "Browse"))
        self.DefineModelLabel.setText(_translate("MainWindow", "Model"))
        self.DefineModelDescription.setText(_translate("MainWindow", "Select a folder for backup models. For more information, see About under the \"backup model\" section."))
        self.DefineModelPath.setText(_translate("MainWindow", "The path is not defined"))
        self.DefineModelButton.setText(_translate("MainWindow", "Browse"))
        self.DefineDefaultPathButton.setText(_translate("MainWindow", "Default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InitializationTab), _translate("MainWindow", "Initialization"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen_File.setText(_translate("MainWindow", "Load File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionPreferences.setText(_translate("MainWindow", "Filters"))
        self.actionExport_Model.setText(_translate("MainWindow", "Export Model"))
        self.actionExport_Model.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInitialization.setText(_translate("MainWindow", "Initialization"))
        self.actionLoad_Model.setText(_translate("MainWindow", "Load Model"))
        self.actionLoad_Model.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionClear_All.setText(_translate("MainWindow", "Clear All"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
