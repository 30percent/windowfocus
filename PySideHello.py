__author__ = 'm'
#!/usr/bin/python
# Import PySide classes

import sys
from PySide import QtGui
from PySide import QtCore

# Create a Qt application


class SelectionWindow(QtGui.QWidget):
    def __init__(self, namelist):
        super(SelectionWindow, self).__init__()

        grid = QtGui.QGridLayout()
        x, y, w, h = 10, 200, 200, 200
        max = 1000
        self.buttons = []
        for i, name in enumerate(namelist):
            tempbut = QtGui.QPushButton(name, self)
            self.buttons.append(tempbut)
            tempbut.setCheckable(True)
            tempbut.setChecked(False)
            tempbut.clicked.connect(self._toggle_btn_cb(tempbut))
            tempbut.setMaximumWidth(max/5)
            row, col = divmod(i, 5)
            grid.addWidget(tempbut, row, col)
        retbut = QtGui.QPushButton("Return", self)
        #retbut.setFlat(True)
        retbut.setCheckable(True)
        retbut.setChecked(False)
        retbut.clicked.connect(QtCore.QCoreApplication.instance().quit)
        grid.addWidget(retbut, 1,5)
        self.setLayout(grid)
        self.setGeometry(x, y, 1000, 1000)
        self.setMaximumSize(w,h)

    def _toggle_btn_cb(self, button):
        def bt_nm():
            print "is checked: " + button.text(), button.isChecked()
        return bt_nm

    def show_and_raise(self):
        self.show()
        self.raise_()

    def get_checked(self):
        retlist = []
        for i, button in enumerate(self.buttons):
            if button.isChecked():
                print button.text()
                retlist.append(button.text())
        return retlist


def GuiStart(names):
    app = QtGui.QApplication(sys.argv)

    dem = SelectionWindow(names)
    dem.show_and_raise()

    app.exec_()
    return dem.get_checked()


if __name__ == "__main__":
    nameslist = ["Onedsaflkjd;lskajfl;kdjsa;lkjf;ldksajf;lkdjs;a", "Twodsaflkjd;lskajfl;kdjsa;lkjf;ldksajf;lkdjs;a", "Threedsaflkjd;lskajfl;kdjsa;lkjf;ldksajf;lkdjs;a", "Fourdsaflkjd;lskajfl;kdjsa;lkjf;ldksajf;lkdjs;a"]
    GuiStart(nameslist)