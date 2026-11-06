# Teste de página estática

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# RF-25292: Criação de Modelos de Ata
class TesteVisualizacaoPagina(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        caminho_arquivo = os.path.abspath("pagina-modelos-ata.html")
        self.driver.get(f"file:///{caminho_arquivo}")

# Descrição: O sistema deve permitir que o usuário, com a permissão de criar Modelos de Ata, através da tela de Modelos de Atas
    def testeElementosPaginaModelosAtaExistem(self):
        elementos = {
            "titulo" : "titulo",
            "botao de cadastro de modelos" : "cadastrar-modelo-ata"
        }

        for nome, classe in elementos.items():
            with self.subTest(elemento=nome):
                encontrados = self.driver.find_elements(
                    By.CLASS_NAME, classe
                )

                self.assertTrue(
                    len(encontrados) > 0,
                    msg = f"Falha: o elemento {nome} (que deve possuir a classe \"{classe}\") não foi encontrado."
                )

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()