from __future__ import print_function

import platform

import dicom
from qtpy import QtGui, QtCore, QtWidgets

class Inspector(QtWidgets.QTextEdit):

    def __init__(self, fname=None, parent=None):

        super(Inspector, self).__init__(parent)
        self._parent = parent
        self.setReadOnly(True)

        if fname is not None and type(fname) == str:
            self.show_header(fname)

    def show_header(self, fname, fit=True):

        try:

            text = str(dicom.read_file(fname))
            self.setText(text)
            self.setWindowTitle(fname)
            if fit:
                font = self.document().defaultFont()
                font_metrics = QtGui.QFontMetrics(font)
                text_size = font_metrics.size(0, text)
                self.resize(text_size.width() + 30, text_size.height() + 30)

        except Exception as e:

            print("Error loading DICOM data")

    def dragEnterEvent(self, e):

        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):

        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):

        if e.mimeData().hasUrls:

            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()

            # Workaround for OSx dragging and dropping
            for url in e.mimeData().urls():
                if platform.system() == 'Darwin':
                    fname = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
                else:
                    fname = str(url.toLocalFile())

            self.show_header(fname, False)

        else:

            e.ignore()
