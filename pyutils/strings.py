#!/usr/bin/env python3

class String(str):#
    def __init__(self, aString):
        self.val = aString
    def __eq__(self, other):
        return str.__eq__(self.val, other)
    def __repr__(self):
        return str.__repr__(self.val)
    def __add__(self, other):
        return String(self.val + str(other))
    def __str__(self):
        return str.__str__(self.val)
    def __hash__(self):
        return str.__hash__(self.val)
    @classmethod
    def fromdate(cls, date=None, format='%d/%m/%Y'):
        import datetime
        if not date: date=datetime.date.today()
        #if not format: format='%d/%m/%Y'
        return cls(date.strftime(format))
    @staticmethod
    def strtodate(string, format='%d/%m/%Y'):
        import datetime
        return datetime.datetime.strptime(string, format)
    @staticmethod
    def concatenar(colecao):
        """Funcao que transforma uma colecao em texto"""
        output = String("")
        if isinstance(colecao, list):
            output += "["
            for elemento in colecao:
                if len(output) > 1:
                    output += ", "
                output += elemento
            output += "]"
        else:
            if isinstance(colecao, dict):
                output += "{"
                for chave,valor in colecao.items():
                    if len(output) > 1:
                        output += ", "
                    output += chave + ": " + (valor if type(valor) not in [list, ] else String.concatenar(valor))
                output += "}"
            else:
                from itertools import groupby
                if isinstance(colecao, groupby):
                    output += "{"
                    for chave,valor in colecao:
                        if len(output) > 1:
                            output += ", "
                        output += chave + ": " + String.concatenar(list(valor))
                    output += "}"
                else:
                    raise Exception("Tipo nao conhecido para concatenacao de String: " + str(type(colecao)))
        return output
    def todate(self, format='%d/%m/%Y'):
        return String.strtodate(self.val, format)
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
    def aparar(self):
        """ Metodo mutavel semelhante a strip """
        self.val = str.strip(self)
        return self
    def replace(self, old, new):
        return String(str.replace(self, old, new))
    def trocar(self, old, new):
        """ Metodo mutavel semelhante a replace """
        self.val = str.replace(self, old, new)
        return self
    def remove_ultimos(self, n):
        return String(self[0 : len(self) - n])
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

