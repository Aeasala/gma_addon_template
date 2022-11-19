# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1133, 847)
        self.actionTools_show_debug = QAction(MainWindow)
        self.actionTools_show_debug.setObjectName(u"actionTools_show_debug")
        self.actionFile_addon_root_folder = QAction(MainWindow)
        self.actionFile_addon_root_folder.setObjectName(u"actionFile_addon_root_folder")
        self.actionFile_gma_select = QAction(MainWindow)
        self.actionFile_gma_select.setObjectName(u"actionFile_gma_select")
        self.actionFile_icon_select = QAction(MainWindow)
        self.actionFile_icon_select.setObjectName(u"actionFile_icon_select")
        self.actionHelp_symlinks = QAction(MainWindow)
        self.actionHelp_symlinks.setObjectName(u"actionHelp_symlinks")
        self.actionHelp_updating = QAction(MainWindow)
        self.actionHelp_updating.setObjectName(u"actionHelp_updating")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(150, 380, 381, 171))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.workshop_update_existing_button = QPushButton(self.gridLayoutWidget)
        self.workshop_update_existing_button.setObjectName(u"workshop_update_existing_button")

        self.gridLayout.addWidget(self.workshop_update_existing_button, 0, 0, 1, 1)

        self.gma_publish_button = QPushButton(self.gridLayoutWidget)
        self.gma_publish_button.setObjectName(u"gma_publish_button")

        self.gridLayout.addWidget(self.gma_publish_button, 1, 0, 1, 1)

        self.gma_generate_button = QPushButton(self.gridLayoutWidget)
        self.gma_generate_button.setObjectName(u"gma_generate_button")

        self.gridLayout.addWidget(self.gma_generate_button, 2, 0, 1, 1)

        self.create_symlink_button = QPushButton(self.gridLayoutWidget)
        self.create_symlink_button.setObjectName(u"create_symlink_button")

        self.gridLayout.addWidget(self.create_symlink_button, 3, 0, 1, 1)

        self.addon_path_line_edit = QLineEdit(self.centralwidget)
        self.addon_path_line_edit.setObjectName(u"addon_path_line_edit")
        self.addon_path_line_edit.setGeometry(QRect(220, 150, 251, 24))
        self.addon_path_label = QLabel(self.centralwidget)
        self.addon_path_label.setObjectName(u"addon_path_label")
        self.addon_path_label.setGeometry(QRect(40, 150, 171, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addon_path_label.sizePolicy().hasHeightForWidth())
        self.addon_path_label.setSizePolicy(sizePolicy)
        self.addon_path_label.setLayoutDirection(Qt.LeftToRight)
        self.addon_path_label.setFrameShape(QFrame.NoFrame)
        self.addon_path_label.setFrameShadow(QFrame.Plain)
        self.addon_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.symlink_path_label = QLabel(self.centralwidget)
        self.symlink_path_label.setObjectName(u"symlink_path_label")
        self.symlink_path_label.setGeometry(QRect(40, 230, 171, 21))
        sizePolicy.setHeightForWidth(self.symlink_path_label.sizePolicy().hasHeightForWidth())
        self.symlink_path_label.setSizePolicy(sizePolicy)
        self.symlink_path_label.setLayoutDirection(Qt.LeftToRight)
        self.symlink_path_label.setFrameShape(QFrame.NoFrame)
        self.symlink_path_label.setFrameShadow(QFrame.Plain)
        self.symlink_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.symlink_path_line_edit = QLineEdit(self.centralwidget)
        self.symlink_path_line_edit.setObjectName(u"symlink_path_line_edit")
        self.symlink_path_line_edit.setGeometry(QRect(220, 230, 251, 24))
        self.gma_path_label = QLabel(self.centralwidget)
        self.gma_path_label.setObjectName(u"gma_path_label")
        self.gma_path_label.setGeometry(QRect(40, 190, 171, 21))
        sizePolicy.setHeightForWidth(self.gma_path_label.sizePolicy().hasHeightForWidth())
        self.gma_path_label.setSizePolicy(sizePolicy)
        self.gma_path_label.setLayoutDirection(Qt.LeftToRight)
        self.gma_path_label.setFrameShape(QFrame.NoFrame)
        self.gma_path_label.setFrameShadow(QFrame.Plain)
        self.gma_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gma_path_line_edit = QLineEdit(self.centralwidget)
        self.gma_path_line_edit.setObjectName(u"gma_path_line_edit")
        self.gma_path_line_edit.setGeometry(QRect(220, 190, 251, 24))
        self.workshop_icon = QLabel(self.centralwidget)
        self.workshop_icon.setObjectName(u"workshop_icon")
        self.workshop_icon.setGeometry(QRect(530, 30, 220, 220))
        self.workshop_icon.setFrameShape(QFrame.Box)
        self.workshop_icon.setFrameShadow(QFrame.Raised)
        self.workshop_icon.setLineWidth(1)
        self.workshop_icon.setMidLineWidth(0)
        self.workshop_icon.setPixmap(QPixmap(u"../icon/icon.jpg"))
        self.workshop_icon.setScaledContents(True)
        self.workshop_icon.setMargin(5)
        self.tools_group_box = QGroupBox(self.centralwidget)
        self.tools_group_box.setObjectName(u"tools_group_box")
        self.tools_group_box.setGeometry(QRect(680, 300, 341, 231))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.tools_group_box.setFont(font)
        self.tools_group_box.setFlat(False)
        self.select_icon_button = QPushButton(self.centralwidget)
        self.select_icon_button.setObjectName(u"select_icon_button")
        self.select_icon_button.setGeometry(QRect(580, 260, 121, 24))
        self.debugging_group_box = QGroupBox(self.centralwidget)
        self.debugging_group_box.setObjectName(u"debugging_group_box")
        self.debugging_group_box.setGeometry(QRect(660, 570, 341, 231))
        self.debugging_group_box.setFont(font)
        self.debugging_group_box.setFlat(False)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(90, 610, 256, 192))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1133, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionFile_addon_root_folder)
        self.menuFile.addAction(self.actionFile_gma_select)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFile_icon_select)
        self.menuHelp.addAction(self.actionHelp_symlinks)
        self.menuHelp.addAction(self.actionHelp_updating)
        self.menuTools.addAction(self.actionTools_show_debug)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Garry's Mod GMA Toolkit", None))
        self.actionTools_show_debug.setText(QCoreApplication.translate("MainWindow", u"Show Debug Console", None))
        self.actionFile_addon_root_folder.setText(QCoreApplication.translate("MainWindow", u"Select a Different Addon Root Folder", None))
        self.actionFile_gma_select.setText(QCoreApplication.translate("MainWindow", u"Select a Different GMA to Publish", None))
        self.actionFile_icon_select.setText(QCoreApplication.translate("MainWindow", u"Select a Different Icon", None))
        self.actionHelp_symlinks.setText(QCoreApplication.translate("MainWindow", u"Symlinks?  Huh?  Why?", None))
        self.actionHelp_updating.setText(QCoreApplication.translate("MainWindow", u"How do I update my published addon?", None))
        self.workshop_update_existing_button.setText(QCoreApplication.translate("MainWindow", u"Update Existing GMA on Steam Workshop", None))
        self.gma_publish_button.setText(QCoreApplication.translate("MainWindow", u"Publish GMA to Steam Workshop", None))
        self.gma_generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate GMA!", None))
        self.create_symlink_button.setText(QCoreApplication.translate("MainWindow", u"Create a Symlink to your Addon", None))
        self.addon_path_line_edit.setText(QCoreApplication.translate("MainWindow", u"./your_addon_here", None))
        self.addon_path_label.setText(QCoreApplication.translate("MainWindow", u"Addon Path", None))
        self.symlink_path_label.setText(QCoreApplication.translate("MainWindow", u"Symlink gens found in", None))
        self.symlink_path_line_edit.setText(QCoreApplication.translate("MainWindow", u"./symlinks", None))
        self.gma_path_label.setText(QCoreApplication.translate("MainWindow", u"Selected GMA", None))
        self.gma_path_line_edit.setText(QCoreApplication.translate("MainWindow", u"./your_addon_here", None))
        self.workshop_icon.setText("")
        self.tools_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.select_icon_button.setText(QCoreApplication.translate("MainWindow", u"Select an Icon", None))
        self.debugging_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Debugging Output", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Addon Path", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"GMA", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Icon Path", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Symlink Path", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

