import unittest
from variacao01 import UtilitariosAnaliseTexto

class TestUtilitariosAnaliseTexto(unittest.TestCase):

    # Configuração inicial para cada teste, criando uma instância da classe e definindo um texto padrão
    def setUp(self):
        self.util = UtilitariosAnaliseTexto()
        self.util.texto = "A casa é bonita e a casa é grande."

    # Testa a função frequencia_palavras para verificar se a frequência das palavras está correta
    def test_frequencia_palavras(self):
        esperado = {'a': 2, 'casa': 2, 'é': 2, 'bonita': 1, 'e': 1, 'grande.': 1}
        resultado = self.util.frequencia_palavras()
        self.assertEqual(resultado, esperado)

    # Testa se a função frequencia_palavras levanta um erro quando o tipo de texto é incorreto
    def test_frequencia_palavras_tipo_errado(self):
        self.util.texto = {"a": 1, "casa": 1}
        with self.assertRaises(AttributeError):
            self.util.frequencia_palavras()
        
    # Testa a função grupos_anagramas para verificar se os anagramas são agrupados corretamente
    def test_grupos_anagramas(self):
        lista_palavras = ["amor", "roma", "carro", "orrac", "arco", "mar"]
        esperado = [['amor', 'roma'], ['carro', 'orrac'], ['arco'], ['mar']]
        resultado = self.util.grupos_anagramas(lista_palavras)
        self.assertEqual(resultado, esperado)
        
    # Testa se a função grupos_anagramas levanta um erro quando o tipo de entrada é incorreto
    def test_grupos_anagramas_tipo_errado(self):
        lista_palavras = 1
        with self.assertRaises(TypeError):
           self.util.grupos_anagramas(lista_palavras)
           
    # Testa a função prefixo_comum com uma lista de palavras e um prefixo comum
    def test_prefixo_comum(self):
        lista_palavras = ["casa", "batman", "casamento", "casual", "carro", "cachorro"]
        prefixo = "cas"
        esperado = ["casa", "casamento", "casual"]
        resultado = self.util.prefixo_comum(lista_palavras, prefixo)
        self.assertEqual(resultado, esperado)

    # Testa a função prefixo_comum com uma lista de palavras e um prefixo que não corresponde a nenhuma palavra
    def test_prefixo_comum_sem_match(self):
        lista_palavras = ["casa", "batman", "casamento", "casual", "carro", "cachorro"]
        prefixo = "xyz"
        esperado = []
        resultado = self.util.prefixo_comum(lista_palavras, prefixo)
        self.assertEqual(resultado, esperado)

    # Testa a função prefixo_comum com uma lista vazia
    def test_prefixo_comum_lista_vazia(self):
        lista_palavras = []
        prefixo = "cas"
        esperado = []
        resultado = self.util.prefixo_comum(lista_palavras, prefixo)
        self.assertEqual(resultado, esperado)

    # Testa se a função prefixo_comum levanta um erro quando o tipo de entrada é incorreto
    def test_prefixo_comum_tipo_errado(self):
        lista_palavras = 1
        prefixo = "cas"
        esperado = []
        resultado = self.util.prefixo_comum(lista_palavras, prefixo)
        self.assertEqual(resultado, esperado)

    # Testa a função prefixo_comum com um prefixo vazio
    def test_prefixo_comum_prefixo_vazio(self):
        lista_palavras = ["casa", "casamento", "casual", "carro", "cachorro"]
        prefixo = ""
        esperado = ["casa", "casamento", "casual", "carro", "cachorro"]
        resultado = self.util.prefixo_comum(lista_palavras, prefixo)
        self.assertEqual(resultado, esperado)       

    # Testa a função detectar_palavras_chave sem fornecer palavras comuns, usando o padrão
    def test_detectar_palavras_chave_sem_palavra_comum(self):
        esperado = {'casa': 2, 'bonita': 1, 'grande': 1, 'é': 2}
        resultado = self.util.detectar_palavras_chave() 
        self.assertEqual(resultado, esperado)
        
    # Testa a função detectar_palavras_chave fornecendo uma lista de palavras comuns
    def test_detectar_palavras_chave(self):
        palavras_comuns = {"a", "é", "e"}
        esperado = {'casa': 2, 'bonita': 1, 'grande': 1}
        resultado = self.util.detectar_palavras_chave(palavras_comuns)
        self.assertEqual(resultado, esperado)
        
    # Testa a função detectar_palavras_chave com um texto vazio
    def test_detectar_palavras_chave_texto_vazio(self):
        self.util.texto = ""
        esperado = {}
        resultado = self.util.detectar_palavras_chave()
        self.assertEqual(resultado, esperado)
    
    # Testa a função detectar_palavras_chave com um texto composto apenas de palavras comuns
    def test_detectar_palavras_chave_todas_comuns(self):
        self.util.texto = "de a o e do da"
        esperado = {}
        resultado = self.util.detectar_palavras_chave()
        self.assertEqual(resultado, esperado)
        
    # Testa a função fatores_primos para verificar se os fatores primos são calculados corretamente
    def test_fatores_primos(self):
        numero = 3125
        esperado = [5, 5, 5 ,5 ,5]
        resultado = self.util.fatores_primos(numero)
        self.assertEqual(resultado, esperado)

    # Testa se a função fatores_primos levanta um erro quando o tipo de entrada é incorreto
    def test_fatores_primos_tipo_errado(self):
        numero = "string teste"
        with self.assertRaises(TypeError):
            self.util.fatores_primos(numero)
        
    # Testa a função fatores_primos com um número negativo
    def test_fatores_primos_numero_negativo(self):
        numero = -1
        esperado = []
        resultado = self.util.fatores_primos(numero)
        self.assertEqual(resultado, esperado)
        
    # Testa a função fatores_primos com o número zero
    def test_fatores_primos_numero_zero(self):
        numero = 0
        esperado = []
        resultado = self.util.fatores_primos(numero)
        self.assertEqual(resultado, esperado)

    # Testa a função fatores_primos com o número um
    def test_fatores_primos_numero_um(self):
        numero = 1
        esperado = []
        resultado = self.util.fatores_primos(numero)
        self.assertEqual(resultado, esperado)
        
if __name__ == '__main__':
    unittest.main()