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

    @mock.patch('application.os.path')
    @mock.patch('__builtin__.open')
    def test_crear_existente(self, builtin_create, mock_path):
        mock_path.isfile.return_value = False
        application.create("name_file")
        builtin_create.assert_called_with("name_file", "w")

    @mock.patch('application.os.path')
    @mock.patch('__builtin__.open')
    def test_verifica_existencia(self, builtin, mock_path):
        mock_path.isfile.return_value = True
        application.create("archivo_existente")
        self.assertFalse(builtin.called, "no se puede crear")