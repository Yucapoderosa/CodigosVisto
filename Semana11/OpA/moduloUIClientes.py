import traceback
import mysql

from uiCliente import *
from moduloEntidades import Cliente
import moduloGestionBD as BD
from PyQt6 import QtWidgets

class FrmCliente(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_frmClientes()
        self.ui.setupUi(self)
        self.objCliente = None       
        self.inicilizarControles()
        self.cargarClientes()
        self.habilitarControles(False)   
        self.modoPantalla = 'X'    
        self.ui.btnNuevo.setText("Nuevo")  
        self.ui.btnGuardar.setEnabled(False)
        self.ui.btnNuevo.clicked.connect(lambda: self.establecerModoPantalla(self.ui.btnNuevo))
        self.ui.btnModificar.clicked.connect(lambda: self.establecerModoPantalla(self.ui.btnModificar))        
        self.ui.btnGuardar.clicked.connect(self.gestionarCliente)        
        self.ui.btnEliminar.clicked.connect(self.eliminarCliente)
        
        
        self.ui.tblClientes.clicked.connect(self.cargarDatosControles)
    
    def habilitarControles(self,seHabilita):
        self.ui.txtId.setEnabled(seHabilita)
        self.ui.txtIdentificacion.setEnabled(seHabilita)
        self.ui.txtnombre.setEnabled(seHabilita)
        self.ui.txtape1.setEnabled(seHabilita)
        self.ui.txtape2.setEnabled(seHabilita)
        self.ui.txtCantViajes.setEnabled(seHabilita)
        self.ui.txtSalario.setEnabled(seHabilita)
        self.ui.cmbGenero.setEnabled(seHabilita)
    
    def inicilizarControles(self):
        self.ui.txtId.clear()
        self.ui.txtIdentificacion.clear()
        self.ui.txtnombre.clear()
        self.ui.txtape1.clear()
        self.ui.txtape2.clear()
        self.ui.txtCantViajes.clear()
        self.ui.txtSalario.clear()
        self.ui.cmbGenero.setCurrentIndex(0)
        
    def llenarControles(self):
        self.ui.txtId.setText(str(self.objCliente.idCliente))
        self.ui.txtIdentificacion.setText(str(self.objCliente.ideCliente))
        self.ui.txtnombre.setText(str(self.objCliente.nomCliente))
        self.ui.txtape1.setText(str(self.objCliente.ape1Cliente))
        self.ui.txtape2.setText(str(self.objCliente.ape2Cliente))
        self.ui.txtCantViajes.setText(str(self.objCliente.cantViajes))
        self.ui.txtSalario.setText(str(self.objCliente.salario))
        generoIndice = 0 if str(self.objCliente.generoClien) == 'M' else 1
        self.ui.cmbGenero.setCurrentIndex(generoIndice)
        
    def cargarDatosControles(self):
        
        try:  
                  
            pos = self.ui.tblClientes.selectedItems()
            fila = pos[0].row()
            identificacion = self.ui.tblClientes.item(fila,0).text()
            rs = BD.buscarCliente(identificacion)
            if rs != None:               
                self.objCliente = Cliente()
                self.objCliente.idCliente = int(rs[0])
                self.objCliente.ideCliente = str(rs[1])
                self.objCliente.nomCliente = str(rs[2])
                self.objCliente.ape1Cliente = str(rs[3])
                self.objCliente.ape2Cliente = str(rs[4])
                self.objCliente.generoClien = str(rs[5])
                self.objCliente.cantViajes = int(rs[6])
                self.objCliente.salario = float(rs[7])
                self.llenarControles()
                
            
        except mysql.connector.Error as err:
            self.mensajesEmergentes("Error BaseDatos",'C',str(err))            
        except BaseException:
            self.mensajesEmergentes("Error General",'C',traceback.format_exc())     
  
    def eliminarCliente(self) :       
        pos = self.ui.tblClientes.selectedItems()
        if not pos:
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setWindowTitle("Eliminar registro")
            msg.setText("Seleccione un cliente.")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msgBox.setText("Desea elminar al cliente {}".format(self.ui.txtIdentificacion.text()))
        msgBox.setWindowTitle("Confirmar cliente a eliminar")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)                
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.StandardButton.Yes:            
            identificacion = self.ui.txtIdentificacion.text()
            BD.eliminarCliente(identificacion)
            self.mensajesEmergentes("Eliminación exitosa","I","Se realizó la eliminación del cliente {}".format(identificacion))                    
            self.ui.btnNuevo.setEnabled(True)
            self.ui.btnGuardar.setEnabled(False)                    
            self.ui.btnModificar.setEnabled(True)
            self.ui.btnEliminar.setEnabled(True)
            self.cargarClientes()
            self.inicilizarControles()                                
            self.habilitarControles(False)
            self.modoPantalla == 'X'
                       
       
    def establecerModoPantalla(self,oButton:QtWidgets.QPushButton):
        if oButton.text() == "Nuevo":
            self.modoPantalla = 'N'           
            self.ui.btnModificar.setEnabled(False)
            self.ui.btnEliminar.setEnabled(False)
            self.ui.btnNuevo.setEnabled(False)
            self.ui.btnGuardar.setEnabled(True)            
            self.inicilizarControles()
            self.habilitarControles(True)
            self.ui.txtId.setFocus() 
            return
        
        if oButton.text() == "Modificar":
            pos = self.ui.tblClientes.selectedItems()
            if not pos:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                msg.setWindowTitle("Modificar registro")
                msg.setText("Seleccione un cliente.")
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                return
            self.modoPantalla = 'M'
            self.ui.btnNuevo.setEnabled(False)
            self.ui.btnModificar.setEnabled(False)
            self.ui.btnEliminar.setEnabled(False)
            self.ui.btnGuardar.setEnabled(True)
            self.habilitarControles(True)
            self.ui.txtId.setEnabled(False)
            self.ui.txtIdentificacion.setEnabled(False)
            self.ui.txtnombre.setFocus()
            return
        
    def gestionarCliente(self):
        try:    
            if self.modoPantalla == 'N':                
                self.objCliente = Cliente()
                self.objCliente.idCliente = int(self.ui.txtId.text())
                self.objCliente.ideCliente = self.ui.txtIdentificacion.text()
                self.objCliente.nomCliente = self.ui.txtnombre.text()
                self.objCliente.ape1Cliente = self.ui.txtape1.text()
                self.objCliente.ape2Cliente = self.ui.txtape2.text()
                self.objCliente.cantViajes = int(self.ui.txtCantViajes.text())
                self.objCliente.salario = float(self.ui.txtSalario.text())
                indiceGenero = self.ui.cmbGenero.currentIndex()
                self.objCliente.generoClien = 'M' if indiceGenero == 0 else 'F'
                BD.registrarCliente(self.objCliente)
                self.mensajesEmergentes("Registro exitoso","I","Se realizó el registro del cliente {}".format(self.objCliente.ideCliente))
                self.cargarClientes()
                self.inicilizarControles()
                self.ui.btnNuevo.setText("Nuevo")
                self.ui.btnModificar.setEnabled(True)
                self.ui.btnEliminar.setEnabled(True)
                self.ui.btnNuevo.setEnabled(True)
                self.ui.btnGuardar.setEnabled(False)
                self.habilitarControles(False)
                self.modoPantalla == 'X'
                return    
            
            if  self.modoPantalla == 'M':
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgBox.setText("Desea modificar al cliente {}".format(self.ui.txtIdentificacion.text()))
                msgBox.setWindowTitle("Confirmar cliente a modificar")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)                
                returnValue = msgBox.exec()
                if returnValue == QtWidgets.QMessageBox.StandardButton.Yes:            
                    self.objCliente = Cliente()
                    self.objCliente.idCliente = int(self.ui.txtId.text())
                    self.objCliente.ideCliente = self.ui.txtIdentificacion.text()
                    self.objCliente.nomCliente = self.ui.txtnombre.text()
                    self.objCliente.ape1Cliente = self.ui.txtape1.text()
                    self.objCliente.ape2Cliente = self.ui.txtape2.text()
                    self.objCliente.cantViajes = int(self.ui.txtCantViajes.text())
                    self.objCliente.salario = float(self.ui.txtSalario.text())
                    indiceGenero = self.ui.cmbGenero.currentIndex()
                    self.objCliente.generoClien = 'M' if indiceGenero == 0 else 'F'
                    BD.modificarCliente(self.objCliente)
                    self.mensajesEmergentes("Actualización exitosa","I","Se realizó la actualización del cliente {}".format(self.objCliente.ideCliente))
                    self.ui.btnNuevo.setText("Nuevo")
                    self.ui.btnNuevo.setEnabled(True)
                    self.ui.btnGuardar.setEnabled(False)                    
                    self.ui.btnModificar.setEnabled(True)
                    self.ui.btnEliminar.setEnabled(True)
                    self.cargarClientes()
                    self.inicilizarControles()                                
                    self.habilitarControles(False)
                    self.modoPantalla == 'X'
                
        except mysql.connector.Error as err:
            self.mensajesEmergentes("Error BaseDatos",'C',str(err))            
        except BaseException:
            self.mensajesEmergentes("Error General",'C',traceback.format_exc())           
    
    def cargarClientes(self):
        try:
           datosClientes = BD.consultarClientes()
           self.ui.tblClientes.setRowCount(0)
           self.numFila = self.ui.tblClientes.rowCount()
           for oCl in datosClientes:
               self.ui.tblClientes.insertRow(self.numFila)
               self.ui.tblClientes.setItem(self.numFila,0,QtWidgets.QTableWidgetItem(str(oCl[1])))
               nombreCompleto = oCl[2]+" "+oCl[3]+" "+oCl[4]
               self.ui.tblClientes.setItem(self.numFila,1,QtWidgets.QTableWidgetItem(nombreCompleto))
               genero = 'Masculino' if oCl[5] == 'M' else 'Femenino'
               self.ui.tblClientes.setItem(self.numFila,2,QtWidgets.QTableWidgetItem(genero))
               self.ui.tblClientes.setItem(self.numFila,3,QtWidgets.QTableWidgetItem(str(oCl[7])))
               self.numFila += 1
           
        except mysql.connector.Error as err:
            print(str(err))
            self.mensajesEmergentes("Error BaseDatos",'C',str(err))            
        except BaseException:
            print(traceback.format_exc())
            self.mensajesEmergentes("Error General",'C',traceback.format_exc()) 
        
    def mensajesEmergentes(self,titulo,tipo,texto):
            msg = QtWidgets.QMessageBox()
            if tipo == 'C':
                msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            if tipo == 'I':
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setWindowTitle(titulo)
            msg.setText(texto)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        
        
       