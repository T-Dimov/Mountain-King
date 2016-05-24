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

    def join(self):
        joinWidget = JoinWidget(self)
        self.centralWidget.addWidget(joinWidget)
        self.centralWidget.setCurrentWidget(joinWidget)

        self.setWindowTitle("Joining Mountain King")
        self.resize(255, 50)

class StartWidget(QWidget):
    def __init__(self, parent=None):
        super(StartWidget, self).__init__(parent)

        hostButton = QPushButton("&Host")
        hostButton.setFocusPolicy(Qt.NoFocus)
        joinButton = QPushButton("&Join")
        joinButton.setFocusPolicy(Qt.NoFocus)

        hostButton.clicked.connect(self.parent().host)
        joinButton.clicked.connect(self.parent().join)

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
        quitButton.clicked.connect(QApplication.instance().quit)

        hostLayout = QGridLayout()
        hostLayout.addWidget(startButton, 0, 0)
        hostLayout.addWidget(quitButton, 1, 0)

        self.setLayout(hostLayout)


class JoinWidget(QWidget):
    def __init__(self, parent=None):
        super(JoinWidget, self).__init__(parent)

        joinButton = QPushButton("&Join")
        joinButton.setFocusPolicy(Qt.NoFocus)
        quitButton = QPushButton("&Quit")
        quitButton.setFocusPolicy(Qt.NoFocus)

        # joinButton.clicked.connect()
        quitButton.clicked.connect(QApplication.instance().quit)

        joinLayout = QGridLayout()
        joinLayout.addWidget(joinButton, 0, 0)
        joinLayout.addWidget(quitButton, 1, 0)

        self.setLayout(joinLayout)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
