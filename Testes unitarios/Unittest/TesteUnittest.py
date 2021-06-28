import os
import sys
sys.path.append(os.getcwd())

import unittest
from verificar_pangrama import verificar_pangrama

class VerificaPangramaTests(unittest.TestCase):
    def test_retorna_true_quando_frase_pangrama(self):
        frase = "Zebras caolhas de Java querem mandar fax para moça gigante de New York"

        frase_eh_pangrama = verificar_pangrama(frase)

        '''Primeiro parametro é o resultado esperado, e o segundo é o propio resultado'''
        self.assertTrue(True, frase_eh_pangrama)


    def test_retorna_falso_quando_frase_nao_eh_pangrama(self):
        frase = "Frase que não é um pangrama"
        
        frase_eh_pangrama = verificar_pangrama(frase)
        
        self.assertFalse(frase_eh_pangrama)






obj = VerificaPangramaTests()
obj.test_retorna_true_quando_frase_pangrama()