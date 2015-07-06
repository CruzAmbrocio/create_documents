#coding:utf-8
import application
import mock.patch
import sys
import unittest

class TestCase(unittest.TestCase):

    @mock.patch('application.os.path')
    @mock.patch('application.os')
    def test_eliminar_archivo_inexistente(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        application.eliminar_archivo("no_existe")
        self.assertFalse(mock_os.remove.called, "No se puede eliminar este archivo")


    @mock.patch('application.os.path')
    @mock.patch('application.os')
    def test_eliminar_archivo_existente(self, mock_os, mock_path):
        mock_path.isfile.return_value = True
        application.eliminar_archivo("si existe")
        mock_os.remove.assert_called_with("si existe")
