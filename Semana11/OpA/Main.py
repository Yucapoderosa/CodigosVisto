import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import moduloUIClientes as mClientes

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mClientes.FrmCliente()
    window.show()
    sys.exit(app.exec())

