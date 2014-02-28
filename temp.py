__author__ = 'm'

import sys
from PySide import QtGui
from PySide import QtCore


class ButtonBlock(QtGui.QWidget):

    def __init__(self, *args):
        super(ButtonBlock, self).__init__()
        grid = QtGui.QGridLayout()
        names = ('One', 'Two', 'Three', 'Four', 'Five',
                 'Six', 'Seven', 'Eight', 'Nine', 'Ten')
        for i, name in enumerate(names):
            button = QtGui.QPushButton(name, self)
            button.clicked.connect(self.make_calluser(name))
            row, col = divmod(i, 5)
            grid.addWidget(button, row, col)
        self.setLayout(grid)

    def make_calluser(self, name):
        def calluser():
            print(name)
        return calluser

app = QtGui.QApplication(sys.argv)
tb = ButtonBlock()
tb.show()
app.exec_()