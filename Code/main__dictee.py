# fichier main.py

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from model__dictee import *
from vue_copie_from_ui__dictee import *
from ctrl_vue__dictee import *


class App():
    def __init__(self):
        self.qtapp = QApplication(sys.argv)
        self.qtapp.setStyle('Fusion')
        self.qtapp.setWindowIcon(QtGui.QIcon("logo_page.png"))
        self.instantiate_all()
        self.qtapp.exec_()

    def instantiate_all(self):
        self.model = Model()
        self.vue = Vue(self.model)
        self.vue.show()
        self.ctrl = Ctrl_vue(self.model, self.vue)

        self.qtapp.aboutToQuit.connect(self.ctrl.action_quitter)


def main(args):
    myApp = App()


if __name__ == "__main__":
    main(sys.argv)
