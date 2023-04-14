import os
import sys
import traceback
import asyncio

from PyQt6 import QtCore, QtGui, QtWidgets, uic

class FrmUsuario(QtWidgets.QDialog):
    def __init__(self):                
        super(FrmUsuario,self).__init__()                        
        
        self.ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.load_ui.loadUi(os.path.join(self.ui_path, "form.ui"),self)      
        
        self.textEscribir = self.findChild(QtWidgets.QPlainTextEdit,"TxtEscribir")
        self.btnEscribir = self.findChild(QtWidgets.QPushButton,"BtnCrear")
        
        self.textLeer = self.findChild(QtWidgets.QPlainTextEdit,"TxtLeer")
        self.btnLeer = self.findChild(QtWidgets.QPushButton,"BtnLeer")
        
        self.btnEscribir.clicked.connect(self.EscribirFile)
        self.btnLeer.clicked.connect(self.LecturaArchivo)        
        
    def EscribirFile(self):
        try:
            archivo = open(os.path.join(self.ui_path,"ClienteTs.txt"),'a')        
            archivo.write(self.textEscribir.toPlainText()+"\r")            
            archivo.close()
            self.textEscribir.clear()
            
        except OSError as oE:
            archivo.close()
            print(oE.strerror)
        except BaseException:
            print(traceback.format_exc())
            archivo.close()
    
    
    def LecturaArchivo(self):
        try:
            archivo = open(os.path.join(self.ui_path,"ClienteTs.txt"),'r')        
            texto = archivo.read()          
            self.textLeer.setPlainText(texto)
            archivo.close()
            
        except OSError as oE:
            archivo.close()
            print(oE.strerror)
        except BaseException:
            archivo.close() 
        

    
app = QtWidgets.QApplication(sys.argv)       
form = FrmUsuario()
form.show()

sys.exit(app.exec())
    