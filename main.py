import sys
from window import Window
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    print("starting initialize window ...")
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    print("ending initialize window ...")
    sys.exit(app.exec())
