# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maquette_accueil.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 628)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.pb_quitter = QtWidgets.QPushButton(Form)
        self.pb_quitter.setObjectName("pb_quitter")
        self.gridLayout_2.addWidget(self.pb_quitter, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 3, 1, 1)
        self.tabw_intercalaires = QtWidgets.QTabWidget(Form)
        self.tabw_intercalaires.setMaximumSize(QtCore.QSize(250, 16777215))
        self.tabw_intercalaires.setObjectName("tabw_intercalaires")
        self.intercalaire_francais = QtWidgets.QWidget()
        self.intercalaire_francais.setObjectName("intercalaire_francais")
        self.tool_button_francais_facile = QtWidgets.QToolButton(self.intercalaire_francais)
        self.tool_button_francais_facile.setGeometry(QtCore.QRect(20, 21, 171, 81))
        self.tool_button_francais_facile.setStyleSheet("nfont: 14pt \"Times New Roman\";\n"
"background-color: rgb(170, 255, 0);\n"
"font: 8pt \"Times New Roman\";\n"
"font: 14pt ;")
        self.tool_button_francais_facile.setObjectName("tool_button_francais_facile")
        self.tool_button_francais_moyen = QtWidgets.QToolButton(self.intercalaire_francais)
        self.tool_button_francais_moyen.setGeometry(QtCore.QRect(20, 120, 171, 81))
        self.tool_button_francais_moyen.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 14pt \"Times New Roman\";\n"
"font: 8pt \"Times New Roman\";\n"
"font: 14pt ;")
        self.tool_button_francais_moyen.setObjectName("tool_button_francais_moyen")
        self.tool_button_francais_difficile = QtWidgets.QToolButton(self.intercalaire_francais)
        self.tool_button_francais_difficile.setGeometry(QtCore.QRect(20, 219, 171, 81))
        self.tool_button_francais_difficile.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 14pt \"Times New Roman\";")
        self.tool_button_francais_difficile.setObjectName("tool_button_francais_difficile")
        self.tool_button_francais_moyen.raise_()
        self.tool_button_francais_difficile.raise_()
        self.tool_button_francais_facile.raise_()
        self.tabw_intercalaires.addTab(self.intercalaire_francais, "")
        self.intercalaire_anglais = QtWidgets.QWidget()
        self.intercalaire_anglais.setObjectName("intercalaire_anglais")
        self.tool_button_anglais_facile = QtWidgets.QToolButton(self.intercalaire_anglais)
        self.tool_button_anglais_facile.setGeometry(QtCore.QRect(20, 20, 171, 81))
        self.tool_button_anglais_facile.setStyleSheet("nfont: 14pt \"Times New Roman\";\n"
"background-color: rgb(170, 255, 0);\n"
"font: 8pt \"Times New Roman\";\n"
"font: 14pt ;")
        self.tool_button_anglais_facile.setObjectName("tool_button_anglais_facile")
        self.tool_button_anglais_moyen = QtWidgets.QToolButton(self.intercalaire_anglais)
        self.tool_button_anglais_moyen.setGeometry(QtCore.QRect(20, 120, 171, 81))
        self.tool_button_anglais_moyen.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 14pt \"Times New Roman\";\n"
"font: 8pt \"Times New Roman\";\n"
"font: 14pt ;")
        self.tool_button_anglais_moyen.setObjectName("tool_button_anglais_moyen")
        self.tool_button_anglais_difficile = QtWidgets.QToolButton(self.intercalaire_anglais)
        self.tool_button_anglais_difficile.setGeometry(QtCore.QRect(20, 220, 171, 81))
        self.tool_button_anglais_difficile.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 14pt \"Times New Roman\";")
        self.tool_button_anglais_difficile.setObjectName("tool_button_anglais_difficile")
        self.tabw_intercalaires.addTab(self.intercalaire_anglais, "")
        self.intercalaire_espagnol = QtWidgets.QWidget()
        self.intercalaire_espagnol.setObjectName("intercalaire_espagnol")
        self.tool_button_espagnol_facile = QtWidgets.QToolButton(self.intercalaire_espagnol)
        self.tool_button_espagnol_facile.setGeometry(QtCore.QRect(20, 20, 171, 81))
        self.tool_button_espagnol_facile.setStyleSheet("nfont: 14pt \"Times New Roman\";\n"
"background-color: rgb(170, 255, 0);\n"
"font: 8pt \"Times New Roman\";\n"
"font: 14pt ;")
        self.tool_button_espagnol_facile.setObjectName("tool_button_espagnol_facile")
        self.tool_button_espagnol_moyen = QtWidgets.QToolButton(self.intercalaire_espagnol)
        self.tool_button_espagnol_moyen.setGeometry(QtCore.QRect(20, 120, 171, 81))
        self.tool_button_espagnol_moyen.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 14pt \"Times New Roman\";\n"
"font: 8pt \"Times New Roman\";\n"
"font: 14pt ;")
        self.tool_button_espagnol_moyen.setObjectName("tool_button_espagnol_moyen")
        self.tool_button_espagnol_difficile = QtWidgets.QToolButton(self.intercalaire_espagnol)
        self.tool_button_espagnol_difficile.setGeometry(QtCore.QRect(20, 220, 171, 81))
        self.tool_button_espagnol_difficile.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 14pt \"Times New Roman\";")
        self.tool_button_espagnol_difficile.setObjectName("tool_button_espagnol_difficile")
        self.tabw_intercalaires.addTab(self.intercalaire_espagnol, "")
        self.gridLayout_6.addWidget(self.tabw_intercalaires, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 4, 2, 1, 1)
        self.label_nom_dictee = QtWidgets.QLabel(Form)
        self.label_nom_dictee.setObjectName("label_nom_dictee")
        self.gridLayout_3.addWidget(self.label_nom_dictee, 0, 0, 1, 1)
        self.plain_text_dictee = QtWidgets.QPlainTextEdit(Form)
        self.plain_text_dictee.setPlainText("")
        self.plain_text_dictee.setObjectName("plain_text_dictee")
        self.gridLayout_3.addWidget(self.plain_text_dictee, 9, 0, 1, 1)
        self.label_correction = QtWidgets.QLabel(Form)
        self.label_correction.setObjectName("label_correction")
        self.gridLayout_3.addWidget(self.label_correction, 9, 2, 1, 1)
        self.label_nom_dictee_apparait = QtWidgets.QLabel(Form)
        self.label_nom_dictee_apparait.setObjectName("label_nom_dictee_apparait")
        self.gridLayout_3.addWidget(self.label_nom_dictee_apparait, 1, 0, 1, 1)
        self.label_note = QtWidgets.QLabel(Form)
        self.label_note.setObjectName("label_note")
        self.gridLayout_3.addWidget(self.label_note, 0, 2, 1, 1)
        self.label_message_erreur_ou_bravo = QtWidgets.QLabel(Form)
        self.label_message_erreur_ou_bravo.setObjectName("label_message_erreur_ou_bravo")
        self.gridLayout_3.addWidget(self.label_message_erreur_ou_bravo, 1, 2, 1, 1)
        self.pb_valider_dictee = QtWidgets.QPushButton(Form)
        self.pb_valider_dictee.setObjectName("pb_valider_dictee")
        self.gridLayout_3.addWidget(self.pb_valider_dictee, 10, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 2, 1, 1)
        self.pb_stop = QtWidgets.QPushButton(Form)
        self.pb_stop.setObjectName("pb_stop")
        self.gridLayout_4.addWidget(self.pb_stop, 0, 3, 1, 1)
        self.pb_play_pause = QtWidgets.QPushButton(Form)
        self.pb_play_pause.setObjectName("pb_play_pause")
        self.gridLayout_4.addWidget(self.pb_play_pause, 0, 0, 1, 1)
        self.pb_rejouer = QtWidgets.QPushButton(Form)
        self.pb_rejouer.setObjectName("pb_rejouer")
        self.gridLayout_4.addWidget(self.pb_rejouer, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 10, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_titre = QtWidgets.QLabel(Form)
        self.label_titre.setStyleSheet("font: 20pt \"Lucida Handwriting\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 170, 127);\n"
"text-decoration: underline;")
        self.label_titre.setObjectName("label_titre")
        self.gridLayout_5.addWidget(self.label_titre, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabw_intercalaires.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_quitter.setText(_translate("Form", "Quitter"))
        self.tool_button_francais_facile.setText(_translate("Form", "Niveau facile"))
        self.tool_button_francais_moyen.setText(_translate("Form", "Niveau moyen "))
        self.tool_button_francais_difficile.setText(_translate("Form", "Niveau difficile"))
        self.tabw_intercalaires.setTabText(self.tabw_intercalaires.indexOf(self.intercalaire_francais), _translate("Form", "Français"))
        self.tool_button_anglais_facile.setText(_translate("Form", "Easy level"))
        self.tool_button_anglais_moyen.setText(_translate("Form", "Medium level"))
        self.tool_button_anglais_difficile.setText(_translate("Form", "Hard level"))
        self.tabw_intercalaires.setTabText(self.tabw_intercalaires.indexOf(self.intercalaire_anglais), _translate("Form", "English"))
        self.tool_button_espagnol_facile.setText(_translate("Form", "Nivel fácil"))
        self.tool_button_espagnol_moyen.setText(_translate("Form", "Nivel medio"))
        self.tool_button_espagnol_difficile.setText(_translate("Form", "Nivel dificil"))
        self.tabw_intercalaires.setTabText(self.tabw_intercalaires.indexOf(self.intercalaire_espagnol), _translate("Form", "Español"))
        self.label_nom_dictee.setText(_translate("Form", "Non de la dictée :"))
        self.label_correction.setText(_translate("Form", "La correction apparitra ici. "))
        self.label_nom_dictee_apparait.setText(_translate("Form", "Nom de la dictée qui apparait (s\'il y en a) "))
        self.label_note.setText(_translate("Form", "Note : "))
        self.label_message_erreur_ou_bravo.setText(_translate("Form", "ici message d\'erreur ou de félicitation"))
        self.pb_valider_dictee.setText(_translate("Form", "Valider ma dictée"))
        self.pb_stop.setText(_translate("Form", "stop"))
        self.pb_play_pause.setText(_translate("Form", "play / pause"))
        self.pb_rejouer.setText(_translate("Form", "rejouer"))
        self.label_titre.setText(_translate("Form", "                        S\'entrainer à la dictée                                  "))

