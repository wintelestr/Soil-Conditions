

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from demo import MyMainWindow_Vis
from unittest.mock import Mock

import numpy as np


# ... 其他代码 ...

def test_apply_Vis_Res_Ani(mocker):
    mocker.patch("demo.save_directory", "./test data")
    app = QtWidgets.QApplication([])
    window = MyMainWindow_Vis()

    # Mock the return values for selected items
    # Add real files to the list widget
    window.listWidget_vis_res_pic.addItem("./test data/GN_2022-07-09_res.jpg")
    window.listWidget_vis_res_pic.addItem("./test data/GN_2022-07-02_res.jpg")

    # Select the items in the list widget
    for index in range(window.listWidget_vis_res_pic.count()):
        item = window.listWidget_vis_res_pic.item(index)
        item.setSelected(True)

    window.apply_Vis_Res_Ani()

    # Assert GIF is named correctly
    assert 'animation_' in window.viewer.gif_path
    assert '.gif' in window.viewer.gif_path

# Testing result:
#
# (new) apple@192-168-1-109 demo testVis % pytest -v test_UnitTesting_apply_Vis_Res_Ani.py
# ======================================================== test session starts ========================================================
# platform darwin -- Python 3.9.18, pytest-7.4.2, pluggy-1.3.0 -- /Users/apple/opt/anaconda3/envs/new/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/apple/Documents/demo testVis
# plugins: mock-3.11.1
# collected 1 item
#
# test_UnitTesting_apply_Vis_Res_Ani.py::test_apply_Vis_Res_Ani PASSED                                                          [100%]
#
# ========================================================= 1 passed in 1.47s =========================================================
# (new) apple@192-168-1-109 demo testVis %
