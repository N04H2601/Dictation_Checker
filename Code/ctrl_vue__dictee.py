# -*- coding: utf-8 -*-
# On importe les modules et fichiers .py nécessaires
import sys
import os

from os.path import basename, dirname, join

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal
from pygame.locals import*
from pygame import event
from pygame import mixer
import pygame
from pylanguagetool import api as languageapi
import webbrowser

from model__dictee import *
from data__dictee import *
from vue__dictee import *
from vue_evaluation__dictee import *
from maquette_accueil_from_ui__dictee import *
from outils__dictee import *
from ctrl_vue_evaluation__dictee import *


# On définit la classe Ctrl_vue
class Ctrl_vue():
    def __init__(self, model=None, vue=None):
        self.model = model
        self.vue = vue
        self.action_on_sound_file = None
        self.sound_is_playing = False
        self.sound_status = "stopped"
        # On connecte les boutons niveau(langue) à leur fonction respective lorsqu'ils sont pressés
        self.vue.ui.tool_button_francais_facile.clicked.connect( \
          self.action_toolButton_francais_facile_clicked)
        self.vue.ui.tool_button_francais_moyen.clicked.connect( \
          self.action_toolButton_francais_moyen_clicked)
        self.vue.ui.tool_button_francais_difficile.clicked.connect( \
          self.action_toolButton_francais_difficile_clicked)
        self.vue.ui.tool_button_anglais_facile.clicked.connect( \
          self.action_toolButton_anglais_facile_clicked)
        self.vue.ui.tool_button_anglais_moyen.clicked.connect( \
          self.action_toolButton_anglais_moyen_clicked)
        self.vue.ui.tool_button_anglais_difficile.clicked.connect( \
          self.action_toolButton_anglais_difficile_clicked)
        self.vue.ui.tool_button_espagnol_facile.clicked.connect( \
          self.action_toolButton_espagnol_facile_clicked)
        self.vue.ui.tool_button_espagnol_moyen.clicked.connect( \
          self.action_toolButton_espagnol_moyen_clicked)
        self.vue.ui.tool_button_espagnol_difficile.clicked.connect( \
          self.action_toolButton_espagnol_difficile_clicked)
        # On connecte les boutons relatifs à l'audio et le bouton "tout effacer" à leur fonction respective lorsqu'ils sont pressés
        self.vue.ui.pb_play_pause.clicked.connect (self.action_pb_play_pause_clicked)
        self.vue.ui.pb_stop.clicked.connect (self.action_pb_stop_clicked)
        self.vue.ui.pb_rejouer.clicked.connect (self.action_pb_rejouer_clicked)
        self.vue.ui.pb_valider_dictee.clicked.connect (self.action_pb_valider_dictee_clicked)
        self.vue.ui.pb_next_dictee.clicked.connect (self.action_pb_dictee_suivante_clicked)
        self.vue.ui.pb_prev_dictee.clicked.connect (self.action_pb_dictee_precedente_clicked)
        self.vue.ui.pb_rewind.clicked.connect(self.action_pb_rewind_clicked)
        self.vue.ui.pb_clear.clicked.connect(self.action_pb_clear_texte_rentre_clicked)
        # On connecte les boutons accents/ponctuations à leur fonction respective lorsqu'ils sont pressés
        self.vue.ui.pb_accent1.clicked.connect(self.action_pb_accent1_clicked)
        self.vue.ui.pb_accent2.clicked.connect(self.action_pb_accent2_clicked)
        self.vue.ui.pb_accent3.clicked.connect(self.action_pb_accent3_clicked)
        self.vue.ui.pb_accent4.clicked.connect(self.action_pb_accent4_clicked)
        self.vue.ui.pb_accent5.clicked.connect(self.action_pb_accent5_clicked)
        self.vue.ui.pb_ponctuation1.clicked.connect(self.action_pb_ponctuation1_clicked)
        self.vue.ui.pb_ponctuation2.clicked.connect(self.action_pb_ponctuation2_clicked)
        # On connecte l'éditeur de texte à sa fonction respective lorsqu'il détecte du texte rentré ou du texte qui change
        self.vue.ui.plain_text_dictee.textChanged.connect(self.action_plain_text_dictee_textChanged)
        # On connecte l'onglet avec les langues (et niveaux) à sa fonction respective lorsque l'index varie
        self.vue.ui.tabw_langues.currentChanged.connect(self.action_tabw_langues_currentChanged)
        # On connecte le boutton info-ponctuation à sa fonction respective lorsqu'il est pressé
        self.vue.ui.pb_info.clicked.connect(self.action_pb_info_clicked)
        self.vue.ui.pb_evaluation.clicked.connect(self.action_pb_evaluation_clicked)

    # On définit la fonction qui "sauvegarde" le texte rentré
    # Elle est déclenchée à chaque fois que le texte entré dans l'éditeur change
    # Remarque : la fonction corriger n'est pas parfaite, mais repère la plupart des fautes
    def action_plain_text_dictee_textChanged (self):
        if self.model.current_dictee == None :
            pass
        else :
            self.vue.ui.plain_text_dictee.setEnabled(True)
            self.model.current_dictee.texte = self.vue.ui.plain_text_dictee.toPlainText ()

    # On définit la fonction corriger, avec la note, le commentaire et les fautes relevées
    def correcteur (self) :
        # La fonction corriger prend en entrée le texte rentré par l'utilisateur et détecte automatiquement la langue
        phrase = self.vue.ui.plain_text_dictee.toPlainText()
        result = languageapi.check(
            phrase,
            api_url = 'https://languagetool.org/api/v2/',
            lang = "auto",
        )

        langue1 = result["language"]["detectedLanguage"]["code"].split("-")[0]
        resultText = ""

        # La variable note_boucle ci-dessous permet de parcourir la liste des erreurs et d'en déduire une note sur 20 après calcul
        note_boucle = 0
        if langue1 != "fr" and langue1 != "es" and langue1 != "en" :
            # Ici, on ne corrige que le français, l'anglais et l'espagnol, sinon le correcteur renvoie le message ci-après
            resultText += "Le correcteur ne supporte que le français, l'anglais et l'espagnol !\n"
            resultText += "---------------------------------------------------------\n"
            resultText += '---------------------------------------------------------\n'
            self.vue.ui.plain_correction_dictee.setPlainText(resultText)
            self.vue.ui.label_note_apparait.setText("")
            self.vue.ui.plain_fautes.setPlainText("")
            self.vue.ui.label_commentaire_apparait.setText("")
            self.vue.ui.plain_corrige_dictee.setPlainText ("")
        else :
            if langue1 == "fr" :
                resultFautes = ""
                testFautes = ""
                if result["matches"] == [] :
                    resultText += "Aucune faute !\n"
                    resultText += "---------------------------------------------------------\n"
                    resultFautes += "Aucune faute !\n"
                else :
                    for match in result["matches"]:
                        liste_lettre = []
                        i = 0
                        liste_retour = []
                        for lettre in str(self.vue.ui.plain_text_dictee.toPlainText()) :
                            liste_lettre.append(lettre)
                        # On a une liste des caractères du texte rentré
                        for i in range (int(match["length"])) :
                            liste_retour.append(liste_lettre[(int(match["offset"])) + i])
                        # On ne garde que celles composant le mot fauté grâce à la place du premier caractère du mot dans la liste précédente et sa longueur
                        correct = "".join(liste_retour)
                        # On transforme les lettres en mot : on a récupéré le mot fauté, que l'on ajoute à la liste des fautes
                        text_str = str(self.vue.ui.plain_text_dictee.toPlainText())
                        correct_str = str(correct)
                        resultFautes += correct_str + "\n"
                        testFautes += correct_str + " "
                        
                        if match['message'] != "Possible spelling mistake found." :
                            resultText += str(match['message']) + "\n"
                        if match['shortMessage'] != '' :
                            resultText += str(match['shortMessage']) + "\n"
                        if match['replacements'] != [] :
                            if len(match['replacements']) == 1 :
                                resultText += "La correction est : " + str(match['replacements'][0].get('value')) + "\n"
                            else :
                                resultText += "La correction est : " + str(match['replacements'][0].get('value')) + "\n"
                                resultText += "(2ème correction éventuelle) : " + str(match['replacements'][1].get('value')) + "\n"
                            
                        resultText += "Type d'erreur : " + str(match['rule']['category'].get('name')) + "\n"
                        resultText += "---------------------------------------------------------\n"
                        note_boucle = note_boucle + 1
                        # On a récupéré la/les deux plus probable(s) correction(s) du mot et le type d'erreur


                    # Le code suivant permet de mettre en rouge les fautes
                    testFautesSplit = testFautes.split()
            
                    text_dictee = str(self.vue.ui.plain_text_dictee.toPlainText())
                    text_dictee_split = text_dictee.split()

                    i = 0
                    j = 0
                    red_correct = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                    while i < len(text_dictee_split) and j < len(testFautesSplit) :
                        if text_dictee_split[i][-1] == "." :
                            testFautesSplit[j] = testFautesSplit[j] + "."
                        else :
                            pass
                        if text_dictee_split[i] == testFautesSplit[j] :
                            if str(text_dictee_split[i][-1]) == "." :
                                text_dictee_split[i] = text_dictee_split[i].replace(".", "")
                                red_correct += "<span style=\" color:#e6310c;\">" + str(text_dictee_split[i]) + "</span>. "
                            else :
                                red_correct += "<span style=\" color:#e6310c;\">" + str(text_dictee_split[i]) + " </span>"
                            j = j + 1
                            i = i + 1
                        elif text_dictee_split[i] != testFautesSplit[j] :
                            red_correct += str(text_dictee_split[i]) + " "
                            i = i + 1
                    red_correct += "</p></body></html>"
                    
                    self.vue.ui.plain_text_dictee.deleteLater()
                    
                    _translate = QtCore.QCoreApplication.translate
                    self.vue.ui.browser_text_dictee = QtWidgets.QTextBrowser()
                    self.vue.ui.browser_text_dictee.setObjectName("browser_text_dictee")
                    self.vue.ui.gridLayout_3.addWidget(self.vue.ui.browser_text_dictee, 10, 0, 1, 1)
                    self.vue.ui.browser_text_dictee.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.vue.ui.browser_text_dictee.setHtml(_translate("Form", red_correct))


            elif langue1 == "es" :
                resultFautes = ""
                testFautes = ""
                if result["matches"] == [] :
                    resultText += "Sin error !\n"
                    resultText += "---------------------------------------------------------\n"
                    resultFautes += "Sin error !\n"
                else :
                    for match in result["matches"]:
                        liste_lettre = []
                        i = 0
                        liste_retour = []
                        for lettre in str(self.vue.ui.plain_text_dictee.toPlainText()) :
                            liste_lettre.append(lettre)
                        # On a une liste des caractères du texte rentré
                        for i in range (int(match["length"])) :
                            liste_retour.append(liste_lettre[(int(match["offset"])) + i])
                        # On ne garde que celles composant le mot fauté grâce à la place du premier caractère du mot dans la liste précédente et sa longueur
                        correct = "".join(liste_retour)
                        # On transforme les lettres en mot : on a récupéré le mot fauté, que l'on ajoute à la liste des fautes
                        text_str = str(self.vue.ui.plain_text_dictee.toPlainText())
                        correct_str = str(correct)
                        resultFautes += correct_str + "\n"
                        testFautes += correct_str + " "
                        
                        if match['message'] != "Possible spelling mistake found." :
                            resultText += str(match['message']) + "\n"
                        if match['shortMessage'] != '' :
                            resultText += str(match['shortMessage']) + "\n"
                        if match['replacements'] != [] :
                            if len(match['replacements']) == 1 :
                                resultText += "La corrección es : " + str(match['replacements'][0].get('value')) + "\n"
                            else :
                                resultText += "La corrección es : " + str(match['replacements'][0].get('value')) + "\n"
                                resultText += "(2da corrección posible) : " + str(match['replacements'][1].get('value')) + "\n"
                            
                        resultText += "Tipo de error : " + str(match['rule']['category'].get('name')) + "\n"
                        resultText += "---------------------------------------------------------\n"
                        note_boucle = note_boucle + 1
                        # On a récupéré la/les deux plus probable(s) correction(s) du mot et le type d'erreur


                    # Le code suivant permet de mettre en rouge les fautes
                    testFautesSplit = testFautes.split()
            
                    text_dictee = str(self.vue.ui.plain_text_dictee.toPlainText())
                    text_dictee_split = text_dictee.split()

                    i = 0
                    j = 0
                    red_correct = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                    while i < len(text_dictee_split) and j < len(testFautesSplit) :
                        if text_dictee_split[i][-1] == "." :
                            testFautesSplit[j] = testFautesSplit[j] + "."
                        else :
                            pass
                        if text_dictee_split[i] == testFautesSplit[j] :
                            if str(text_dictee_split[i][-1]) == "." :
                                text_dictee_split[i] = text_dictee_split[i].replace(".", "")
                                red_correct += "<span style=\" color:#e6310c;\">" + str(text_dictee_split[i]) + "</span>. "
                            else :
                                red_correct += "<span style=\" color:#e6310c;\">" + str(text_dictee_split[i]) + " </span>"
                            j = j + 1
                            i = i + 1
                        elif text_dictee_split[i] != testFautesSplit[j] :
                            red_correct += str(text_dictee_split[i]) + " "
                            i = i + 1
                    red_correct += "</p></body></html>"
                    
                    self.vue.ui.plain_text_dictee.deleteLater()
                    
                    _translate = QtCore.QCoreApplication.translate
                    self.vue.ui.browser_text_dictee = QtWidgets.QTextBrowser()
                    self.vue.ui.browser_text_dictee.setObjectName("browser_text_dictee")
                    self.vue.ui.gridLayout_3.addWidget(self.vue.ui.browser_text_dictee, 10, 0, 1, 1)
                    self.vue.ui.browser_text_dictee.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.vue.ui.browser_text_dictee.setHtml(_translate("Form", red_correct))

            elif langue1 == "en" :
                resultFautes = ""
                testFautes = ""
                if result["matches"] == [] :
                    resultText += "No mistake !\n"
                    resultText += "---------------------------------------------------------\n"
                    resultFautes += "No mistake !\n"
                else :
                    for match in result["matches"]:
                        liste_lettre = []
                        i = 0
                        liste_retour = []
                        for lettre in str(self.vue.ui.plain_text_dictee.toPlainText()) :
                            liste_lettre.append(lettre)
                        # On a une liste des caractères du texte rentré
                        for i in range (int(match["length"])) :
                            liste_retour.append(liste_lettre[(int(match["offset"])) + i])
                        # On ne garde que celles composant le mot fauté grâce à la place du premier caractère du mot dans la liste précédente et sa longueur
                        correct = "".join(liste_retour)
                        # On transforme les lettres en mot : on a récupéré le mot fauté, que l'on ajoute à la liste des fautes
                        text_str = str(self.vue.ui.plain_text_dictee.toPlainText())
                        correct_str = str(correct)
                        resultFautes += correct_str + "\n"
                        testFautes += correct_str + " "
                        
                        if match['message'] != "Possible spelling mistake found." :
                            resultText += str(match['message']) + "\n"
                        if match['shortMessage'] != '' :
                            resultText += str(match['shortMessage']) + "\n"
                        if match['replacements'] != [] :
                            if len(match['replacements']) == 1 :
                                resultText += "The correction is : " + str(match['replacements'][0].get('value')) + "\n"
                            else :
                                resultText += "The correction is : " + str(match['replacements'][0].get('value')) + "\n"
                                resultText += "(2nd possible correction) : " + str(match['replacements'][1].get('value')) + "\n"
                            
                        resultText += "Type of mistake : " + str(match['rule']['category'].get('name')) + "\n"
                        resultText += "---------------------------------------------------------\n"
                        note_boucle = note_boucle + 1
                        # On a récupéré la/les deux plus probable(s) correction(s) du mot et le type d'erreur


                    # Le code suivant permet de mettre en rouge les fautes
                    testFautesSplit = testFautes.split()
            
                    text_dictee = str(self.vue.ui.plain_text_dictee.toPlainText())
                    text_dictee_split = text_dictee.split()

                    i = 0
                    j = 0
                    red_correct = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                    while i < len(text_dictee_split) and j < len(testFautesSplit) :
                        if text_dictee_split[i][-1] == "." :
                            testFautesSplit[j] = testFautesSplit[j] + "."
                        else :
                            pass
                        if text_dictee_split[i] == testFautesSplit[j] :
                            if str(text_dictee_split[i][-1]) == "." :
                                text_dictee_split[i] = text_dictee_split[i].replace(".", "")
                                red_correct += "<span style=\" color:#e6310c;\">" + str(text_dictee_split[i]) + "</span>. "
                            else :
                                red_correct += "<span style=\" color:#e6310c;\">" + str(text_dictee_split[i]) + " </span>"
                            j = j + 1
                            i = i + 1
                        elif text_dictee_split[i] != testFautesSplit[j] :
                            red_correct += str(text_dictee_split[i]) + " "
                            i = i + 1
                    red_correct += "</p></body></html>"
                    
                    self.vue.ui.plain_text_dictee.deleteLater()
                    
                    _translate = QtCore.QCoreApplication.translate
                    self.vue.ui.browser_text_dictee = QtWidgets.QTextBrowser()
                    self.vue.ui.browser_text_dictee.setObjectName("browser_text_dictee")
                    self.vue.ui.gridLayout_3.addWidget(self.vue.ui.browser_text_dictee, 10, 0, 1, 1)
                    self.vue.ui.browser_text_dictee.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.vue.ui.browser_text_dictee.setHtml(_translate("Form", red_correct))
                        
            resultText += '---------------------------------------------------------\n'

            self.vue.ui.plain_correction_dictee.setPlainText(resultText)
            self.vue.ui.label_note_apparait.setText(str(20-note_boucle)+str("/20"))
            self.vue.ui.plain_fautes.setStyleSheet("color: rgb(255, 0, 0);\n"
                                                   "background-color: rgb(255, 255, 255);")
            self.vue.ui.plain_fautes.setPlainText(resultFautes)
            
            
            # On affiche la correction, la note et les fautes

            if langue1 == "fr" :
                if 20-note_boucle >= 17 :
                    self.vue.ui.label_commentaire_apparait.setText("Excellent !")
                if 20-note_boucle == 16 :
                    self.vue.ui.label_commentaire_apparait.setText("Très bien !")
                if 20-note_boucle == 14 or 20-note_boucle == 15 :
                    self.vue.ui.label_commentaire_apparait.setText("Bien.")
                if 20-note_boucle == 12 or 20-note_boucle == 13 :
                    self.vue.ui.label_commentaire_apparait.setText("Assez bien.")
                if 20-note_boucle == 10 or 20-note_boucle == 11 :
                    self.vue.ui.label_commentaire_apparait.setText("Passable.")
                if 20-note_boucle == 8 or 20-note_boucle == 9 :
                    self.vue.ui.label_commentaire_apparait.setText("Insuffisant.")
                if 20-note_boucle == 6 or 20-note_boucle == 7 :
                    self.vue.ui.label_commentaire_apparait.setText("Faible.")
                if 20-note_boucle < 6 :
                    self.vue.ui.label_commentaire_apparait.setText("Médiocre.")
            if langue1 == "en" :
                if 20-note_boucle >= 17 :
                    self.vue.ui.label_commentaire_apparait.setText("Excellent !")
                if 20-note_boucle == 16 :
                    self.vue.ui.label_commentaire_apparait.setText("Very good !")
                if 20-note_boucle == 14 or 20-note_boucle == 15 :
                    self.vue.ui.label_commentaire_apparait.setText("Good.")
                if 20-note_boucle == 12 or 20-note_boucle == 13 :
                    self.vue.ui.label_commentaire_apparait.setText("Pretty good.")
                if 20-note_boucle == 10 or 20-note_boucle == 11 :
                    self.vue.ui.label_commentaire_apparait.setText("Passable.")
                if 20-note_boucle == 8 or 20-note_boucle == 9 :
                    self.vue.ui.label_commentaire_apparait.setText("Insufficient.")
                if 20-note_boucle == 6 or 20-note_boucle == 7 :
                    self.vue.ui.label_commentaire_apparait.setText("Low.")
                if 20-note_boucle < 6 :
                    self.vue.ui.label_commentaire_apparait.setText("Poor.")
            if langue1 == "es" :
                if 20-note_boucle >= 17 :
                    self.vue.ui.label_commentaire_apparait.setText("Excelente !")
                if 20-note_boucle == 16 :
                    self.vue.ui.label_commentaire_apparait.setText("Muy bien !")
                if 20-note_boucle == 14 or 20-note_boucle == 15 :
                    self.vue.ui.label_commentaire_apparait.setText("Bien.")
                if 20-note_boucle == 12 or 20-note_boucle == 13 :
                    self.vue.ui.label_commentaire_apparait.setText("Bastante bien.")
                if 20-note_boucle == 10 or 20-note_boucle == 11 :
                    self.vue.ui.label_commentaire_apparait.setText("Justa.")
                if 20-note_boucle == 8 or 20-note_boucle == 9 :
                    self.vue.ui.label_commentaire_apparait.setText("Insuficiente.")
                if 20-note_boucle == 6 or 20-note_boucle == 7 :
                    self.vue.ui.label_commentaire_apparait.setText("Bajo.")
                if 20-note_boucle < 6 :
                    self.vue.ui.label_commentaire_apparait.setText("Pobre.")
            # On affiche un commentaire (dans la langue actuelle) en fonction de la note

            # Si aucune dictée n'a été selectionnée, aucun corrigé n'est affiché, sinon c'est celui de la dernière dictée selectionnée qui s'affiche
            if self.sound_status == "stopped" :
                self.vue.ui.plain_corrige_dictee.setPlainText ("Pas de dictée sélectionée.")
            else :
                self.vue.update()

            
    # On définit la fonction a effectuer lorsque le bouton corriger est pressé
    # Elle appelle la fonction corriger ci-dessus et ne se déclenche que si du texte a été rentré
    def action_pb_valider_dictee_clicked (self):
        # Faire une double correction (pour trouver les double-erreurs après une première correction)
        self.vue.ui.plain_fautes.setStyleSheet("color: rgb(255, 0, 0);\n"
                                                   "background-color: rgb(255, 255, 255);")
        if self.sound_status == "stopped" :
            msg_information_audio = QMessageBox()
            msg_information_audio.setWindowTitle("Information")
            msg_information_audio.setText("Aucune dictée sélectionnée.")
            msg_information_audio.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_audio.setIcon(QMessageBox.Information)
            msg_information_audio.setStandardButtons(QMessageBox.Yes)
            button_oui_audio = msg_information_audio.button(QMessageBox.Yes)
            button_oui_audio.setText("Ok")
            if msg_information_audio.exec_() == QMessageBox.Yes :
                pass
        else :
            # La fonction corriger prend en entrée le texte rentré par l'utilisateur et détecte automatiquement la langue
            phrase = self.vue.ui.plain_text_dictee.toPlainText()
            result = languageapi.check(
                phrase,
                api_url = 'https://languagetool.org/api/v2/',
                lang = "auto",
            )

            langue1 = result["language"]["detectedLanguage"]["code"].split("-")[0]
            str_langue = str(self.get_current_langue())
            if str_langue[1] != langue1[1] :
                msg_information_langue = QMessageBox()
                msg_information_langue.setWindowTitle("Information")
                msg_information_langue.setText("La langue de la dictée n'est pas la même que celle du texte rentré.")
                msg_information_langue.setWindowIcon(QtGui.QIcon("info.png"))
                msg_information_langue.setIcon(QMessageBox.Information)
                msg_information_langue.setStandardButtons(QMessageBox.Yes)
                button_oui_langue = msg_information_langue.button(QMessageBox.Yes)
                button_oui_langue.setText("Ok")
                if msg_information_langue.exec_() == QMessageBox.Yes :
                    pass
            if self.vue.ui.plain_text_dictee.toPlainText() == "" :
                msg_information_valider = QMessageBox()
                msg_information_valider.setWindowTitle("Information")
                msg_information_valider.setText("Aucun texte rentré.")
                msg_information_valider.setWindowIcon(QtGui.QIcon("info.png"))
                msg_information_valider.setIcon(QMessageBox.Information)
                msg_information_valider.setStandardButtons(QMessageBox.Yes)
                button_oui_valider = msg_information_valider.button(QMessageBox.Yes)
                button_oui_valider.setText("Ok")
                if msg_information_valider.exec_() == QMessageBox.Yes :
                    pass
            elif  str_langue[1] == langue1[1] :
                # Si du texte a été rentré, elle l'enregistre en effectuant une copie (ctrl+C)
                clipboard = QApplication.clipboard()
                clipboard.setText(self.vue.ui.plain_text_dictee.toPlainText())
                self.correcteur()
                # Puis, elle appelle la fonction corriger
                # Enfin, on met le bouton corriger en mode non éditable pour que l'utilisateur n'ait plus accès au texte rentré (mais sauvegardé)
                # et n'effectue qu'une seule correction, symbolique
                self.vue.ui.pb_valider_dictee.setEnabled(False)
                self.vue.ui.tool_button_francais_facile.setEnabled(False)
                self.vue.ui.tool_button_francais_moyen.setEnabled(False)
                self.vue.ui.tool_button_francais_difficile.setEnabled(False)
                self.vue.ui.tool_button_anglais_facile.setEnabled(False)
                self.vue.ui.tool_button_anglais_moyen.setEnabled(False)
                self.vue.ui.tool_button_anglais_difficile.setEnabled(False)
                self.vue.ui.tool_button_espagnol_facile.setEnabled(False)
                self.vue.ui.tool_button_espagnol_moyen.setEnabled(False)
                self.vue.ui.tool_button_espagnol_difficile.setEnabled(False)
                self.vue.ui.pb_play_pause.setEnabled(False)
                self.vue.ui.pb_stop.setEnabled(False)
                self.vue.ui.pb_rejouer.setEnabled(False)
                self.vue.ui.pb_next_dictee.setEnabled(False)
                self.vue.ui.pb_prev_dictee.setEnabled(False)
                self.vue.ui.pb_rewind.setEnabled(False)
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.vue.ui.pb_play_pause.setIcon(icon6)
                self.vue.ui.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
                self.action_pb_stop_clicked()
                self.vue.ui.plain_fautes.setStyleSheet("color: rgb(255, 0, 0);\n"
                                                   "background-color: rgb(255, 255, 255);")

    # Les fonctions suivantes permettent d'avoir accès aux accents et à la ponctuation espagnols en cliquant dessus,
    # ce qui va l'ajouter au plain (texte à entrer par l'utilisateur)
    def action_pb_accent1_clicked (self) :
        try:
            self.vue.ui.plain_text_dictee.insertPlainText("á")
        except :
            msg_information_accent1 = QMessageBox()
            msg_information_accent1.setWindowTitle("Information")
            msg_information_accent1.setText("Vous ne pouvez plus modifier la dictée rentrée.")
            msg_information_accent1.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_accent1.setIcon(QMessageBox.Information)
            msg_information_accent1.setStandardButtons(QMessageBox.Yes)
            button_oui_accent1 = msg_information_accent1.button(QMessageBox.Yes)
            button_oui_accent1.setText("Ok")
            if msg_information_accent1.exec_() == QMessageBox.Yes :
                pass
        
    def action_pb_accent2_clicked (self) :
        try:
            self.vue.ui.plain_text_dictee.insertPlainText("í")
        except :
            msg_information_accent2 = QMessageBox()
            msg_information_accent2.setWindowTitle("Information")
            msg_information_accent2.setText("Vous ne pouvez plus modifier la dictée rentrée.")
            msg_information_accent2.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_accent2.setIcon(QMessageBox.Information)
            msg_information_accent2.setStandardButtons(QMessageBox.Yes)
            button_oui_accent2 = msg_information_accent2.button(QMessageBox.Yes)
            button_oui_accent2.setText("Ok")
            if msg_information_accent2.exec_() == QMessageBox.Yes :
                pass
        
    def action_pb_accent3_clicked (self) :
        try:
            self.vue.ui.plain_text_dictee.insertPlainText("ó")
        except :
            msg_information_accent3 = QMessageBox()
            msg_information_accent3.setWindowTitle("Information")
            msg_information_accent3.setText("Vous ne pouvez plus modifier la dictée rentrée.")
            msg_information_accent3.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_accent3.setIcon(QMessageBox.Information)
            msg_information_accent3.setStandardButtons(QMessageBox.Yes)
            button_oui_accent3 = msg_information_accent3.button(QMessageBox.Yes)
            button_oui_accent3.setText("Ok")
            if msg_information_accent3.exec_() == QMessageBox.Yes :
                pass
        
    def action_pb_accent4_clicked (self) :
        try:
            self.vue.ui.plain_text_dictee.insertPlainText("ú")
        except :
            msg_information_accent4 = QMessageBox()
            msg_information_accent4.setWindowTitle("Information")
            msg_information_accent4.setText("Vous ne pouvez plus modifier la dictée rentrée.")
            msg_information_accent4.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_accent4.setIcon(QMessageBox.Information)
            msg_information_accent4.setStandardButtons(QMessageBox.Yes)
            button_oui_accent4 = msg_information_accent4.button(QMessageBox.Yes)
            button_oui_accent4.setText("Ok")
            if msg_information_accent4.exec_() == QMessageBox.Yes :
                pass
    def action_pb_accent5_clicked (self) :
        try:
            self.vue.ui.plain_text_dictee.insertPlainText("ñ")
        except :
            msg_information_accent5 = QMessageBox()
            msg_information_accent5.setWindowTitle("Information")
            msg_information_accent5.setText("Vous ne pouvez plus modifier la dictée rentrée.")
            msg_information_accent5.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_accent5.setIcon(QMessageBox.Information)
            msg_information_accent5.setStandardButtons(QMessageBox.Yes)
            button_oui_accent5 = msg_information_accent5.button(QMessageBox.Yes)
            button_oui_accent5.setText("Ok")
            if msg_information_accent5.exec_() == QMessageBox.Yes :
                pass

    def action_pb_ponctuation1_clicked (self) :
        try:
            self.vue.ui.plain_text_dictee.insertPlainText("¡")
        except :
            msg_information_ponctuation1 = QMessageBox()
            msg_information_ponctuation1.setWindowTitle("Information")
            msg_information_ponctuation1.setText("Vous ne pouvez plus modifier la dictée rentrée.")
            msg_information_ponctuation1.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_ponctuation1.setIcon(QMessageBox.Information)
            msg_information_ponctuation1.setStandardButtons(QMessageBox.Yes)
            button_oui_ponctuation1 = msg_information_ponctuation1.button(QMessageBox.Yes)
            button_oui_ponctuation1.setText("Ok")
            if msg_information_ponctuation1.exec_() == QMessageBox.Yes :
                pass

    def action_pb_ponctuation2_clicked (self) :
        try:
            self.vue.ui.plain_text_dictee.insertPlainText("¡")
        except :
            msg_information_ponctuation2 = QMessageBox()
            msg_information_ponctuation2.setWindowTitle("Information")
            msg_information_ponctuation2.setText("Vous ne pouvez plus modifier la dictée rentrée.")
            msg_information_ponctuation2.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_ponctuation2.setIcon(QMessageBox.Information)
            msg_information_ponctuation2.setStandardButtons(QMessageBox.Yes)
            button_oui_ponctuation2 = msg_information_ponctuation2.button(QMessageBox.Yes)
            button_oui_ponctuation2.setText("Ok")
            if msg_information_ponctuation2.exec_() == QMessageBox.Yes :
                pass

    def action_pb_info_clicked (self) :
        webbrowser.open('http://www.ec-la-burliere-pertuis.ac-aix-marseille.fr/spip/sites/www.ec-la-burliere-pertuis/spip/IMG/pdf/la_ponctuation.pdf')

    def action_pb_evaluation_clicked (self) :
        if self.sound_status == "stopped" :
            pass
        else :
            self.action_pb_stop_clicked()
        self.vue.hide()
        self.model = Model ()
        self.vue = Vue2 (self.model)
        self.vue.show ()
        self.ctrl = Ctrl_vue2 (self.model, self.vue)


    # La fonction suivante permet d'obtenir la langue actuelle (pour les audios,...) grâce à l'index actuel de l'onglet
    def get_current_langue (self):
        cur_index = self.vue.ui.tabw_langues.currentIndex ()
        if cur_index == 0:
            cur_langue = langue_francais_text
        elif cur_index == 1:
            cur_langue = langue_anglais_text
        else:
            cur_langue = langue_espagnol_text
        return cur_langue


    # La fonction suivante affiche les accents espagnols seulement lorsque l'index de l'onglet correspond à cette langue
    # Ils sont cachés lors du démarrage et lorsque l'index est 2, on les affiche, sinon on les cache
    def action_tabw_langues_currentChanged (self, index):
        if self.vue.ui.tabw_langues.currentIndex() == 2:
            self.vue.ui.pb_accent1.show()
            self.vue.ui.pb_accent2.show()
            self.vue.ui.pb_accent3.show()
            self.vue.ui.pb_accent4.show()
            self.vue.ui.pb_accent5.show()
            self.vue.ui.pb_ponctuation1.show()
            self.vue.ui.pb_ponctuation2.show()
        else:
            self.vue.ui.pb_accent1.hide()
            self.vue.ui.pb_accent2.hide()
            self.vue.ui.pb_accent3.hide()
            self.vue.ui.pb_accent4.hide()
            self.vue.ui.pb_accent5.hide()
            self.vue.ui.pb_ponctuation1.hide()
            self.vue.ui.pb_ponctuation2.hide()
        if self.vue.ui.tabw_langues.currentIndex () == 0:
            self.model.current_langue = langue_francais_text
        elif self.vue.ui.tabw_langues.currentIndex () == 1:
            self.model.current_langue = langue_anglais_text
        else:
            self.model.current_langue = langue_espagnol_text

    # La focntion ci-après permet, lorsque un audio est en cours, de passer à la dictée suivante
    # Elle s'appuie sur l'indice actuel de la dictée en cours et s'arrête lorsqu'il n'y a plus d'autre dictée (suivante)
    def action_pb_dictee_suivante_clicked (self):
        if self.sound_status == "stopped" :
            msg_information_suivante = QMessageBox()
            msg_information_suivante.setWindowTitle("Information")
            msg_information_suivante.setText("Aucun audio en cours.")
            msg_information_suivante.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_suivante.setIcon(QMessageBox.Information)
            msg_information_suivante.setStandardButtons(QMessageBox.Yes)
            button_oui_suivante = msg_information_suivante.button(QMessageBox.Yes)
            button_oui_suivante.setText("Ok")
            if msg_information_suivante.exec_() == QMessageBox.Yes :
                pass
        else:
            if (self.model.current_langue != None) \
            and (self.model.current_niveau != None):
                langue = self.model.current_langue
                niveau = self.model.current_niveau
                sons = self.model.all_dictees[langue][niveau]
                if self.model.current_dictee_indice + 1 >= (len(self.model.all_dictees[langue][niveau])):
                    self.model.current_dictee_indice = (len(self.model.all_dictees[langue][niveau]))-1
                else :
                    self.model.current_dictee_indice += 1
                self.lecture_dictee(sons [self.model.current_dictee_indice])
                cur_indice = self.model.current_dictee_indice
                self.model.current_dictee = self.model.all_dictees [langue] [niveau] [cur_indice]
                self.sound_status == "unpaused"
                self.action_pb_play_pause_clicked ()
                self.vue.ui.plain_correction_dictee.setPlainText("")
                self.vue.ui.plain_corrige_dictee.setPlainText ("")
                self.vue.ui.label_commentaire_apparait.setText ("")
                self.vue.ui.label_note_apparait.setText ("")
                self.vue.ui.plain_fautes.setPlainText("")

    # La focntion ci-après permet, lorsque un audio est en cours, de passer à la dictée précédente
    # Elle s'appuie sur l'indice actuel de la dictée en cours et s'arrête lorsqu'il n'y a plus d'autre dictée (précédente)
    def action_pb_dictee_precedente_clicked (self) :
        if self.sound_status == "stopped" :
            msg_information_precedente = QMessageBox()
            msg_information_precedente.setWindowTitle("Information")
            msg_information_precedente.setText("Aucun audio en cours.")
            msg_information_precedente.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_precedente.setIcon(QMessageBox.Information)
            msg_information_precedente.setStandardButtons(QMessageBox.Yes)
            button_oui_precedente = msg_information_precedente.button(QMessageBox.Yes)
            button_oui_precedente.setText("Ok")
            if msg_information_precedente.exec_() == QMessageBox.Yes :
                pass
        else:
            if (self.model.current_langue != None) \
            and (self.model.current_niveau != None):
                langue = self.model.current_langue
                niveau = self.model.current_niveau
                sons = self.model.all_dictees[langue][niveau]
                if (self.model.current_dictee_indice - 1 < 0):
                    self.model.current_dictee_indice = 0
                else :
                    self.model.current_dictee_indice -= 1
                try:
                    self.lecture_dictee(sons [self.model.current_dictee_indice])
                except:
                    msg_information_soon = QMessageBox()
                    msg_information_soon.setWindowTitle("Information")
                    msg_information_soon.setText("Bientôt d'autres dictées...")
                    msg_information_soon.setWindowIcon(QtGui.QIcon("info.png"))
                    msg_information_soon.setIcon(QMessageBox.Information)
                    msg_information_soon.setStandardButtons(QMessageBox.Yes)
                    button_oui_soon = msg_information_soon.button(QMessageBox.Yes)
                    button_oui_soon.setText("Ok")
                    if msg_information_soon.exec_() == QMessageBox.Yes :
                        pass
                cur_indice = self.model.current_dictee_indice
                self.model.current_dictee = self.model.all_dictees [langue] [niveau] [cur_indice]
                self.sound_status == "unpaused"
                self.action_pb_play_pause_clicked ()
                self.vue.ui.plain_correction_dictee.setPlainText("")
                self.vue.ui.plain_corrige_dictee.setPlainText ("")
                self.vue.ui.label_commentaire_apparait.setText ("")
                self.vue.ui.label_note_apparait.setText ("")
                self.vue.ui.plain_fautes.setPlainText("")

    # La fonction ci-dessous permet d'effacer, la note, le commentaire, les fautes relevées, la correction et arrêter l'audio
    # Elle permet notamment de passer à une autre dictée mais elle sauvegarde elle aussi le texte rentré en le copiant (par précaution)
    def action_pb_clear_texte_rentre_clicked (self) :
        if self.sound_status == "playing" or self.sound_status == "unpaused":
            self.action_pb_play_pause_clicked ()
        else :
            pass
        msg = QMessageBox()
        msg.setWindowTitle("Attention !")
        msg.setText("Êtes-vous sûr de vouloir tout effacer ?")
        msg.setInformativeText("Le texte rentré sera tout de même copié.")
        msg.setWindowIcon(QtGui.QIcon("warning.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_oui = msg.button(QMessageBox.Yes)
        button_oui.setText("Oui")
        button_non = msg.button(QMessageBox.No)
        button_non.setText("Non")
        if msg.exec_() == QMessageBox.Yes :
            if self.sound_status != "stopped" :
                self.action_pb_stop_clicked()
            else :
                pass
            self.vue.ui.plain_correction_dictee.setPlainText("")
            self.vue.ui.plain_corrige_dictee.setPlainText ("")
            self.vue.ui.label_commentaire_apparait.setText ("")
            self.vue.ui.label_note_apparait.setText ("")
            self.vue.ui.label_nom_dictee_apparait.setText ("")
            self.vue.ui.plain_fautes.setPlainText("")
            self.vue.ui.pb_valider_dictee.setEnabled(True)
            self.vue.ui.tool_button_francais_facile.setEnabled(True)
            self.vue.ui.tool_button_francais_moyen.setEnabled(True)
            self.vue.ui.tool_button_francais_difficile.setEnabled(True)
            self.vue.ui.tool_button_anglais_facile.setEnabled(True)
            self.vue.ui.tool_button_anglais_moyen.setEnabled(True)
            self.vue.ui.tool_button_anglais_difficile.setEnabled(True)
            self.vue.ui.tool_button_espagnol_facile.setEnabled(True)
            self.vue.ui.tool_button_espagnol_moyen.setEnabled(True)
            self.vue.ui.tool_button_espagnol_difficile.setEnabled(True)
            self.vue.ui.pb_play_pause.setEnabled(True)
            self.vue.ui.pb_stop.setEnabled(True)
            self.vue.ui.pb_rejouer.setEnabled(True)
            self.vue.ui.pb_next_dictee.setEnabled(True)
            self.vue.ui.pb_prev_dictee.setEnabled(True)
            self.vue.ui.pb_rewind.setEnabled(True)
            try :
                clipboard = QApplication.clipboard()
                clipboard.setText(self.vue.ui.plain_text_dictee.toPlainText())
                self.vue.ui.plain_text_dictee.setPlainText("")
            except :
                self.vue.ui.plain_fautes.setStyleSheet("color: rgb(255, 0, 0);\n"
                                                   "background-color: rgb(255, 255, 255);")
                self.vue.ui.browser_text_dictee.deleteLater()
                self.vue.ui.plain_text_dictee = QtWidgets.QPlainTextEdit()
                self.vue.ui.plain_text_dictee.setPlaceholderText("Saisir ici votre dictée en respectant les règles de ponctuation et en mettant des accents aux majuscules :")
                self.vue.ui.plain_text_dictee.setObjectName("plain_text_dictee")
                self.vue.ui.plain_text_dictee.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.vue.ui.gridLayout_3.addWidget(self.vue.ui.plain_text_dictee, 10, 0, 1, 1)


    # Cette fonction permet la lecture d'un audio grâce à la langue et le niveau
    def lecture_dictee (self, dictee):
        mixer.init()
        pygame.init()
        self.ma_dictee = mixer.music
        self.ma_dictee.load (dictee.audio)
        self.ma_dictee.play ()
        self.sound_status = "playing"
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        sons = self.model.all_dictees[langue][niveau]
        self.vue.ui.label_nom_dictee_apparait.setText ((str(sons [self.model.current_dictee_indice].nom)).replace("_", " "))        

    # La fonction suivante permet de gérer les actions pause, unpause, rewind et stop
    def do_this_action_on_sound_file (self, cmd):
        if cmd == "pause":
            self.ma_dictee.pause ()
        if cmd == "unpause":
            self.ma_dictee.unpause ()
        if cmd == "stop":
            self.ma_dictee.stop ()
        if cmd == "play" :
            if self.sound_status == "stopped" :
                msg_information_cmd = QMessageBox()
                msg_information_cmd.setWindowTitle("Information")
                msg_information_cmd.setText("Aucun audio en cours.")
                msg_information_cmd.setWindowIcon(QtGui.QIcon("info.png"))
                msg_information_cmd.setIcon(QMessageBox.Information)
                msg_information_cmd.setStandardButtons(QMessageBox.Yes)
                button_oui_cmd = msg_information_cmd.button(QMessageBox.Yes)
                button_oui_cmd.setText("Ok")
                if msg_information_cmd.exec_() == QMessageBox.Yes :
                    pass
            else :
                self.ma_dictee.play()
                self.sound_status = "playing"
        if cmd == "rewind":
            self.ma_dictee.play ()
            self.sound_status = "playing"

            

    # Cette fonction permet de mettre en pause et unpause l'audio en cours et change notamment l'icône en fonction du statut de l'audio
    def action_pb_play_pause_clicked (self):
        if self.sound_status == "playing":
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vue.ui.pb_play_pause.setIcon(icon6)
            self.vue.ui.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
            cmd = "pause"
            self.sound_status = "paused"
        elif self.sound_status == "paused":
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vue.ui.pb_play_pause.setIcon(icon6)
            self.vue.ui.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
            cmd = "unpause"
            self.sound_status = "unpaused"
        elif self.sound_status == "unpaused":
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vue.ui.pb_play_pause.setIcon(icon6)
            self.vue.ui.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
            cmd = "pause"
            self.sound_status = "paused"
        elif self.sound_status == "stopped":
            cmd = "play"
        else:
            pass
        self.do_this_action_on_sound_file (cmd)

    # Cette fonction permet d'arrêter un audio
    def action_pb_stop_clicked (self):
        if self.sound_status == "stopped" :
            if self.sound_status == "stopped" :
                msg_information_stop = QMessageBox()
                msg_information_stop.setWindowTitle("Information")
                msg_information_stop.setText("Aucun audio en cours.")
                msg_information_stop.setWindowIcon(QtGui.QIcon("info.png"))
                msg_information_stop.setIcon(QMessageBox.Information)
                msg_information_stop.setStandardButtons(QMessageBox.Yes)
                button_oui_stop = msg_information_stop.button(QMessageBox.Yes)
                button_oui_stop.setText("Ok")
                if msg_information_stop.exec_() == QMessageBox.Yes :
                    pass
        else :
            cmd = "stop"
            self.sound_status = "stopped"
            self.vue.ui.plain_corrige_dictee.setPlainText ("Pas de dictée sélectionée.")
            self.do_this_action_on_sound_file (cmd)
            try :
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.vue.ui.pb_play_pause.setIcon(icon6)
                self.vue.ui.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
            except :
                pass
        self.vue.update_stop()

    # La fonction suivante permet de rejouer un audio en le jouant depuis le début
    def action_pb_rejouer_clicked (self):
        if self.sound_status == "stopped" :
            msg_information_rejouer = QMessageBox()
            msg_information_rejouer.setWindowTitle("Information")
            msg_information_rejouer.setText("Aucun audio en cours.")
            msg_information_rejouer.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_rejouer.setIcon(QMessageBox.Information)
            msg_information_rejouer.setStandardButtons(QMessageBox.Yes)
            button_oui_rejouer = msg_information_rejouer.button(QMessageBox.Yes)
            button_oui_rejouer.setText("Ok")
            if msg_information_rejouer.exec_() == QMessageBox.Yes :
                pass
        else :
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vue.ui.pb_play_pause.setIcon(icon6)
            self.vue.ui.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
            cmd = "rewind"
            self.do_this_action_on_sound_file (cmd)

    # Cette fonction (pour le mode entraînement) permet de remettre 10 secondes en arrière, notamment si l'utilisateur a mal saisi un mot
    def action_pb_rewind_clicked (self) :
        if self.sound_status == "stopped" :
            msg_information_rewind = QMessageBox()
            msg_information_rewind.setWindowTitle("Information")
            msg_information_rewind.setText("Aucun audio en cours.")
            msg_information_rewind.setWindowIcon(QtGui.QIcon("info.png"))
            msg_information_rewind.setIcon(QMessageBox.Information)
            msg_information_rewind.setStandardButtons(QMessageBox.Yes)
            button_oui_rewind = msg_information_rewind.button(QMessageBox.Yes)
            button_oui_rewind.setText("Ok")
            if msg_information_rewind.exec_() == QMessageBox.Yes :
                pass
        else :
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.vue.ui.pb_play_pause.setIcon(icon6)
            self.vue.ui.pb_play_pause.setIconSize(QtCore.QSize(60, 35))
            duree = self.ma_dictee.get_pos ()
            if (duree/1000)-10 > 0 :
                self.ma_dictee.stop()
                self.ma_dictee.play(start = (duree/1000)-10)
            else :
                cmd = "rewind"
                self.do_this_action_on_sound_file (cmd)
                
    # Cette fonction permet, lorsque l'utilisateur quitte la fenêtre, d'arrêter un audio en cours si tel est le cas
    def action_quitter (self):
        if self.sound_status != "stopped" :
            self.action_pb_stop_clicked ()
        sys.exit ()
        return


    # Les fonctions qui suivent permettent de définir la langue et le niveau en cours pour pouvoir ensuite jouer l'audio correspondant
    def action_toolButton_francais_facile_clicked(self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_facile_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()

    def action_toolButton_francais_moyen_clicked (self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_moyen_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()

    def action_toolButton_francais_difficile_clicked (self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_difficile_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()
         

    def action_toolButton_anglais_facile_clicked(self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_facile_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()
         

    def action_toolButton_anglais_moyen_clicked (self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_moyen_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()
         
    def action_toolButton_anglais_difficile_clicked (self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_difficile_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()
         

    def action_toolButton_espagnol_facile_clicked(self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_facile_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()
         

    def action_toolButton_espagnol_moyen_clicked (self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_moyen_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()
         

    def action_toolButton_espagnol_difficile_clicked (self):
        self.model.current_langue = self.get_current_langue ()
        self.model.current_niveau = niveau_difficile_text
        self.model.current_dictee_indice = 0
        langue = self.model.current_langue
        niveau = self.model.current_niveau
        indice = self.model.current_dictee_indice
        dictee = self.model.all_dictees [langue][niveau][indice]
        self.model.current_dictee = dictee
        liste_dictees = \
          list (map (lambda dictee: dictee.nom, self.model.all_dictees[langue][niveau]))
        self.lecture_dictee (self.model.current_dictee)
        self.action_pb_play_pause_clicked ()
        
