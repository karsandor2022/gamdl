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
        self.Name_and_Settings = QVBoxLayout()
        self.Name_and_Settings.setObjectName(u"Name_and_Settings")
        self.Name_and_Settings.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.name = QLabel(MainWindows)
        self.name.setObjectName(u"name")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.name.setFont(font)

        self.Name_and_Settings.addWidget(self.name)

        self.apple_link = QHBoxLayout()
        self.apple_link.setObjectName(u"apple_link")
        self.apple_playlistLabel = QLabel(MainWindows)
        self.apple_playlistLabel.setObjectName(u"apple_playlistLabel")

        self.apple_link.addWidget(self.apple_playlistLabel)

        self.apple_link_text = QLineEdit(MainWindows)
        self.apple_link_text.setObjectName(u"apple_link_text")
        self.apple_link_text.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.apple_link.addWidget(self.apple_link_text)


        self.Name_and_Settings.addLayout(self.apple_link)

        self.dont_skip_video = QHBoxLayout()
        self.dont_skip_video.setObjectName(u"dont_skip_video")
        self.dont_skip_video_checkbox = QLabel(MainWindows)
        self.dont_skip_video_checkbox.setObjectName(u"dont_skip_video_checkbox")

        self.dont_skip_video.addWidget(self.dont_skip_video_checkbox)

        self.dont_skip_video_download = QCheckBox(MainWindows)
        self.dont_skip_video_download.setObjectName(u"dont_skip_video_download")

        self.dont_skip_video.addWidget(self.dont_skip_video_download)

        self.dont_skip_video.setStretch(0, 1)

        self.Name_and_Settings.addLayout(self.dont_skip_video)

        self.save_cover = QHBoxLayout()
        self.save_cover.setObjectName(u"save_cover")
        self.save_cover_checkbox = QLabel(MainWindows)
        self.save_cover_checkbox.setObjectName(u"save_cover_checkbox")

        self.save_cover.addWidget(self.save_cover_checkbox)

        self.save_cover_label = QCheckBox(MainWindows)
        self.save_cover_label.setObjectName(u"save_cover_label")

        self.save_cover.addWidget(self.save_cover_label)

        self.save_cover.setStretch(0, 1)

        self.Name_and_Settings.addLayout(self.save_cover)

        self.overwrite = QHBoxLayout()
        self.overwrite.setObjectName(u"overwrite")
        self.overwrite_label = QLabel(MainWindows)
        self.overwrite_label.setObjectName(u"overwrite_label")

        self.overwrite.addWidget(self.overwrite_label)

        self.overwrite_song_checkbox = QCheckBox(MainWindows)
        self.overwrite_song_checkbox.setObjectName(u"overwrite_song_checkbox")

        self.overwrite.addWidget(self.overwrite_song_checkbox)

        self.overwrite.setStretch(0, 1)

        self.Name_and_Settings.addLayout(self.overwrite)

        self.lyrics = QHBoxLayout()
        self.lyrics.setObjectName(u"lyrics")
        self.lyrics_label = QLabel(MainWindows)
        self.lyrics_label.setObjectName(u"lyrics_label")

        self.lyrics.addWidget(self.lyrics_label)

        self.lyrics_type = QComboBox(MainWindows)
        self.lyrics_type.addItem("")
        self.lyrics_type.addItem("")
        self.lyrics_type.addItem("")
        self.lyrics_type.setObjectName(u"lyrics_type")

        self.lyrics.addWidget(self.lyrics_type)


        self.Name_and_Settings.addLayout(self.lyrics)

        self.config_and_search = QHBoxLayout()
        self.config_and_search.setObjectName(u"config_and_search")
        self.config_button = QPushButton(MainWindows)
        self.config_button.setObjectName(u"config_button")

        self.config_and_search.addWidget(self.config_button)

        self.search_button = QPushButton(MainWindows)
        self.search_button.setObjectName(u"search_button")

        self.config_and_search.addWidget(self.search_button)


        self.Name_and_Settings.addLayout(self.config_and_search)

        self.Name_and_Settings.setStretch(0, 1)
        self.Name_and_Settings.setStretch(1, 1)
        self.Name_and_Settings.setStretch(2, 1)
        self.Name_and_Settings.setStretch(3, 1)
        self.Name_and_Settings.setStretch(4, 1)
        self.Name_and_Settings.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.Name_and_Settings)

        self.Download = QVBoxLayout()
        self.Download.setObjectName(u"Download")
        self.download_list = QListWidget(MainWindows)
        self.download_list.setObjectName(u"download_list")

        self.Download.addWidget(self.download_list)

        self.download_list_button = QPushButton(MainWindows)
        self.download_list_button.setObjectName(u"download_list_button")
        self.download_list_button.setFlat(False)

        self.Download.addWidget(self.download_list_button)


        self.horizontalLayout.addLayout(self.Download)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)


        self.retranslateUi(MainWindows)

        QMetaObject.connectSlotsByName(MainWindows)
    # setupUi

    def retranslateUi(self, MainWindows):
        MainWindows.setWindowTitle(QCoreApplication.translate("MainWindows", u"GAMDL", None))
        self.name.setText(QCoreApplication.translate("MainWindows", u"Glomatico's Apple Music Downloader", None))
        self.apple_playlistLabel.setText(QCoreApplication.translate("MainWindows", u"Link:", None))
        self.dont_skip_video_checkbox.setText(QCoreApplication.translate("MainWindows", u"Don't Skip Music Video In Download", None))
        self.dont_skip_video_download.setText("")
        self.save_cover_checkbox.setText(QCoreApplication.translate("MainWindows", u"Save cover as a seprate file", None))
        self.save_cover_label.setText("")
        self.overwrite_label.setText(QCoreApplication.translate("MainWindows", u"Overwrite download songs", None))
        self.overwrite_song_checkbox.setText("")
        self.lyrics_label.setText(QCoreApplication.translate("MainWindows", u"Lyrics", None))
        self.lyrics_type.setItemText(0, QCoreApplication.translate("MainWindows", u"All Lyrics", None))
        self.lyrics_type.setItemText(1, QCoreApplication.translate("MainWindows", u"Synced Lyrics", None))
        self.lyrics_type.setItemText(2, QCoreApplication.translate("MainWindows", u"No Lyrics", None))

        self.config_button.setText(QCoreApplication.translate("MainWindows", u"Config", None))
        self.search_button.setText(QCoreApplication.translate("MainWindows", u"Search", None))
        self.download_list_button.setText(QCoreApplication.translate("MainWindows", u"Download", None))
    # retranslateUi

