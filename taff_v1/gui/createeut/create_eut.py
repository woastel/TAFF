# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_eut.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(924, 836)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 337, 652))
        self.page.setObjectName("page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 1)
        self.listWidget_eut = QtWidgets.QListWidget(self.page)
        self.listWidget_eut.setObjectName("listWidget_eut")
        self.gridLayout_8.addWidget(self.listWidget_eut, 1, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 98, 119))
        self.page_2.setObjectName("page_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_10.addWidget(self.label_24, 0, 0, 1, 1)
        self.listWidget_configs = QtWidgets.QListWidget(self.page_2)
        self.listWidget_configs.setObjectName("listWidget_configs")
        self.gridLayout_10.addWidget(self.listWidget_configs, 1, 0, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 98, 119))
        self.page_3.setObjectName("page_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_25 = QtWidgets.QLabel(self.page_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_11.addWidget(self.label_25, 0, 0, 1, 1)
        self.listWidget_pcietable = QtWidgets.QListWidget(self.page_3)
        self.listWidget_pcietable.setObjectName("listWidget_pcietable")
        self.gridLayout_11.addWidget(self.listWidget_pcietable, 1, 0, 1, 1)
        self.toolBox.addItem(self.page_3, "")
        self.gridLayout_12.addWidget(self.toolBox, 1, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.btn_loaddatas = QtWidgets.QPushButton(self.frame_4)
        self.btn_loaddatas.setObjectName("btn_loaddatas")
        self.gridLayout.addWidget(self.btn_loaddatas, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_4, 0, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_eut_systemid = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_eut_systemid.setObjectName("comboBox_eut_systemid")
        self.gridLayout_3.addWidget(self.comboBox_eut_systemid, 3, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_eut_name = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_eut_name.setObjectName("lineEdit_eut_name")
        self.gridLayout_3.addWidget(self.lineEdit_eut_name, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_eut_configid = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_eut_configid.setObjectName("comboBox_eut_configid")
        self.gridLayout_3.addWidget(self.comboBox_eut_configid, 4, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.btn_createEUT = QtWidgets.QPushButton(self.frame_2)
        self.btn_createEUT.setObjectName("btn_createEUT")
        self.gridLayout_3.addWidget(self.btn_createEUT, 5, 2, 1, 1)
        self.lineEdit_eut_info = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_eut_info.setObjectName("lineEdit_eut_info")
        self.gridLayout_3.addWidget(self.lineEdit_eut_info, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_createConfig = QtWidgets.QPushButton(self.frame_3)
        self.btn_createConfig.setObjectName("btn_createConfig")
        self.gridLayout_5.addWidget(self.btn_createConfig, 13, 2, 1, 1)
        self.comboBox_config_pcietableid = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_config_pcietableid.setObjectName("comboBox_config_pcietableid")
        self.gridLayout_5.addWidget(self.comboBox_config_pcietableid, 12, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 8, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 9, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 12, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 13, 0, 1, 2)
        self.comboBox_config_memid = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_config_memid.setObjectName("comboBox_config_memid")
        self.gridLayout_5.addWidget(self.comboBox_config_memid, 9, 1, 1, 2)
        self.lineEdit_config_memcount = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_config_memcount.setObjectName("lineEdit_config_memcount")
        self.gridLayout_5.addWidget(self.lineEdit_config_memcount, 8, 1, 1, 2)
        self.comboBox_config_cpuid = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_config_cpuid.setObjectName("comboBox_config_cpuid")
        self.gridLayout_5.addWidget(self.comboBox_config_cpuid, 7, 1, 1, 2)
        self.lineEdit_config_cpucount = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_config_cpucount.setObjectName("lineEdit_config_cpucount")
        self.gridLayout_5.addWidget(self.lineEdit_config_cpucount, 6, 1, 1, 2)
        self.comboBox_config_hddid = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_config_hddid.setObjectName("comboBox_config_hddid")
        self.gridLayout_5.addWidget(self.comboBox_config_hddid, 5, 1, 1, 2)
        self.lineEdit_config_hddcount = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_config_hddcount.setObjectName("lineEdit_config_hddcount")
        self.gridLayout_5.addWidget(self.lineEdit_config_hddcount, 4, 1, 1, 2)
        self.comboBox_config_moboid = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_config_moboid.setObjectName("comboBox_config_moboid")
        self.gridLayout_5.addWidget(self.comboBox_config_moboid, 3, 1, 1, 2)
        self.comboBox_config_chassisid = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_config_chassisid.setObjectName("comboBox_config_chassisid")
        self.gridLayout_5.addWidget(self.comboBox_config_chassisid, 2, 1, 1, 2)
        self.lineEdit_config_info = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_config_info.setObjectName("lineEdit_config_info")
        self.gridLayout_5.addWidget(self.lineEdit_config_info, 1, 1, 1, 2)
        self.lineEdit_config_name = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_config_name.setObjectName("lineEdit_config_name")
        self.gridLayout_5.addWidget(self.lineEdit_config_name, 0, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 11, 0, 1, 1)
        self.comboBox_config_psu = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_config_psu.setObjectName("comboBox_config_psu")
        self.gridLayout_5.addWidget(self.comboBox_config_psu, 11, 1, 1, 2)
        self.lineEdit_config_psucount = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_config_psucount.setObjectName("lineEdit_config_psucount")
        self.gridLayout_5.addWidget(self.lineEdit_config_psucount, 10, 1, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 10, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_13.addWidget(self.label_26, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_7.addWidget(self.label_23, 16, 0, 1, 1)
        self.btn_create_PCIeTable = QtWidgets.QPushButton(self.widget)
        self.btn_create_PCIeTable.setObjectName("btn_create_PCIeTable")
        self.gridLayout_7.addWidget(self.btn_create_PCIeTable, 17, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 17, 0, 1, 2)
        self.comboBox_ctrl15 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl15.setObjectName("comboBox_ctrl15")
        self.gridLayout_7.addWidget(self.comboBox_ctrl15, 16, 1, 1, 2)
        self.comboBox_ctrl14 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl14.setObjectName("comboBox_ctrl14")
        self.gridLayout_7.addWidget(self.comboBox_ctrl14, 15, 1, 1, 2)
        self.comboBox_ctrl13 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl13.setObjectName("comboBox_ctrl13")
        self.gridLayout_7.addWidget(self.comboBox_ctrl13, 14, 1, 1, 2)
        self.comboBox_ctrl12 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl12.setObjectName("comboBox_ctrl12")
        self.gridLayout_7.addWidget(self.comboBox_ctrl12, 13, 1, 1, 2)
        self.comboBox_ctrl11 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl11.setObjectName("comboBox_ctrl11")
        self.gridLayout_7.addWidget(self.comboBox_ctrl11, 12, 1, 1, 2)
        self.comboBox_ctrl10 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl10.setObjectName("comboBox_ctrl10")
        self.gridLayout_7.addWidget(self.comboBox_ctrl10, 11, 1, 1, 2)
        self.comboBox_ctrl09 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl09.setObjectName("comboBox_ctrl09")
        self.gridLayout_7.addWidget(self.comboBox_ctrl09, 10, 1, 1, 2)
        self.comboBox_ctrl08 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl08.setObjectName("comboBox_ctrl08")
        self.gridLayout_7.addWidget(self.comboBox_ctrl08, 9, 1, 1, 2)
        self.comboBox_ctrl07 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl07.setObjectName("comboBox_ctrl07")
        self.gridLayout_7.addWidget(self.comboBox_ctrl07, 8, 1, 1, 2)
        self.comboBox_ctrl06 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl06.setObjectName("comboBox_ctrl06")
        self.gridLayout_7.addWidget(self.comboBox_ctrl06, 7, 1, 1, 2)
        self.comboBox_ctrl05 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl05.setObjectName("comboBox_ctrl05")
        self.gridLayout_7.addWidget(self.comboBox_ctrl05, 6, 1, 1, 2)
        self.comboBox_ctrl04 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl04.setObjectName("comboBox_ctrl04")
        self.gridLayout_7.addWidget(self.comboBox_ctrl04, 5, 1, 1, 2)
        self.comboBox_ctrl03 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl03.setObjectName("comboBox_ctrl03")
        self.gridLayout_7.addWidget(self.comboBox_ctrl03, 4, 1, 1, 2)
        self.comboBox_ctrl02 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl02.setObjectName("comboBox_ctrl02")
        self.gridLayout_7.addWidget(self.comboBox_ctrl02, 3, 1, 1, 2)
        self.comboBox_ctrl01 = QtWidgets.QComboBox(self.widget)
        self.comboBox_ctrl01.setObjectName("comboBox_ctrl01")
        self.gridLayout_7.addWidget(self.comboBox_ctrl01, 2, 1, 1, 2)
        self.lineEdit_pcie_t_info = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_pcie_t_info.setObjectName("lineEdit_pcie_t_info")
        self.gridLayout_7.addWidget(self.lineEdit_pcie_t_info, 1, 1, 1, 2)
        self.lineEdit_pcie_t_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_pcie_t_name.setObjectName("lineEdit_pcie_t_name")
        self.gridLayout_7.addWidget(self.lineEdit_pcie_t_name, 0, 1, 1, 2)
        self.gridLayout_13.addWidget(self.widget, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem6, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_12.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_18.setText(_translate("Form", "TextLabel"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "EUT list"))
        self.label_24.setText(_translate("Form", "TextLabel"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Configuration List"))
        self.label_25.setText(_translate("Form", "TextLabel"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "PCIe Controller List"))
        self.btn_loaddatas.setText(_translate("Form", "load data"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Create a EUT</span></p><p>you neet to be difine a Name, Info, System (id) and a Configuration (id).</p><p>Please create first a Configuration.</p></body></html>"))
        self.label_3.setText(_translate("Form", "[EUT] System (id):"))
        self.label.setText(_translate("Form", "[EUT] Name:"))
        self.label_4.setText(_translate("Form", "[EUT] Configuration (id):"))
        self.btn_createEUT.setText(_translate("Form", "Create EUT"))
        self.label_2.setText(_translate("Form", "[EUT] Info:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "EUT"))
        self.btn_createConfig.setText(_translate("Form", "create configuration"))
        self.label_8.setText(_translate("Form", "[CONFIG] Name:"))
        self.label_10.setText(_translate("Form", "[CONFIG] Info:"))
        self.label_7.setText(_translate("Form", "[CONFIG] Chassis (id):"))
        self.label_9.setText(_translate("Form", "[CONFIG] MoBo (id):"))
        self.label_15.setText(_translate("Form", "[CONFIG] HDD Count:"))
        self.label_11.setText(_translate("Form", "[CONFIG] HDD (id):"))
        self.label_16.setText(_translate("Form", "[CONFIG] CPU Count:"))
        self.label_12.setText(_translate("Form", "[CONFIG] CPU (id):"))
        self.label_14.setText(_translate("Form", "[CONFIG] MEM Count:"))
        self.label_17.setText(_translate("Form", "[CONFIG] MEM (id):"))
        self.label_13.setText(_translate("Form", "[CONFIG] PCIe Ctrl Table (id):"))
        self.label_19.setText(_translate("Form", "[CONFIG] PSU (id):"))
        self.label_27.setText(_translate("Form", "[CONFIG] PSU Count:"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Create a Configuration</span></p><p>you neet to be difine a Name, Info, System (id) and a Configuration (id).</p><p>Please create first a Configuration.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Configuration"))
        self.label_26.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Create a Configuration</span></p><p>you neet to be difine a Name, Info, System (id) and a Configuration (id).</p><p>Please create first a Configuration.</p></body></html>"))
        self.label_20.setText(_translate("Form", "PCIeCtrlList Name:"))
        self.label_21.setText(_translate("Form", "PCIeCtrlList Info:"))
        self.label_22.setText(_translate("Form", "PCIe Ctrl #1"))
        self.label_23.setText(_translate("Form", "PCIe Ctrl #15"))
        self.btn_create_PCIeTable.setText(_translate("Form", "create PCIe Ctrl. Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "PCIe Ctrl Table"))
