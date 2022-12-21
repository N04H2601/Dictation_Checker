from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from model__dictee import *
from data__dictee import *
from outils__dictee import *
from maquette_evaluation_from_ui__dictee import *

class Vue2(QtWidgets.QWidget):
    def __init__ (self, model = None):
        QtWidgets.QWidget.__init__ (self)
        self.ui = Ui_Form ()
        self.ui.setupUi (self)
        self.model = model
        self.setWindowTitle (software_name)
        self.ui.pb_accent1.hide()
        self.ui.pb_accent2.hide()
        self.ui.pb_accent3.hide()
        self.ui.pb_accent4.hide()
        self.ui.pb_accent5.hide()
        self.ui.pb_ponctuation1.hide()
        self.ui.pb_ponctuation2.hide()
        self.update ()
    

    def update (self):
        pass

        
        
        
