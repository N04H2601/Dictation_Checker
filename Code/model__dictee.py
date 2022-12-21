# MCV
# I) Model
import os 
from os.path import *

from outils__dictee import *
from data__dictee import *

# Debut JPE
class Model ():
    def __init__ (self):
        self.all_dictees = self.make_all_dictees ()
        self.current_langue = None
        self.current_niveau = None
        self.current_son = None
        self.current_dictee = None
        self.current_dictee_indice = None

    def get_corrige (self, son):
        dir_name = os.path.dirname (son)
        base_name = os.path.basename (son)
        son_name, son_extension = os.path.splitext (base_name)
        ma_liste = dir_name.split (separ)
        corrige = corriges [str(ma_liste[1])] [str(ma_liste[2])] [son_name]
        return corrige

    def make_dictee (self, langue, niveau, son):
        ''' son est le nom d'un fichier mp3 ou ogg ou autre format audio
             par exemple: audio/audio_fra/audio_fra_facile/au_village.ogg
        '''
        base_name = os.path.basename (son)
        son_name, son_extension = os.path.splitext (base_name)
        la_langue = langue
        le_niveau = niveau
        le_texte = None # le user va remplir ce champ en tapant dans palin_texte_dictee
        le_corrige = corriges [son_name]
        l_audio = son
        le_nom = son_name
        dictee = Dictee (la_langue, \
                         le_niveau, \
                         le_texte, \
                         le_corrige, \
                         l_audio, \
                         le_nom)
        return dictee

    def make_dictees (self, langue, niveau, chemin):
        dictees = []
        sons = os.listdir (chemin)
        for i in range(len(sons)):
            dictee = self.make_dictee (langue, niveau, chemin + separ + sons[i])
            dictees.append (dictee)
        return dictees

    def make_all_dictees (self):
        ''' dans le répertoire du logiciel, il y aura un répertoire audio et dedans 
            les différents répertoires audio suivant les langues fra, esp et ang.
            Puis les répertoires par niveaux.
            Chaque dictée sera une instance de la classe Dictee définie ci-après.
            all_dictees est un dictionnaire contenant 3 sous-dictionnaires.
            Chaque sous-dictionnaire contient la liste des sons situés dans un répertoire
            correspondant à une langue et un niveau donnés.
        '''
        all_dictees = {}
        all_dictees[langue_francais_text] = {}
        all_dictees[langue_espagnol_text] = {}
        all_dictees[langue_anglais_text] = {}
        # création des dictees niveau facile en fra
        chemin = rep_audio_name + separ + rep_audio_fra_name + separ + rep_audio_fra_facile_name
        all_dictees[langue_francais_text][niveau_facile_text] = \
          self.make_dictees (langue_francais_text, \
                             niveau_facile_text, \
                             chemin)
        # création des dictees niveau moyen en fra
        chemin = rep_audio_name + separ + rep_audio_fra_name + separ + rep_audio_fra_moyen_name
        all_dictees[langue_francais_text][niveau_moyen_text] = \
          self.make_dictees (langue_francais_text, \
                         niveau_moyen_text, \
                         chemin)
        # création des dictees niveau difficile en fra
        chemin = rep_audio_name + separ + rep_audio_fra_name + separ + rep_audio_fra_difficile_name
        all_dictees[langue_francais_text][niveau_difficile_text] = \
          self.make_dictees (langue_francais_text, \
                         niveau_difficile_text, \
                         chemin)
        # création des dictees niveau facile en esp
        chemin = rep_audio_name + separ + rep_audio_esp_name + separ + rep_audio_esp_facile_name
        all_dictees[langue_espagnol_text][niveau_facile_text] = \
          self.make_dictees (langue_espagnol_text, \
                         niveau_facile_text, \
                         chemin)
        # création des dictees niveau moyen en esp
        chemin = rep_audio_name + separ + rep_audio_esp_name + separ + rep_audio_esp_moyen_name
        all_dictees[langue_espagnol_text][niveau_moyen_text] = \
          self.make_dictees (langue_espagnol_text, \
                         niveau_moyen_text, \
                         chemin)
        # création des dictees niveau difficile en esp
        chemin = rep_audio_name + separ + rep_audio_esp_name + separ + rep_audio_esp_difficile_name
        all_dictees[langue_espagnol_text][niveau_difficile_text] = \
          self.make_dictees (langue_espagnol_text, \
                         niveau_difficile_text, \
                         chemin)
        # création des dictees niveau facile en ang
        chemin = rep_audio_name + separ + rep_audio_ang_name + separ + rep_audio_ang_facile_name
        all_dictees[langue_anglais_text][niveau_facile_text] = \
          self.make_dictees (langue_anglais_text, \
                         niveau_facile_text, \
                         chemin)
        # création des dictees niveau moyen en ang
        chemin = rep_audio_name + separ + rep_audio_ang_name + separ + rep_audio_ang_moyen_name
        all_dictees[langue_anglais_text][niveau_moyen_text] = \
          self.make_dictees (langue_anglais_text, \
                         niveau_facile_text, \
                         chemin)
         # création des dictees niveau difficile en ang
        chemin = rep_audio_name + separ + rep_audio_ang_name + separ + rep_audio_ang_difficile_name
        all_dictees[langue_anglais_text][niveau_difficile_text] = \
          self.make_dictees (langue_anglais_text, \
                             niveau_facile_text, \
                             chemin)
        return all_dictees
# Fin JPE


class Dictee ():
    ''' classe générale '''
    def __init__(self,\
                 langue =None, \
                 niveau = None, \
                 texte = None, \
                 corrige=None, \
                 audio = None, \
                 nom = None):
        # attributs de la classe Dictee
        self.langue = langue
        self.niveau = niveau
        self.texte = texte 
        self.corrige = corrige # 
        self.audio = audio # audio est ...
        self.nom = nom

    def corriger(texte, corrige) :
        """ fonction qui corrige et renvoie les erreurs de l'user \
            et la corrige et aussi la note pour n'importe qu'elle dictee """
        erreur = []
        note = 0
        i = 0
        texte = creer_liste_de_string(texte)
        corrige = creer_liste_de_string(corrige)

        if len(texte) == len(corrige) : # s'il y a autant de mots 

            for i in range (len(corrige)) :
                if texte[i] == corrige[i] :
                    i = i + 1
                elif texte[i] != corrige[i] :
                    erreur.append(texte[i])
                    note.append(corrige[i])
                    return(erreur)

            if erreur != [] :
                if len(erreur) == 1 :
                    erreur = " ; ".join(erreur)
                    note = " ; ".join(note)
                    print("Vous avez mal écrit le mot suivant: " + str(erreur) +  \
                          ".\nL'orthographe correcte est", note,".")
                else :
                    erreur = " ; ".join(erreur)
                    note = " ; ".join(note)
                    print("Vous avez mal écrit les mots suivants : ",erreur, \
                          ". L'orthographe correcte est", note,".")

            else :
                print("Bravo ! Vous n'avez fait aucune erreur !")
        else : # s'il n'y a pas autant de mots 
            print("Veuillez vous relire s'il vous plaît.")
        
        note = 20 -(0.5 * longueur_liste(erreur))
        print("Votre note : ", note)
        
class Dictee_fr(Dictee):
    ''' classe des dictées françaises '''
    def __init__(self):
        langue = text_francais

class Dictee_fr_facile():
    ''' classe des dictées françaises faciles '''
    def __init__(self, Dictee_fr):
        niveau = facile
        corrige = corrige_dictee_fr_facile
        audio = audio_dictee_fr_facile

class Dictee_fr_moyen():
    ''' classe dictee française moyen'''
    def __init__(self, Dictee_fr):
        niveau = moyen
        corrige = corrige_dictee_fr_moyen
        audio = audio_dictee_fr_moyen

class Dictee_fr_difficile():
    def __init__(self, Dictee_fr):
        niveau = difficile
        corrige = corrige_dictee_fr_difficile
        audio = audio_dictee_fr_difficile

class Dictee_ang():
    def __init__(self, Dictee):
        langue = anglais

class Dictee_ang_facile():
    def __init__(self, Dictee_ang):
        niveau = facile
        corrige = corrige_dictee_ang_facile
        audio = audio_dictee_ang_facile

class Dictee_ang_moyen():
    def __init__(self, Dictee_ang):
        niveau = moyen
        corrige = corrige_dictee_ang_moyen
        audio = audio_dictee_ang_moyen

class Dictee_ang_difficile():
    def __init__(self, Dictee_ang):
        niveau = difficile
        corrige = corrige_dictee_ang_difficile
        audio = audio_dictee_ang_difficile

class Dictee_esp():
    def __init__(self, Dictee):
        langue = espagnol

class Dictee_esp_facile():
    def __init__(self, Dictee_esp):
        niveau = facile
        corrige = corrige_dictee_esp_facile
        audio = audio_dictee_esp_facile

class Dictee_esp_moyen():
    def __init__(self, Dictee_esp):
        niveau = moyen
        corrige = corrige_dictee_esp_moyen
        audio = audio_dictee_esp_moyen

class Dictee_esp_difficile():
    def __init__(self, Dictee_esp) :
        niveau = difficile
        corrige = corrige_dictee_esp_difficile
        audio = audio_dictee_esp_difficile
