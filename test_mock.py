#coding:utf-8
import application
import mock
import unittest

class TestCase(unittest.TestCase):

    @mock.patch('application.os.path')
    @mock.patch('application.os')

    def test_eliminar_archivo(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        application.delete("name_file")
        self.assertFalse(mock_os.remove.called, "No se puede eliminar este archivo")

    @mock.patch('application.os.path')
    @mock.patch('application.os')
    def test_eliminar_existente(self, mock_os, mock_path):
        mock_path.isfile.return_value = True
        application.delete("name_file")
        mock_os.remove.assert_called_with("name_file")