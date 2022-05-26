#!/usr/bin/env python3

class String(str):
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
    def __len__(self):
        return str.__len__(self.val)
    def __getitem__(self, i):
        return self.val.__getitem__(i)
    def __setitem__(self, i, v):
        self.val.__setitem__(i, v)
    def __int__(self):
        return int(self.val)
    def __float__(self):
        return float(self.val)
    @classmethod
    def fromdate(cls, date=None, format='%d/%m/%Y'):
        import datetime
        if not date: date=datetime.date.today()
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
        part = self.partition(inicio)
        return String(part[1]+part[2])
    def ate_incluso(self, fim):
        part = self.partition(fim)
        return String(part[0]+part[1])
    def desde_ultimo(self, inicio, inicio_incluso=False):
        part = self.rpartition(inicio)
        return String(part[1]+part[2]) if inicio_incluso else String(part[2]) 
    def ate_ultimo(self, fim, fim_incluso=False):
        part = self.rpartition(fim)
        return String(part[0]+part[1]) if fim_incluso else String(part[0]) 
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
    def linhas(self):
        return [String(l) for l in self.val.splitlines() if l and l.strip()]
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
    def vazia(self):
        return not self.val or not self.val.strip()
    def add(self, s, index=None):
        """ Metodo mutavel. Concatena string em dado indice """
        if index:
            self.val = self.val[:index] + s + self.val[index:]
        else: self.val += s
        return self
    def mask(self, format):
        """ Metodo mutavel. Aplica uma dada mascara.\n 
        Cada caractere da string substitui, em ordem, cada tralha (#) da mascara. \n 
        Os demais caracteres sao inseridos, se necessario. """
        assert len(format) >= len(self.val) and format.count('#') <= len(self.val)
        mask_chars = {}
        for index, c in enumerate(format):
            if c != '#':
                mask_chars[index] = c
        for index, c in mask_chars.items():
            if self[index] != c:
                self.add(c, index)
        return self