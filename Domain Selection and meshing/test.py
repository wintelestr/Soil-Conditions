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

    # Test if clicking the button can generate a domain
    def test_create_domain_applyButton_clicked(self):
        self.ui.spinBox_startX.setValue(0)
        self.ui.spinBox_startY.setValue(5)
        self.ui.spinBox_endX.setValue(45)
        self.ui.spinBox_endY.setValue(0)
        self.ui.pushButton_domain_apply.click()
        self.assertIsNotNone(self.ui.geom)
        
    # Test if clicking the button can generate a mesh
    def test_create_mesh_applyButton_clicked(self):
        self.ui.doubleSpinBox_quality.setValue(23.5)
        self.ui.doubleSpinBox_area.setValue(0.5)
        self.ui.pushButton_domain_apply_2.click()
        self.assertIsNotNone(self.ui.canvas_mesh)

if __name__ == '__main__':
    unittest.main()
