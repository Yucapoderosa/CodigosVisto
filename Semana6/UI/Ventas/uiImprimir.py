# Form implementation generated from reading ui file 'UI_Imprmir.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UIImprimir(object):
    def setupUi(self, UIImprimir):
        UIImprimir.setObjectName("UIImprimir")
        UIImprimir.resize(629, 300)
        self.tblFacturas = QtWidgets.QTableWidget(UIImprimir)
        self.tblFacturas.setGeometry(QtCore.QRect(10, 61, 591, 221))
        self.tblFacturas.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tblFacturas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblFacturas.setObjectName("tblFacturas")
        self.tblFacturas.setColumnCount(4)
        self.tblFacturas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblFacturas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblFacturas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblFacturas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblFacturas.setHorizontalHeaderItem(3, item)
        self.tblFacturas.horizontalHeader().setDefaultSectionSize(152)
        self.btnImprimir = QtWidgets.QPushButton(UIImprimir)
        self.btnImprimir.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnImprimir.setObjectName("btnImprimir")
        self.btnEliminarFactura = QtWidgets.QPushButton(UIImprimir)
        self.btnEliminarFactura.setGeometry(QtCore.QRect(110, 20, 151, 23))
        self.btnEliminarFactura.setObjectName("btnEliminarFactura")

        self.retranslateUi(UIImprimir)
        QtCore.QMetaObject.connectSlotsByName(UIImprimir)

    def retranslateUi(self, UIImprimir):
        _translate = QtCore.QCoreApplication.translate
        UIImprimir.setWindowTitle(_translate("UIImprimir", "Form"))
        item = self.tblFacturas.horizontalHeaderItem(0)
        item.setText(_translate("UIImprimir", "IdFactura"))
        item = self.tblFacturas.horizontalHeaderItem(1)
        item.setText(_translate("UIImprimir", "Cliente"))
        item = self.tblFacturas.horizontalHeaderItem(2)
        item.setText(_translate("UIImprimir", "Monto"))
        item = self.tblFacturas.horizontalHeaderItem(3)
        item.setText(_translate("UIImprimir", "Impuesto"))
        self.btnImprimir.setText(_translate("UIImprimir", "Imprimir"))
        self.btnEliminarFactura.setText(_translate("UIImprimir", "Eliminar factura"))
