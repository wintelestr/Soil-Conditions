import unittest
import sys
from PyQt5.QtWidgets import QApplication
from soil_gui import Ui_MainWindow  # 导入您的主窗口类
from PyQt5 import  QtWidgets

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

    def tearDown(self):
        self.window.close()

    def test_startInversion(self):
        # Simulate clicking the Apply button
        self.ui.pushButton_5.click()
        # Check if something has occurred
        self.assertIsNotNone(self.ui.fig1)  # Check if a figure is created


if __name__ == '__main__':
    unittest.main()
