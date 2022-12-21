# Dans ce fichier je vous mets à disposition un certain nombre de fonction que j'ai développées.
# Comme par exemple la finction infoiramtion qui affiche une sous-fenêtre avec le message
# que vous lui passez (Voir
#
#
import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5 import QtWidgets, QtGui, QtCore

def qmessage_box(txt1, txt2, with_cancel_button=None):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(txt1)
    msgBox.setInformativeText(txt2)
    if with_cancel_button == None:
        msgBox.exec_()
    else:
        buttonReply = \
          QMessageBox.question(\
            msgBox, str(txt1), str(txt2), \
            QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if buttonReply == QMessageBox.Yes:
            return True
        else:
            return False

def information (message, with_cancel_button=None):
  if with_cancel_button == None:
      title = "Information"
      qmessage_box (title, message)
  else:
      buttonReply = qmessage_box("Information", message, "with_cancel_button")
      return buttonReply

# Setting text in tableWidget
def set_tablew_item_text(tablew, i, j, value):
    tablew.blockSignals(True)
    tablew.item(int(i), int(j)).setText(value)
    tablew.blockSignals(False)

def set_tablew_case_non_editable(tablew, i, j):
    state = QtCore.Qt.ItemIsEditable
    tablew.blockSignals(True)
    tablew.item(i, j).setFlags(state)
    tablew.blockSignals(False)

def set_combo_current_text(combo, texte):
    combo.blockSignals(True)
    combo.setCurrentText(texte)
    combo.blockSignals(False)

def set_combo_current_index(combo, index):
    combo.blockSignals(True)
    combo.setCurrentIndex(index)
    combo.blockSignals(False)

def set_combo_items(combo, list_of_items):
    combo.blockSignals(True)
    combo.clear()
    combo.addItems(list_of_items)
    combo.blockSignals(False)

# Setting at (i, j) position, a widget called widget in a tableWidget called tablew
def set_tablew_cellWidget(tablew, i, j, widget):
    tablew.blockSignals(True)
    tablew.setCellWidget(int(i), int(j), widget)
    tablew.blockSignals(False)

def set_cmd_button(cmd_button):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, \
                                       QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(cmd_button.sizePolicy().hasHeightForWidth())
    cmd_button.setSizePolicy(sizePolicy)
    cmd_button.setMaximumSize(QtCore.QSize(32, 16777215))
    cmd_button.setText("")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/png/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    cmd_button.setIcon(icon)
    return cmd_button

def set_checked_radio_button (rb, boolvar):
    rb.blockSignals(True)
    rb.setChecked(boolvar)
    rb.blockSignals(False)

def set_text_line_edit(le, texte):
    le.blockSignals(True)
    le.setText(texte)
    le.blockSignals(False)
