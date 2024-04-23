# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        if not MainWindows.objectName():
            MainWindows.setObjectName(u"MainWindows")
        MainWindows.resize(680, 300)
        MainWindows.setMinimumSize(QSize(680, 300))
        self.horizontalLayout_8 = QHBoxLayout(MainWindows)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_2 = QLabel(MainWindows)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.apple_playlistLabel = QLabel(MainWindows)
        self.apple_playlistLabel.setObjectName(u"apple_playlistLabel")

        self.horizontalLayout_3.addWidget(self.apple_playlistLabel)

        self.apple_link = QLineEdit(MainWindows)
        self.apple_link.setObjectName(u"apple_link")
        self.apple_link.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.horizontalLayout_3.addWidget(self.apple_link)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dontskipvideo = QLabel(MainWindows)
        self.dontskipvideo.setObjectName(u"dontskipvideo")

        self.horizontalLayout_4.addWidget(self.dontskipvideo)

        self.dont_skip_video_download = QCheckBox(MainWindows)
        self.dont_skip_video_download.setObjectName(u"dont_skip_video_download")

        self.horizontalLayout_4.addWidget(self.dont_skip_video_download)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(MainWindows)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.save_cover = QCheckBox(MainWindows)
        self.save_cover.setObjectName(u"save_cover")

        self.horizontalLayout_5.addWidget(self.save_cover)

        self.horizontalLayout_5.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(MainWindows)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.overwrite_song = QCheckBox(MainWindows)
        self.overwrite_song.setObjectName(u"overwrite_song")

        self.horizontalLayout_6.addWidget(self.overwrite_song)

        self.horizontalLayout_6.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(MainWindows)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lyrics_type = QComboBox(MainWindows)
        self.lyrics_type.addItem("")
        self.lyrics_type.addItem("")
        self.lyrics_type.addItem("")
        self.lyrics_type.setObjectName(u"lyrics_type")

        self.horizontalLayout_7.addWidget(self.lyrics_type)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.config = QPushButton(MainWindows)
        self.config.setObjectName(u"config")

        self.horizontalLayout_2.addWidget(self.config)

        self.search = QPushButton(MainWindows)
        self.search.setObjectName(u"search")

        self.horizontalLayout_2.addWidget(self.search)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(MainWindows)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.download_list = QPushButton(MainWindows)
        self.download_list.setObjectName(u"download_list")
        self.download_list.setFlat(False)

        self.verticalLayout_2.addWidget(self.download_list)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)


        self.retranslateUi(MainWindows)

        QMetaObject.connectSlotsByName(MainWindows)
    # setupUi

    def retranslateUi(self, MainWindows):
        MainWindows.setWindowTitle(QCoreApplication.translate("MainWindows", u"GAMDL", None))
        self.label_2.setText(QCoreApplication.translate("MainWindows", u"Glomatico's Apple Music Downloader", None))
        self.apple_playlistLabel.setText(QCoreApplication.translate("MainWindows", u"Link:", None))
        self.dontskipvideo.setText(QCoreApplication.translate("MainWindows", u"Don't Skip Music Video In Download", None))
        self.dont_skip_video_download.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindows", u"Save cover as a seprate file", None))
        self.save_cover.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindows", u"Overwrite download songs", None))
        self.overwrite_song.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindows", u"Lyrics", None))
        self.lyrics_type.setItemText(0, QCoreApplication.translate("MainWindows", u"All Lyrics", None))
        self.lyrics_type.setItemText(1, QCoreApplication.translate("MainWindows", u"Synced Lyrics", None))
        self.lyrics_type.setItemText(2, QCoreApplication.translate("MainWindows", u"No Lyrics", None))

        self.config.setText(QCoreApplication.translate("MainWindows", u"Config", None))
        self.search.setText(QCoreApplication.translate("MainWindows", u"Search", None))
        self.download_list.setText(QCoreApplication.translate("MainWindows", u"Download", None))
    # retranslateUi

