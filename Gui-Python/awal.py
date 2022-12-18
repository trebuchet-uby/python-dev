from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def awal():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(400, 400, 400, 400)
    win.setWindowTitle("JUDUL")
    label=QtWidgets.QLabel(win)
    label.setText("HALO.....")
    label.move(200, 200)

    win.show()
    sys.exit(app.exec_())

awal()