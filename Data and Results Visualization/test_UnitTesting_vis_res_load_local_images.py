# Unit Testing for "Visualization" Part of "final_demo.py"
# testing: "def vis_res_load_local_images(self)" from "class MyMainWindow_Vis"

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from demo import MyMainWindow_Vis

# Define a test function, taking a mocker object as an argument for mocking purposes
def test_vis_res_load_local_images(mocker):
    # Use mocker to patch (which means replace):
    # the "save_directory" variable (from the demo.py) with the value "./test data".
    # Because function works only if "save_directory" is set correctly,
    # and I put the testing images in the folder "./test data".
    mocker.patch("demo.save_directory", "./test data")

    # Create an instance of the QApplication class
    app = QtWidgets.QApplication([])
    # Create an instance of the MyMainWindow_Vis class
    window = MyMainWindow_Vis()

    # Execute "vis_res_load_local_images" function
    window.vis_res_load_local_images()

    # Verify the results
    # To check the number of items in listWidget_vis_res_pic
    # In the testing, I put 2 proper images in the testing directory
    assert window.listWidget_vis_res_pic.count() == 2, "Expected 2 items in the list"
    # If the number of items in listWidget_vis_res_pic is 2,
    # it returns:
    # "test_UnitTesting_vis_res_load_local_images.py::test_vis_res_load_local_images PASSED";
    # Otherwise it returns the error message.

# Testing result:
#
# (new) apple@192-168-1-109 demo testVis % pytest -v test_UnitTesting_vis_res_load_local_images.py
# ======================================================== test session starts ========================================================
# platform darwin -- Python 3.9.18, pytest-7.4.2, pluggy-1.3.0 -- /Users/apple/opt/anaconda3/envs/new/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/apple/Documents/demo testVis
# plugins: mock-3.11.1
# collected 1 item
#
# test_UnitTesting_vis_res_load_local_images.py::test_vis_res_load_local_images PASSED                                          [100%]
#
# ========================================================= 1 passed in 1.19s =========================================================
# (new) apple@192-168-1-109 demo testVis %
