from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from model__dictee import *
from data__dictee import *
from outils__dictee import *
from maquette_accueil_from_ui__dictee import *

class Vue(QtWidgets.QWidget):
    def __init__ (self, model = None):
        QtWidgets.QWidget.__init__ (self)
        self.ui = Ui_Form ()
        self.ui.setupUi (self)
        self.model = model
        self.setWindowTitle (software_name)
        self.ui.plain_text_dictee.setPlaceholderText(plain_text_dictee_init_text)
        self.ui.pb_accent1.hide()
        self.ui.pb_accent2.hide()
        self.ui.pb_accent3.hide()
        self.ui.pb_accent4.hide()
        self.ui.pb_accent5.hide()
        self.ui.pb_ponctuation1.hide()
        self.ui.pb_ponctuation2.hide()
        self.update ()
    

    def update (self):
        if self.model.current_dictee != None:
            self.ui.plain_corrige_dictee.setPlainText (self.model.current_dictee.corrige)
        else :
            self.ui.plain_corrige_dictee.setPlainText ("Pas de dictée sélectionée.")
            
    def update_stop (self) :
        self.ui.label_nom_dictee_apparait.setText("")

        
        
        
