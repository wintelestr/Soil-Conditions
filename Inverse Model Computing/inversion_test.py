import unittest
import sys
from PyQt5.QtWidgets import QApplication
from soil_gui import Ui_MainWindow  
from PyQt5 import  QtWidgets

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.fig1 = None  # Initialize fig1 as None in setUp.

    def test_startInversion(self):
        self.ui.pushButton_5.click()
        self.assertIsNotNone(self.ui.fig1)

    def test_saveFig(self):
        self.ui.pushButton_5.click()  # Call startInversion to ensure fig1 is available
        file_name = 'test_figure.png'
        self.ui.fig1.savefig(file_name, format="png")
        # Check if the file is successfully created
        import os
        self.assertTrue(os.path.isfile(file_name))



if __name__ == '__main__':
    unittest.main()
