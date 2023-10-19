import unittest
import os
import shutil
import tempfile
from PyQt5 import QtWidgets  # Replace with PySide2 if you're using PySide
from final_demo import Ui_MainWindow

class TestCode(unittest.TestCase):

    def setUp(self):
        # Set up a temporary directory for testing
        self.test_directory = tempfile.mkdtemp()
   
        
        # Create an instance of your Ui_MainWindow class
        self.mock_main_window = Ui_MainWindow()

    def tearDown(self):
        # Clean up the temporary directory after testing
        shutil.rmtree(self.test_directory)

    def test_open_file_dialog(self):
        # Create a mock QMainWindow object for testing
        mock_main_window = self.mock_main_window
        mock_main_window.listWidget_file_list = QtWidgets.QListWidget()
        mock_main_window.textBrowser_showdata = QtWidgets.QTextBrowser()

        # Call the open_file_dialog method
        mock_main_window.open_file_dialog()

        # Perform assertions to check if the method worked as expected
        self.assertEqual(mock_main_window.listWidget_file_list.count(), 1)
        self.assertTrue(os.path.exists(os.path.join(self.test_directory, 'test.tx0')))
        self.assertTrue(mock_main_window.textBrowser_showdata.toPlainText() != '')

    def test_data_transfer(self):
        # Create a mock QMainWindow object for testing
        mock_main_window = self.mock_main_window

        # Create a test .tx0 file in the temporary directory
        with open(os.path.join(self.test_directory, 'test.tx0'), 'w') as f:
            f.write("48# Number of electrodes\n# x z\n0     0\n1     0\n909# Number of data")

        # Call the data_transfer method
        mock_main_window.data_transfer()

        # Perform assertions to check if the method worked as expected
        self.assertTrue(os.path.exists(os.path.join(self.test_directory, 'test.txt')))

    def test_data_show(self):
        # Create a mock QMainWindow object for testing
        mock_main_window = self.mock_main_window
        mock_main_window.textBrowser_showdata = QtWidgets.QTextBrowser()

        # Create a test .txt file in the temporary directory
        with open(os.path.join(self.test_directory, 'test.txt'), 'w') as f:
            f.write("Test data")

        # Call the data_show method
        mock_main_window.data_show()

        # Perform assertions to check if the method worked as expected
        self.assertEqual(mock_main_window.textBrowser_showdata.toPlainText(), "Test data")

if __name__ == '__main__':
    unittest.main()
