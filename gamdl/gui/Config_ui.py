# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QScrollArea, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        Configuration.resize(640, 360)
        Configuration.setMinimumSize(QSize(640, 360))
        self.gridLayout = QGridLayout(Configuration)
        self.gridLayout.setObjectName(u"gridLayout")
        self.version = QHBoxLayout()
        self.version.setObjectName(u"version")
        self.version_text = QLabel(Configuration)
        self.version_text.setObjectName(u"version_text")
        self.version_text.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.version_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.version.addWidget(self.version_text)

        self.version_label = QLabel(Configuration)
        self.version_label.setObjectName(u"version_label")

        self.version.addWidget(self.version_label)


        self.gridLayout.addLayout(self.version, 1, 1, 1, 1)

        self.tabWidget = QTabWidget(Configuration)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.Common_tab = QWidget()
        self.Common_tab.setObjectName(u"Common_tab")
        self.horizontalLayout = QHBoxLayout(self.Common_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.Common_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(500, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 269))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_5.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_6.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_7.addWidget(self.comboBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_8.addWidget(self.comboBox_5)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.comboBox_6 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_9.addWidget(self.comboBox_6)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.comboBox_7 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_10.addWidget(self.comboBox_7)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.Common_tab, "")
        self.Path_Tab = QWidget()
        self.Path_Tab.setObjectName(u"Path_Tab")
        self.horizontalLayout_2 = QHBoxLayout(self.Path_Tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea_2 = QScrollArea(self.Path_Tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 596, 269))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_12.addWidget(self.lineEdit_2)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_13.addWidget(self.lineEdit_3)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_14.addWidget(self.lineEdit_4)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_15.addWidget(self.lineEdit_5)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_16.addWidget(self.lineEdit_6)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_17.addWidget(self.lineEdit_7)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.Path_Tab, "")
        self.Templates_tab = QWidget()
        self.Templates_tab.setObjectName(u"Templates_tab")
        self.Templates_tab.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_25 = QHBoxLayout(self.Templates_tab)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.scrollArea_4 = QScrollArea(self.Templates_tab)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 596, 269))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_16 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_26.addWidget(self.label_16)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_26.addWidget(self.lineEdit_9)

        self.horizontalLayout_26.setStretch(0, 2)
        self.horizontalLayout_26.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_17 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_27.addWidget(self.label_17)

        self.lineEdit_10 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_27.addWidget(self.lineEdit_10)

        self.horizontalLayout_27.setStretch(0, 2)
        self.horizontalLayout_27.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_18 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_28.addWidget(self.label_18)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_28.addWidget(self.lineEdit_11)

        self.horizontalLayout_28.setStretch(0, 2)
        self.horizontalLayout_28.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_29.addWidget(self.label_19)

        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_29.addWidget(self.lineEdit_12)

        self.horizontalLayout_29.setStretch(0, 2)
        self.horizontalLayout_29.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_20 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_30.addWidget(self.label_20)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_30.addWidget(self.lineEdit_13)

        self.horizontalLayout_30.setStretch(0, 2)
        self.horizontalLayout_30.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_31.addWidget(self.label_21)

        self.lineEdit_14 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_31.addWidget(self.lineEdit_14)

        self.horizontalLayout_31.setStretch(0, 2)
        self.horizontalLayout_31.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_31)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_25.addWidget(self.scrollArea_4)

        self.tabWidget.addTab(self.Templates_tab, "")
        self.Advanced_tab = QWidget()
        self.Advanced_tab.setObjectName(u"Advanced_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.Advanced_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea_3 = QScrollArea(self.Advanced_tab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 596, 269))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_28 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_19.addWidget(self.label_28)

        self.lineEdit_19 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.horizontalLayout_19.addWidget(self.lineEdit_19)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_27 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_20.addWidget(self.label_27)

        self.lineEdit_18 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.horizontalLayout_20.addWidget(self.lineEdit_18)


        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_26 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_21.addWidget(self.label_26)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.horizontalLayout_21.addWidget(self.lineEdit_17)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_25 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_22.addWidget(self.label_25)

        self.lineEdit_16 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.horizontalLayout_22.addWidget(self.lineEdit_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_24 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_23.addWidget(self.label_24)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.horizontalLayout_23.addWidget(self.lineEdit_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_23 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_24.addWidget(self.label_23)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_24.addWidget(self.checkBox)

        self.horizontalLayout_24.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_24)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_3.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.Advanced_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.retranslateUi(Configuration)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Configuration)
    # setupUi

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QCoreApplication.translate("Configuration", u"Configuration", None))
        self.version_text.setText(QCoreApplication.translate("Configuration", u"GAMDL version:", None))
        self.version_label.setText(QCoreApplication.translate("Configuration", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Configuration", u"Download mode", None))
        self.label_2.setText(QCoreApplication.translate("Configuration", u"Remux mode", None))
        self.label_3.setText(QCoreApplication.translate("Configuration", u"Cover format", None))
        self.label_4.setText(QCoreApplication.translate("Configuration", u"Song codec", None))
        self.label_5.setText(QCoreApplication.translate("Configuration", u"Synced lyrics format", None))
        self.label_6.setText(QCoreApplication.translate("Configuration", u"Music video codec", None))
        self.label_7.setText(QCoreApplication.translate("Configuration", u"Post video quality", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Common_tab), QCoreApplication.translate("Configuration", u"Common", None))
        self.label_8.setText(QCoreApplication.translate("Configuration", u"Cookies file", None))
        self.label_9.setText(QCoreApplication.translate("Configuration", u"Output directory", None))
        self.label_10.setText(QCoreApplication.translate("Configuration", u"Temporary directory", None))
        self.label_11.setText(QCoreApplication.translate("Configuration", u"N_m3u8DL-RE binary.", None))
        self.label_12.setText(QCoreApplication.translate("Configuration", u"Mp4decrypt binary", None))
        self.label_13.setText(QCoreApplication.translate("Configuration", u"FFmpeg binary", None))
        self.label_14.setText(QCoreApplication.translate("Configuration", u"MP4Box binary", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Path_Tab), QCoreApplication.translate("Configuration", u"Paths", None))
        self.label_16.setText(QCoreApplication.translate("Configuration", u"Tracks that are part of an album", None))
        self.label_17.setText(QCoreApplication.translate("Configuration", u"Tracks that are part of a compilation album", None))
        self.label_18.setText(QCoreApplication.translate("Configuration", u"Tracks that are part of a single-disc album", None))
        self.label_19.setText(QCoreApplication.translate("Configuration", u"Tracks that are part of a multi-disc album", None))
        self.label_20.setText(QCoreApplication.translate("Configuration", u"Tracks that are not part of an album", None))
        self.label_21.setText(QCoreApplication.translate("Configuration", u"Tracks that are not part of an album", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Templates_tab), QCoreApplication.translate("Configuration", u"Templates", None))
        self.label_28.setText(QCoreApplication.translate("Configuration", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("Configuration", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("Configuration", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("Configuration", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("Configuration", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("Configuration", u"TextLabel", None))
        self.checkBox.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Advanced_tab), QCoreApplication.translate("Configuration", u"Advanced", None))
    # retranslateUi

