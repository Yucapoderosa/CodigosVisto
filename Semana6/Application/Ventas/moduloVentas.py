import traceback
from  PyQt6 import QtCore,QtGui,QtWidgets
from UI.Ventas.uiFactura import Ui_UIFactura
from UI.Ventas.uiImprimir import Ui_UIImprimir
from Dominio.Ventas.Entities import Factura
from Application.Core.CoreApp import *

class FrmFactura(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_UIFactura() #La propieda ui contiene la instancia de la interfaz grafica que dibujamos
        self.ui.setupUi(self) #Esta linea dibuja la interfaz grafica
        self.ofactura = None
        self.inicializarControles()
        self.modelolista = QtGui.QStandardItemModel()
        self.ui.lstFacturas.setModel(self.modelolista)
        reg_ex = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")
        input_validator = QtGui.QRegularExpressionValidator(reg_ex, self.ui.txtMontoFactura)
        self.ui.txtMontoFactura.setValidator(input_validator)
        
        self.ui.btnCrearFactura.clicked.connect(self.btnCrearFactura_clicked_crearFactura)
    
    def inicializarControles(self):
        self.ui.dtFechaFactura.setDate(QtCore.QDate.currentDate())
        
    def btnCrearFactura_clicked_crearFactura(self):
        self.ofactura = Factura()
        self.ofactura.idfactura = self.ui.txtidfactura.text()
        self.ofactura.nombreCliente = self.ui.txtNombreCliente.text()
        self.ofactura.montofactura = float(self.ui.txtMontoFactura.text())
        self.ofactura.fechafactura = self.ui.dtFechaFactura.text()
        indiceEstado = self.ui.cmbEstado.currentIndex()
        self.ofactura.estadoFactura = 'A' if indiceEstado == 0 else 'I' # A = Activo / I = Inactivo
        itemView = (self.ofactura.idfactura+
                    " "+self.ofactura.nombreCliente+
                    " "+
                    str(self.ofactura.montofactura))
        item = QtGui.QStandardItem(itemView)
        self.modelolista.appendRow(item)       
        Persistencia.agregarFactura(self.ofactura)
        #print(self.ofactura.nombreCliente)
        
class FrmImprimir(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_UIImprimir()
        self.ui.setupUi(self)
        self.ui.btnImprimir.clicked.connect(self.imprimirFacturas)
        self.ui.btnEliminarFactura.clicked.connect(self.eliminarFactura)
        
     
    def eliminarFactura(self):
        try:
            numFacturas = self.ui.tblFacturas.rowCount()
            if numFacturas <= 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setWindowTitle("Validación")
                msg.setText("Actualmente no existen facturas registradas")
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                return
            
            filaSeleccionada = self.ui.tblFacturas.selectedItems()
            if not filaSeleccionada:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setWindowTitle("Validación")
                msg.setText("Debe seleccionar una factura por eliminar")
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()                 
            
            self.ui.tblFacturas.removeRow(filaSeleccionada[0].row())         
        except BaseException:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error general")
            msg.setText(traceback.format_exc())
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()    
        
    def imprimirFacturas(self):
        self.ui.tblFacturas.setRowCount(0)
        numfila = self.ui.tblFacturas.rowCount()
        
        for item in Persistencia.obtenerFacturas():
            self.ui.tblFacturas.insertRow(numfila)
            idfactura = QtWidgets.QTableWidgetItem(item.idfactura)
            cliente = QtWidgets.QTableWidgetItem(item.nombreCliente)
            monto = QtWidgets.QTableWidgetItem(str(item.montofactura))
            impuesto = QtWidgets.QTableWidgetItem(str(item.impuestofactura))
            self.ui.tblFacturas.setItem(numfila,0,idfactura)
            self.ui.tblFacturas.setItem(numfila,1,cliente)
            self.ui.tblFacturas.setItem(numfila,2,monto)
            self.ui.tblFacturas.setItem(numfila,3,impuesto)
            numfila += 1
            
        