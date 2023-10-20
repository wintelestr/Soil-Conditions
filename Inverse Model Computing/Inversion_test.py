import unittest
from soil_condition_visual import Ui_MainWindow  # Import the class containing startInversion method
import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert
import matplotlib.pyplot as plt
import numpy as np
import pygimli as pg
import pygimli.meshtools as mt
from pygimli.physics import ert

import unittest
import sys
from PyQt5.QtWidgets import QApplication

class TestStartInversion(unittest.TestCase):
    def setUp(self):
        # Create an application instance and test main window
        self.app = QApplication(sys.argv)
        self.main_window = Ui_MainWindow()  # Replace with the actual name of test main window class

    def tearDown(self):
        # Clean up resources
        self.app.quit()

    def test_startInversion(self):
        file_to_convert = '/Users/mac/Desktop/MITUWA/Third_semester/Capstone/deliverable3/Soil-Conditions/Main/test2/GN_2022-07-09.txt'
        mgr = ert.ERTManager(file_to_convert, verbose=True, debug=True)


        # Create an instance of testClass
        test_instance = Ui_MainWindow()

        # Set up necessary attributes for the instance
        test_instance.spinBox_Iterations.setValue(6)
        test_instance.spinBox_Lambda.setValue(2)
        test_instance.spinBox_dPhi.setValue(2)
        geom = pg.meshtools.createWorld(start=[0, 0], end=[47, -8], worldMarker=False)
        test_instance.geom = geom
        mesh = mt.createMesh(self.geom, quality=33.5, area=0.5, smooth=True)
        test_instance.mesh = mesh

        # Call the method to be tested
        test_instance.startInversion()

        # Assertions to check if the methods were called correctly
        mgr.invert.assert_called_once_with(mesh=mesh, lam=2, maxIter=6, dPhi=2, CHI1OPT=5, Verbose=True)
        mgr.assert_called_once_with("result_res.jpg")
        self.main_window.startInversion()
        self.assertIsNotNone(self.main_window.Storage)
        self.assertIsNotNone(self.main_window.fig1)

if __name__ == '__main__':
    unittest.main()


