import unittest
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from meshCreation import Ui_MainWindow

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

    def test_create_domain_applyButton_clicked(self):
        self.ui.startX.setValue(0)
        self.ui.startY.setValue(0)
        self.ui.endX.setValue(45)
        self.ui.endY.setValue(5)
        self.ui.applyButton_1.click()
        self.assertIsNotNone(self.ui.geom)

    def test_create_mesh_applyButton_clicked(self):
        self.ui.quality.setValue(23.5)
        self.ui.area.setValue(0.5)
        self.ui.applyButton_2.click()
        self.assertIsNotNone(self.ui.canvas_mesh)


if __name__ == '__main__':
    unittest.main()