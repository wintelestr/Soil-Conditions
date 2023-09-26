import unittest

import unittest
from unittest.mock import Mock
from unittest.mock import patch, mock_open

class tab_switch_test(unittest.TestCase):
    def test_switch_to_preprocessing_tab(self):
        self.tabWidget_Data = Mock()
        self.switch_to_preprocessing_tab()
        self.tabWidget_Data.setCurrentIndex.assert_called_once_with(1)




class upload_file_test(unittest.TestCase):
    @patch('your_module_name.QFileDialog.getOpenFileNames', return_value=(['test_file'], ''))
    @patch('your_module_name.QFileDialog.getExistingDirectory', return_value='save_directory')
    @patch('builtins.open', new_callable=Mock)
    @patch('shutil.copy', new_callable=Mock)
    def test_open_file_dialog(self, mock_copy, mock_open, mock_get_directory, mock_get_files):
        self.listWidget_file_list = Mock()
        self.textBrowser_showdata = Mock()
        self.open_file_dialog()

        # perform assertions here based on expected side effects or interactions
        self.listWidget_file_list.clear.assert_called_once()
        self.listWidget_file_list.addItem.assert_called()
        mock_copy.assert_called_with('test_file', 'save_directory')




class data_show_Tests(unittest.TestCase):
    @patch('file.os.listdir', return_value=['filename.tx0'])
    @patch('builtins.open', new_callable=mock_open)
    def test_data_show(self, m_open, mock_listdir):
        self = YourClass()  # replace with your actual class name
        self.textBrowser_showdata = Mock()
        self.data_show()

        # perform assertions here based on expected side effects or interactions
        self.textBrowser_showdata.setPlainText.assert_called_once_with(
            '/Users/qianzhang/PycharmProjects/pythonProject1/data/2022-07-02_09-00-00.txt')


class YourClassTests(unittest.TestCase):
    def test_jump_to_next_page(self):
        obj = YourClass()  # replace with your actual class name
        self.tabWidget_Importing = Mock()
        self.jump_to_next_page()
        self.tabWidget_Importing.setCurrentIndex.assert_called_once_with(1)

    def test_jump_to_next_visualization(self):
        object = YourClass()  # replace with your actual class name
        self.tabWidget_Importing = Mock()
        obj.jump_to_next_visualization()
        obj.tabWidget_Importing.setCurrentIndex.assert_called_once_with(4)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
