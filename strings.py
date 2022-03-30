#!/usr/bin/env python3

from typing import Dict
from itertools import groupby

class String(str):
    def __init__(self, aString):
        self.val = aString
    def desde(self, inicio):
        return String(self.partition(inicio)[2])
    def ate(self, fim):
        return String(self.partition(fim)[0])
    def desde_incluso(self, inicio):
        return String(self.partition(inicio)[1:2])
    def ate_incluso(self, fim):
        return String(self.partition(fim)[0:1])
    def contem_todos(self, *strings):
        return all(x in self for x in strings)
    def int(self):
        return int(self)
    def strip(self):
        return String(str.strip(self))
    def __add__(self, other):
        return String(self.val + str(other))
    def remove_ultimos(self, n):
        return String(self[0 : len(self) - 2])
    def corta(self, *separador):
        return [String(s) for s in str.split(self, *separador)]
    def linhas_com(self, *strings):
        return [l for l in self.corta('\n') if all(s in l for s in strings)]
    def linha_com(self, *strings):
        linhas = self.linhas_com(*strings)
        assert(len(linhas) <= 1)
        return linhas[0] if linhas else None
    def celulas_com(self, *strings):
        return [c for c in self.corta() if all(s in c for s in strings)]
    def celula_com(self, *strings):
        celulas = self.celulas_com(*strings)
        assert(len(celulas) <= 1)
        return celulas[0] if celulas else None

# Funcao que transforma uma colecao em texto.
def concatenar(colecao):
    output = String("")
    if type(colecao) is list:
        output += "["
        for elemento in colecao:
            if len(output) > 1:
                output += ", "
            output += elemento
        output += "]"
    elif type(colecao) is dict:
        output += "{"
        for chave,valor in colecao.items():
            if len(output) > 1:
                output += ", "
            output += chave + ": " + (valor if type(valor) not in [list, Dict] else concatenar(valor))
        output += "}"
    elif type(colecao) is groupby:
        output += "{"
        for chave,valor in colecao:
            if len(output) > 1:
                output += ", "
            output += chave + ": " + concatenar(list(valor))
        output += "}"
    else:
        output += "Erro: concatenando tipo " + str(type(colecao))
    return output
