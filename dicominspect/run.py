import sys
from qtpy import QtWidgets
from dicominspect import Inspector

def main():

    fname = sys.argv[1] if len(sys.argv) > 1 else None

    app = QtWidgets.QApplication(sys.argv)

    inspector = Inspector(fname=fname)
    inspector.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
