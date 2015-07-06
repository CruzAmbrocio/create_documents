#coding:utf-8
import application
import mock
import sys
import unittest

class TestCase(unittest.TestCase):

    @mock.patch('application.os.path')
    @mock.patch('application.os')
    def eliminar_archivo(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        application.remove1("name_file")
        self.assertFalse(mock_os.remove.called, "No se puede eliminar este archivo")

