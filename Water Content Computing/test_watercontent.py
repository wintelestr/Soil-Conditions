import unittest
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QGraphicsView
from ui_watercontent_computing.py import Ui_MainWindow

class TestWaterContent(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()  # Create the application window
        self.ui.setupUi(self.window)
        self.ui.result = None

    def tearDown(self):
        self.window.close()

    def test_result(self): # Test Water Content Calculation and Result Presentation
        self.ui.pushButton_12.click()
        self.assertIsNotNone(self.ui.result)

if __name__ == '__main__':
    unittest.main()
