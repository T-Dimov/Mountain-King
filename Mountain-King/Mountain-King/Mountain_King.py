from PyQt5.QtCore import pyqtSignal, QBasicTimer, QSize, Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                             QLCDNumber, QPushButton, QWidget, QMainWindow,
                             QStackedWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        startWidget = StartWidget(self)
        self.centralWidget.addWidget(startWidget)

        self.setWindowTitle("Mountain King")
        self.resize(210, 50)

    def host(self):
        hostWidget = HostWidget(self)
        self.centralWidget.addWidget(hostWidget)
        self.centralWidget.setCurrentWidget(hostWidget)

        self.setWindowTitle("Hosting Mountain King")
        self.resize(255, 50)


class StartWidget(QWidget):
    def __init__(self, parent=None):
        super(StartWidget, self).__init__(parent)

        hostButton = QPushButton("&Host")
        hostButton.setFocusPolicy(Qt.NoFocus)
        joinButton = QPushButton("&Client")
        joinButton.setFocusPolicy(Qt.NoFocus)

        hostButton.clicked.connect(self.parent().host)
        # joinButton.clicked.connect()

        startLayout = QGridLayout()
        startLayout.addWidget(hostButton, 0, 0)
        startLayout.addWidget(joinButton, 1, 0)

        self.setLayout(startLayout)


class HostWidget(QWidget):
    def __init__(self, parent=None):
        super(HostWidget, self).__init__(parent)

        startButton = QPushButton("&Start")
        startButton.setFocusPolicy(Qt.NoFocus)
        quitButton = QPushButton("&Quit")
        quitButton.setFocusPolicy(Qt.NoFocus)

        # startButton.clicked.connect()
        # quitButton.clicked.connect()

        hostLayout = QGridLayout()
        hostLayout.addWidget(startButton, 0, 0)
        hostLayout.addWidget(quitButton, 1, 0)

        self.setLayout(hostLayout)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
