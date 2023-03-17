from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Core.uiQMain import Ui_MainWindow
from Application.Ventas.moduloVentas import *

class FrmMain(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mnuFactura.triggered.connect(self.onClickMnuFactura)
        self.ui.mnuImprimir.triggered.connect(self.onClickMnuImprimir)
        self.pantalla1 = None
        self.pantalla2 = None
        
        
    def onClickMnuFactura(self):
        self.pantalla1 = FrmFactura()
        self.pantalla1.show()
        
    def onClickMnuImprimir(self):
        self.pantalla2 = FrmImprimir()
        self.pantalla2.show()    
        
    