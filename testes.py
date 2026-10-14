"""Testes automatizados das três partes. Execute: python -m unittest -v testes.py"""

import unittest
from fractions import Fraction

import parte1_conjuntos as p1
import parte2_numeros as p2
import parte3_recomendacao as p3


class TestesParte1(unittest.TestCase):
    def test_caso_geral_e_repetidos(self):
        a = p1.remover_repetidos(["1", "2", "2", "3", "4"])
        b = ["3", "4", "5", "6"]
        self.assertEqual(a, ["1", "2", "3", "4"])
        self.assertEqual(p1.uniao(a, b), ["1", "2", "3", "4", "5", "6"])
        self.assertEqual(p1.intersecao(a, b), ["3", "4"])
        self.assertEqual(p1.diferenca_simetrica(a, b), ["1", "2", "5", "6"])

    def test_vazio_iguais_disjuntos_e_contido(self):
        self.assertTrue(p1.esta_contido([], ["1", "2"]))
        self.assertFalse(p1.inclusao_propria(["1", "2"], ["1", "2"]))
        self.assertEqual(p1.intersecao(["1", "2"], ["3", "4"]), [])
        self.assertTrue(p1.inclusao_propria(["1", "2"], ["1", "2", "3"]))

    def test_complemento_e_pertinencia(self):
        universo = [str(n) for n in range(1, 11)]
        self.assertEqual(
            p1.complemento(["1", "2", "3", "4"], universo),
            ["5", "6", "7", "8", "9", "10"],
        )
        self.assertTrue(p1.pertence("3", ["1", "2", "3"]))
        self.assertFalse(p1.pertence("5", ["1", "2", "3"]))

    def test_todas_as_validacoes_nativas(self):
        a, b, universo = ["1", "2"], ["2", "3"], ["1", "2", "3"]
        manuais = p1.resultados_manuais(a, b, universo, "1")
        nativos = p1.validacao_nativa(a, b, universo, "1")
        for nome, manual in manuais.items():
            with self.subTest(operacao=nome):
                if isinstance(manual, list):
                    self.assertEqual(set(manual), nativos[nome])
                else:
                    self.assertEqual(manual, nativos[nome])


class TestesParte2(unittest.TestCase):
    CASOS = {
        "7": ["N", "Z", "Q", "R"], "-3": ["Z", "Q", "R"],
        "0": ["N", "Z", "Q", "R"], "3/4": ["Q", "R"],
        "-5/2": ["Q", "R"], "6/3": ["N", "Z", "Q", "R"],
        "0,75": ["Q", "R"], "0,(3)": ["Q", "R"],
        "2,(7)": ["Q", "R"], "1,2(5)": ["Q", "R"],
        "0,(9)": ["N", "Z", "Q", "R"], "√9": ["N", "Z", "Q", "R"],
        "√2": ["I", "R"], "√(-4)": [],
    }

    def test_classificacoes_obrigatorias(self):
        for entrada, esperado in self.CASOS.items():
            with self.subTest(entrada=entrada):
                self.assertEqual(p2.classificar_numero(entrada)["conjuntos"], esperado)

    def test_geratrizes(self):
        self.assertEqual(p2.calcular_fracao_geratriz("0,(3)")[0], Fraction(1, 3))
        self.assertEqual(p2.calcular_fracao_geratriz("2,(7)")[0], Fraction(25, 9))
        self.assertEqual(p2.calcular_fracao_geratriz("1,2(5)")[0], Fraction(113, 90))
        self.assertEqual(p2.calcular_fracao_geratriz("0,(9)")[0], Fraction(1, 1))
        self.assertEqual(p2.calcular_fracao_geratriz("-0,1(6)")[0], Fraction(-1, 6))
        self.assertEqual(p2.classificar_numero("0,(3)")["tipo"], "dízima periódica simples")
        self.assertEqual(p2.classificar_numero("1,2(5)")["tipo"], "dízima periódica composta")

    def test_invalidos(self):
        for entrada in ("", "1/0", "1//2", "1,", "0,()", "0,(3", "abc"):
            with self.subTest(entrada=entrada):
                with self.assertRaises(ValueError):
                    p2.classificar_numero(entrada)

    def test_bonus(self):
        self.assertEqual(p2.gerar_primos(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(p2.listar_divisores(36), [1, 2, 3, 4, 6, 9, 12, 18, 36])
        with self.assertRaises(ValueError):
            p2.listar_divisores(0)


class TestesParte3(unittest.TestCase):
    def test_exemplo_do_pdf(self):
        comparacoes, melhores = p3.recomendar("Ana", p3.USUARIOS_INICIAIS)
        indices = {item["nome"]: item["indice"] for item in comparacoes}
        self.assertAlmostEqual(indices["Bia"], 2 / 6)
        self.assertAlmostEqual(indices["Caio"], 2 / 5)
        self.assertEqual(melhores, ["Caio"])

    def test_sem_comuns_vazios_e_repetidos(self):
        self.assertEqual(p3.calcular_jaccard({"a"}, {"b"})[2], 0)
        self.assertEqual(p3.calcular_jaccard(set(), set())[2], 0)
        self.assertEqual(p3.normalizar_interesses("rock, rock, ROCK"), {"rock"})

    def test_empate(self):
        usuarios = {"Alvo": {"a"}, "B": {"a", "b"}, "C": {"a", "c"}}
        _, melhores = p3.recomendar("Alvo", usuarios)
        self.assertEqual(melhores, ["B", "C"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
