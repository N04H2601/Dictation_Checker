# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maquette_accueil.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 628)
        Form.setMinimumSize(QtCore.QSize(970, 628))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 4, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setToolTip("")
        self.tab.setObjectName("tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.plain_correction_dictee = QtWidgets.QPlainTextEdit(self.tab)
        self.plain_correction_dictee.setEnabled(True)
        self.plain_correction_dictee.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plain_correction_dictee.setReadOnly(True)
        self.plain_correction_dictee.setObjectName("plain_correction_dictee")
        self.gridLayout_11.addWidget(self.plain_correction_dictee, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setToolTip("")
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.plain_corrige_dictee = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plain_corrige_dictee.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plain_corrige_dictee.setReadOnly(True)
        self.plain_corrige_dictee.setObjectName("plain_corrige_dictee")
        self.gridLayout_12.addWidget(self.plain_corrige_dictee, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 10, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plain_fautes = QtWidgets.QPlainTextEdit(Form)
        self.plain_fautes.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.plain_fautes.setFont(font)
        self.plain_fautes.setStyleSheet("font: 75 10pt \"Calibri\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plain_fautes.setReadOnly(True)
        self.plain_fautes.setObjectName("plain_fautes")
        self.gridLayout_2.addWidget(self.plain_fautes, 1, 0, 1, 1)
        self.label_fautes = QtWidgets.QLabel(Form)
        self.label_fautes.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_fautes.setStyleSheet("font: 75 10pt \"Arial\";")
        self.label_fautes.setObjectName("label_fautes")
        self.gridLayout_2.addWidget(self.label_fautes, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 11, 1, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_commentaire_apparait = QtWidgets.QLabel(Form)
        self.label_commentaire_apparait.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_commentaire_apparait.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_commentaire_apparait.setText("")
        self.label_commentaire_apparait.setObjectName("label_commentaire_apparait")
        self.gridLayout_14.addWidget(self.label_commentaire_apparait, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_14, 5, 1, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pb_next_dictee = QtWidgets.QPushButton(Form)
        self.pb_next_dictee.setMinimumSize(QtCore.QSize(80, 36))
        self.pb_next_dictee.setMaximumSize(QtCore.QSize(80, 45))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_next_dictee.setIcon(icon)
        self.pb_next_dictee.setIconSize(QtCore.QSize(60, 30))
        self.pb_next_dictee.setObjectName("pb_next_dictee")
        self.gridLayout_10.addWidget(self.pb_next_dictee, 0, 2, 1, 1)
        self.pb_prev_dictee = QtWidgets.QPushButton(Form)
        self.pb_prev_dictee.setMinimumSize(QtCore.QSize(80, 36))
        self.pb_prev_dictee.setMaximumSize(QtCore.QSize(80, 45))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pb_prev_dictee.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_prev_dictee.setIcon(icon1)
        self.pb_prev_dictee.setIconSize(QtCore.QSize(60, 30))
        self.pb_prev_dictee.setObjectName("pb_prev_dictee")
        self.gridLayout_10.addWidget(self.pb_prev_dictee, 0, 0, 1, 1)
        self.pb_play_pause = QtWidgets.QPushButton(Form)
        self.pb_play_pause.setMinimumSize(QtCore.QSize(75, 50))
        self.pb_play_pause.setMaximumSize(QtCore.QSize(75, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_play_pause.setFont(font)
        self.pb_play_pause.setMouseTracking(False)
        self.pb_play_pause.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pb_play_pause.setAcceptDrops(False)
        self.pb_play_pause.setAutoFillBackground(False)
        self.pb_play_pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_play_pause.setIcon(icon2)
        self.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
        self.pb_play_pause.setCheckable(False)
        self.pb_play_pause.setAutoDefault(False)
        self.pb_play_pause.setDefault(False)
        self.pb_play_pause.setFlat(False)
        self.pb_play_pause.setObjectName("pb_play_pause")
        self.gridLayout_10.addWidget(self.pb_play_pause, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_10, 3, 0, 1, 1)
        self.label_note_apparait = QtWidgets.QLabel(Form)
        self.label_note_apparait.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_note_apparait.setText("")
        self.label_note_apparait.setObjectName("label_note_apparait")
        self.gridLayout_3.addWidget(self.label_note_apparait, 2, 1, 1, 1)
        self.label_nom_dictee = QtWidgets.QLabel(Form)
        self.label_nom_dictee.setStyleSheet("font: 63 10pt \"Arial\";")
        self.label_nom_dictee.setObjectName("label_nom_dictee")
        self.gridLayout_3.addWidget(self.label_nom_dictee, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pb_stop = QtWidgets.QPushButton(Form)
        self.pb_stop.setMinimumSize(QtCore.QSize(75, 50))
        self.pb_stop.setMaximumSize(QtCore.QSize(75, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_stop.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_stop.setIcon(icon3)
        self.pb_stop.setIconSize(QtCore.QSize(60, 25))
        self.pb_stop.setObjectName("pb_stop")
        self.gridLayout_4.addWidget(self.pb_stop, 0, 4, 1, 1)
        self.pb_rejouer = QtWidgets.QPushButton(Form)
        self.pb_rejouer.setMinimumSize(QtCore.QSize(75, 50))
        self.pb_rejouer.setMaximumSize(QtCore.QSize(75, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pb_rejouer.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("replay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_rejouer.setIcon(icon4)
        self.pb_rejouer.setIconSize(QtCore.QSize(75, 37))
        self.pb_rejouer.setObjectName("pb_rejouer")
        self.gridLayout_4.addWidget(self.pb_rejouer, 0, 2, 1, 1)
        self.pb_rewind = QtWidgets.QPushButton(Form)
        self.pb_rewind.setMinimumSize(QtCore.QSize(75, 50))
        self.pb_rewind.setMaximumSize(QtCore.QSize(75, 50))
        self.pb_rewind.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("rewind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_rewind.setIcon(icon5)
        self.pb_rewind.setIconSize(QtCore.QSize(75, 45))
        self.pb_rewind.setObjectName("pb_rewind")
        self.gridLayout_4.addWidget(self.pb_rewind, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 5, 0, 1, 1)
        self.label_message_erreur_ou_bravo = QtWidgets.QLabel(Form)
        self.label_message_erreur_ou_bravo.setStyleSheet("font: 10pt \"Arial\";")
        self.label_message_erreur_ou_bravo.setObjectName("label_message_erreur_ou_bravo")
        self.gridLayout_3.addWidget(self.label_message_erreur_ou_bravo, 3, 1, 1, 1)
        self.label_note = QtWidgets.QLabel(Form)
        self.label_note.setStyleSheet("font: 75 10pt \"Arial\";")
        self.label_note.setObjectName("label_note")
        self.gridLayout_3.addWidget(self.label_note, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.plain_text_dictee = QtWidgets.QPlainTextEdit(Form)
        self.plain_text_dictee.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plain_text_dictee.setPlaceholderText("")
        self.plain_text_dictee.setObjectName("plain_text_dictee")
        self.gridLayout_3.addWidget(self.plain_text_dictee, 10, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pb_valider_dictee = QtWidgets.QPushButton(Form)
        self.pb_valider_dictee.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pb_valider_dictee.setFont(font)
        self.pb_valider_dictee.setStyleSheet("font: 75 10pt \"Arial\";")
        self.pb_valider_dictee.setObjectName("pb_valider_dictee")
        self.gridLayout_8.addWidget(self.pb_valider_dictee, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_8, 12, 0, 1, 1)
        self.pb_clear = QtWidgets.QPushButton(Form)
        self.pb_clear.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pb_clear.setFont(font)
        self.pb_clear.setStyleSheet("font: 75 10pt \"Arial\";")
        self.pb_clear.setObjectName("pb_clear")
        self.gridLayout_3.addWidget(self.pb_clear, 12, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_nom_dictee_apparait = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_nom_dictee_apparait.setFont(font)
        self.label_nom_dictee_apparait.setStyleSheet("color: rgb(0, 0, 200);")
        self.label_nom_dictee_apparait.setText("")
        self.label_nom_dictee_apparait.setObjectName("label_nom_dictee_apparait")
        self.gridLayout_7.addWidget(self.label_nom_dictee_apparait, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 2, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pb_accent2 = QtWidgets.QPushButton(Form)
        self.pb_accent2.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_accent2.setMaximumSize(QtCore.QSize(40, 30))
        self.pb_accent2.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.pb_accent2.setObjectName("pb_accent2")
        self.gridLayout_9.addWidget(self.pb_accent2, 1, 1, 1, 1)
        self.pb_accent4 = QtWidgets.QPushButton(Form)
        self.pb_accent4.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_accent4.setMaximumSize(QtCore.QSize(40, 30))
        self.pb_accent4.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.pb_accent4.setObjectName("pb_accent4")
        self.gridLayout_9.addWidget(self.pb_accent4, 1, 3, 1, 1)
        self.pb_accent1 = QtWidgets.QPushButton(Form)
        self.pb_accent1.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_accent1.setMaximumSize(QtCore.QSize(40, 30))
        self.pb_accent1.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.pb_accent1.setObjectName("pb_accent1")
        self.gridLayout_9.addWidget(self.pb_accent1, 1, 0, 1, 1)
        self.pb_accent3 = QtWidgets.QPushButton(Form)
        self.pb_accent3.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_accent3.setMaximumSize(QtCore.QSize(40, 30))
        self.pb_accent3.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.pb_accent3.setObjectName("pb_accent3")
        self.gridLayout_9.addWidget(self.pb_accent3, 1, 2, 1, 1)
        self.pb_ponctuation1 = QtWidgets.QPushButton(Form)
        self.pb_ponctuation1.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_ponctuation1.setMaximumSize(QtCore.QSize(40, 30))
        self.pb_ponctuation1.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.pb_ponctuation1.setObjectName("pb_ponctuation1")
        self.gridLayout_9.addWidget(self.pb_ponctuation1, 1, 5, 1, 1)
        self.pb_ponctuation2 = QtWidgets.QPushButton(Form)
        self.pb_ponctuation2.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_ponctuation2.setMaximumSize(QtCore.QSize(40, 30))
        self.pb_ponctuation2.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.pb_ponctuation2.setObjectName("pb_ponctuation2")
        self.gridLayout_9.addWidget(self.pb_ponctuation2, 1, 6, 1, 1)
        self.pb_accent5 = QtWidgets.QPushButton(Form)
        self.pb_accent5.setMinimumSize(QtCore.QSize(40, 30))
        self.pb_accent5.setMaximumSize(QtCore.QSize(40, 30))
        self.pb_accent5.setObjectName("pb_accent5")
        self.gridLayout_9.addWidget(self.pb_accent5, 1, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_9, 11, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.pb_info = QtWidgets.QPushButton(Form)
        self.pb_info.setStyleSheet("")
        self.pb_info.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("round_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_info.setIcon(icon6)
        self.pb_info.setIconSize(QtCore.QSize(18, 18))
        self.pb_info.setAutoDefault(False)
        self.pb_info.setDefault(False)
        self.pb_info.setFlat(True)
        self.pb_info.setObjectName("pb_info")
        self.gridLayout_13.addWidget(self.pb_info, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_13, 7, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 3, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.tabw_langues = QtWidgets.QTabWidget(Form)
        self.tabw_langues.setMinimumSize(QtCore.QSize(200, 0))
        self.tabw_langues.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.tabw_langues.setFont(font)
        self.tabw_langues.setStyleSheet("background-color: rgb(204, 204, 204);\n"
"font: 63 10pt \"Open Sans Semibold\";")
        self.tabw_langues.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabw_langues.setUsesScrollButtons(True)
        self.tabw_langues.setDocumentMode(False)
        self.tabw_langues.setTabBarAutoHide(False)
        self.tabw_langues.setObjectName("tabw_langues")
        self.intercalaire_francais = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.intercalaire_francais.setFont(font)
        self.intercalaire_francais.setObjectName("intercalaire_francais")
        self.tool_button_francais_facile = QtWidgets.QToolButton(self.intercalaire_francais)
        self.tool_button_francais_facile.setGeometry(QtCore.QRect(20, 20, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tool_button_francais_facile.setFont(font)
        self.tool_button_francais_facile.setMouseTracking(False)
        self.tool_button_francais_facile.setAutoFillBackground(False)
        self.tool_button_francais_facile.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"border-color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 255, 0);")
        self.tool_button_francais_facile.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.tool_button_francais_facile.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.tool_button_francais_facile.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tool_button_francais_facile.setAutoRaise(False)
        self.tool_button_francais_facile.setArrowType(QtCore.Qt.NoArrow)
        self.tool_button_francais_facile.setObjectName("tool_button_francais_facile")
        self.tool_button_francais_moyen = QtWidgets.QToolButton(self.intercalaire_francais)
        self.tool_button_francais_moyen.setGeometry(QtCore.QRect(20, 120, 171, 81))
        self.tool_button_francais_moyen.setMouseTracking(False)
        self.tool_button_francais_moyen.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(255, 255, 0);\n"
"font: 14pt \"Comic Sans MS\";")
        self.tool_button_francais_moyen.setObjectName("tool_button_francais_moyen")
        self.tool_button_francais_difficile = QtWidgets.QToolButton(self.intercalaire_francais)
        self.tool_button_francais_difficile.setGeometry(QtCore.QRect(20, 220, 171, 81))
        self.tool_button_francais_difficile.setMouseTracking(False)
        self.tool_button_francais_difficile.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"border-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.tool_button_francais_difficile.setObjectName("tool_button_francais_difficile")
        self.tool_button_francais_moyen.raise_()
        self.tool_button_francais_difficile.raise_()
        self.tool_button_francais_facile.raise_()
        self.tabw_langues.addTab(self.intercalaire_francais, "")
        self.intercalaire_anglais = QtWidgets.QWidget()
        self.intercalaire_anglais.setObjectName("intercalaire_anglais")
        self.tool_button_anglais_facile = QtWidgets.QToolButton(self.intercalaire_anglais)
        self.tool_button_anglais_facile.setGeometry(QtCore.QRect(20, 20, 171, 81))
        self.tool_button_anglais_facile.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 170, 0);\n"
"font: 14pt \"Comic Sans MS\";")
        self.tool_button_anglais_facile.setObjectName("tool_button_anglais_facile")
        self.tool_button_anglais_moyen = QtWidgets.QToolButton(self.intercalaire_anglais)
        self.tool_button_anglais_moyen.setGeometry(QtCore.QRect(20, 120, 171, 81))
        self.tool_button_anglais_moyen.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(255, 255, 0);\n"
"font: 14pt \"Comic Sans MS\";")
        self.tool_button_anglais_moyen.setObjectName("tool_button_anglais_moyen")
        self.tool_button_anglais_difficile = QtWidgets.QToolButton(self.intercalaire_anglais)
        self.tool_button_anglais_difficile.setGeometry(QtCore.QRect(20, 220, 171, 81))
        self.tool_button_anglais_difficile.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-color: rgb(255, 0, 0);\n"
"font: 14pt \"Comic Sans MS\";")
        self.tool_button_anglais_difficile.setObjectName("tool_button_anglais_difficile")
        self.tabw_langues.addTab(self.intercalaire_anglais, "")
        self.intercalaire_espagnol = QtWidgets.QWidget()
        self.intercalaire_espagnol.setObjectName("intercalaire_espagnol")
        self.tool_button_espagnol_facile = QtWidgets.QToolButton(self.intercalaire_espagnol)
        self.tool_button_espagnol_facile.setGeometry(QtCore.QRect(20, 20, 171, 81))
        self.tool_button_espagnol_facile.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 170, 0);\n"
"font: 14pt \"Comic Sans MS\";")
        self.tool_button_espagnol_facile.setObjectName("tool_button_espagnol_facile")
        self.tool_button_espagnol_moyen = QtWidgets.QToolButton(self.intercalaire_espagnol)
        self.tool_button_espagnol_moyen.setGeometry(QtCore.QRect(20, 120, 171, 81))
        self.tool_button_espagnol_moyen.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(255, 255, 0);\n"
"font: 14pt \"Comic Sans MS\";")
        self.tool_button_espagnol_moyen.setObjectName("tool_button_espagnol_moyen")
        self.tool_button_espagnol_difficile = QtWidgets.QToolButton(self.intercalaire_espagnol)
        self.tool_button_espagnol_difficile.setGeometry(QtCore.QRect(20, 220, 171, 81))
        self.tool_button_espagnol_difficile.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-color: rgb(255, 0, 0);\n"
"font: 14pt \"Comic Sans MS\";")
        self.tool_button_espagnol_difficile.setObjectName("tool_button_espagnol_difficile")
        self.tabw_langues.addTab(self.intercalaire_espagnol, "")
        self.gridLayout_17.addWidget(self.tabw_langues, 0, 0, 1, 1)
        self.pb_evaluation = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pb_evaluation.setFont(font)
        self.pb_evaluation.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(0, 85, 255);")
        self.pb_evaluation.setObjectName("pb_evaluation")
        self.gridLayout_17.addWidget(self.pb_evaluation, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_titre = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_titre.setFont(font)
        self.label_titre.setStyleSheet("text-decoration: underline;\n"
"text-decoration: underline;\n"
"font: 20pt \"Comic Sans MS\";\n"
"text-decoration: underline;\n"
"color: rgb(0, 0, 214);\n"
"background-color: rgb(255, 255, 255);")
        self.label_titre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titre.setObjectName("label_titre")
        self.gridLayout_5.addWidget(self.label_titre, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabw_langues.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Correction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Corrig??"))
        self.label_fautes.setText(_translate("Form", "Fautes :"))
        self.pb_next_dictee.setToolTip(_translate("Form", "Dict??e suivante"))
        self.pb_prev_dictee.setToolTip(_translate("Form", "Dict??e pr??c??dente"))
        self.pb_play_pause.setToolTip(_translate("Form", "Pause / Reprendre la lecture"))
        self.pb_play_pause.setShortcut(_translate("Form", "Space"))
        self.label_nom_dictee.setText(_translate("Form", "Nom de la dict??e :"))
        self.pb_stop.setToolTip(_translate("Form", "Arr??ter l\'audio"))
        self.pb_rejouer.setToolTip(_translate("Form", "Rejouer l\'audio"))
        self.pb_rewind.setToolTip(_translate("Form", "Revenir en arri??re (10s)"))
        self.label_message_erreur_ou_bravo.setText(_translate("Form", "Commentaire :"))
        self.label_note.setText(_translate("Form", "Note : "))
        self.pb_valider_dictee.setToolTip(_translate("Form", "Corriger la dict??e rentr??e"))
        self.pb_valider_dictee.setText(_translate("Form", "Corriger ma dict??e"))
        self.pb_clear.setToolTip(_translate("Form", "Tout effacer et copier la dict??e rentr??e"))
        self.pb_clear.setText(_translate("Form", "Tout effacer et faire une autre dict??e"))
        self.pb_accent2.setText(_translate("Form", "??"))
        self.pb_accent4.setText(_translate("Form", "??"))
        self.pb_accent1.setText(_translate("Form", "??"))
        self.pb_accent3.setText(_translate("Form", "??"))
        self.pb_ponctuation1.setText(_translate("Form", "??"))
        self.pb_ponctuation2.setText(_translate("Form", "??"))
        self.pb_accent5.setText(_translate("Form", "??"))
        self.pb_info.setToolTip(_translate("Form", "Clique ici pour voir les r??gles de ponctuation"))
        self.intercalaire_francais.setToolTip(_translate("Form", "Dict??es en fran??ais"))
        self.tool_button_francais_facile.setToolTip(_translate("Form", "Fran??ais / Facile"))
        self.tool_button_francais_facile.setText(_translate("Form", "Niveau facile"))
        self.tool_button_francais_moyen.setToolTip(_translate("Form", "Fran??ais / Moyen"))
        self.tool_button_francais_moyen.setText(_translate("Form", "Niveau moyen "))
        self.tool_button_francais_difficile.setToolTip(_translate("Form", "Fran??ais / Difficile"))
        self.tool_button_francais_difficile.setText(_translate("Form", "Niveau difficile"))
        self.tabw_langues.setTabText(self.tabw_langues.indexOf(self.intercalaire_francais), _translate("Form", "Fran??ais"))
        self.intercalaire_anglais.setToolTip(_translate("Form", "Dict??es en anglais"))
        self.tool_button_anglais_facile.setToolTip(_translate("Form", "Anglais / Facile"))
        self.tool_button_anglais_facile.setText(_translate("Form", "Easy level"))
        self.tool_button_anglais_moyen.setToolTip(_translate("Form", "Anglais / Moyen"))
        self.tool_button_anglais_moyen.setText(_translate("Form", "Medium level"))
        self.tool_button_anglais_difficile.setToolTip(_translate("Form", "Anglais / Difficile"))
        self.tool_button_anglais_difficile.setText(_translate("Form", "Hard level"))
        self.tabw_langues.setTabText(self.tabw_langues.indexOf(self.intercalaire_anglais), _translate("Form", "English"))
        self.intercalaire_espagnol.setToolTip(_translate("Form", "Dict??es en espagnol"))
        self.tool_button_espagnol_facile.setToolTip(_translate("Form", "Espagnol / Facile"))
        self.tool_button_espagnol_facile.setText(_translate("Form", "Nivel f??cil"))
        self.tool_button_espagnol_moyen.setToolTip(_translate("Form", "Espagnol / Moyen"))
        self.tool_button_espagnol_moyen.setText(_translate("Form", "Nivel medio"))
        self.tool_button_espagnol_difficile.setToolTip(_translate("Form", "Espagnol / Difficile"))
        self.tool_button_espagnol_difficile.setText(_translate("Form", "Nivel dificil"))
        self.tabw_langues.setTabText(self.tabw_langues.indexOf(self.intercalaire_espagnol), _translate("Form", "Espa??ol"))
        self.pb_evaluation.setText(_translate("Form", "Aller au mode ??valuation"))
        self.label_titre.setText(_translate("Form", " Entra??nement ?? la dict??e "))
