# -*- coding: utf-8 -*-
# On importe les modules et fichiers .py nécessaires
import sys
import os

from os.path import basename, dirname, join

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QMovie
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


# On définit la classe Ctrl_vue2
class Ctrl_vue2():
    def __init__(self, model=None, vue=None):
        self.model = model
        self.vue = vue
        self.action_on_sound_file = None
        self.sound_is_playing = False
        self.sound_status = "stopped"
        # On connecte les boutons niveau(langue) à leur fonction respective lorsqu'ils sont pressés
        self.vue.ui.tool_button_francais_random.clicked.connect(self.action_toolButton_francais_random_clicked)
        self.vue.ui.tool_button_anglais_random.clicked.connect(self.action_toolButton_anglais_random_clicked)
        self.vue.ui.tool_button_espagnol_random.clicked.connect(self.action_toolButton_espagnol_random_clicked)
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
        self.vue.ui.tabw_langues.currentChanged.connect(self.action_tabw_langues_currentChanged)

    # On définit la fonction qui "sauvegarde" le texte rentré
    # Elle est déclenchée à chaque fois que le texte entré dans l'éditeur change
    # Remarque : la fonction corriger n'est pas parfaite, mais repère la plupart des fautes
    def action_plain_text_dictee_textChanged (self):
        self.gif = QMovie('clap.gif')
        self.vue.ui.label_clap.setMovie(self.gif)
        self.gif.start()
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
                if result["matches"] == [] :
                    self.vue.ui.plain_fautes.setStyleSheet("color: rgb(0, 170, 0);")
                    resultText += "Aucune faute !\n"
                    resultText += "---------------------------------------------------------\n"
                    resultFautes += "Aucune faute !\n"
                else :
                    self.vue.ui.plain_fautes.setStyleSheet("color: rgb(255, 0, 0);")
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


            elif langue1 == "es" :
                resultFautes = ""
                if result["matches"] == [] :
                    self.vue.ui.plain_fautes.setStyleSheet("color: rgb(0, 170, 0);")
                    resultText += "Sin error !\n"
                    resultText += "---------------------------------------------------------\n"
                    resultFautes += "Sin error !\n"
                else :
                    self.vue.ui.plain_fautes.setStyleSheet("color: rgb(255, 0, 0);")
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

            elif langue1 == "en" :
                resultFautes = ""
                if result["matches"] == [] :
                    self.vue.ui.plain_fautes.setStyleSheet("color: rgb(0, 170, 0);")
                    resultText += "No mistake !\n"
                    resultText += "---------------------------------------------------------\n"
                    resultFautes += "No mistake !\n"
                else :
                    self.vue.ui.plain_fautes.setStyleSheet("color: rgb(255, 0, 0);")
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
                        
            resultText += '---------------------------------------------------------\n'

            self.vue.ui.plain_correction_dictee.setPlainText(resultText)
            self.vue.ui.label_note_apparait.setText(str(20-note_boucle)+str("/20"))
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
                text_dictee = self.vue.ui.plain_text_dictee.toPlainText()
                self.vue.ui.plain_text_dictee.deleteLater()
                # Après, elle transforme le plain en browser (non éditable) en le supprimant puis remplaçant
                # afin de pouvoir mettre en rouge les fautes détectées par la fonction corriger
                self.vue.ui.browser_text_dictee = QtWidgets.QTextBrowser()
                self.vue.ui.browser_text_dictee.setObjectName("browser_text_dictee")
                self.vue.ui.gridLayout_3.addWidget(self.vue.ui.browser_text_dictee, 10, 0, 1, 1)
                self.vue.ui.browser_text_dictee.setText(text_dictee)
                # ici pour enabled (False)


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
            self.vue.ui.pb_ponctuation1.show()
            self.vue.ui.pb_ponctuation2.show()
        else:
            self.vue.ui.pb_accent1.hide()
            self.vue.ui.pb_accent2.hide()
            self.vue.ui.pb_accent3.hide()
            self.vue.ui.pb_accent4.hide()
            self.vue.ui.pb_ponctuation1.hide()
            self.vue.ui.pb_ponctuation2.hide()
        if self.vue.ui.tabw_langues.currentIndex () == 0:
            self.model.current_langue = langue_francais_text
        elif self.vue.ui.tabw_langues.currentIndex () == 1:
            self.model.current_langue = langue_anglais_text
        else:
            self.model.current_langue = langue_espagnol_text


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

                
    # Cette fonction permet, lorsque l'utilisateur quitte la fenêtre, d'arrêter un audio en cours si tel est le cas
    def action_quitter (self):
        if self.sound_status != "stopped" :
            self.action_pb_stop_clicked ()
        sys.exit ()
        return


    # Les fonctions qui suivent permettent de définir la langue et le niveau en cours pour pouvoir ensuite jouer l'audio correspondant
    def action_toolButton_francais_random_clicked(self):
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

    def action_toolButton_anglais_random_clicked (self):
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

    def action_toolButton_espagnol_random_clicked (self):
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
