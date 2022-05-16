#!/usr/bin/env python3

from .strings import String

class TextoParseado:
    def __init__(self):
        self.elementos = dict([])
    def add(self, elemento):
        if elemento != None:
            # print("Adicionando elemento", elemento, "com chave", elemento.chave)
            self.elementos[elemento.chave] = elemento
        # else:
            # print("Pedido para adicionar elemento nulo")
    def __str__(self):
        return String.concatenar(self.elementos)
            
class ElementoParseado:
    def __init__(self):
        self.chave = String("")
        self.atributos = dict([])
    def set_chave(self, chave):
        # print("Setando chave", chave)
        self.chave = String(chave)
    def add_atributo(self, chave_atributo, valor_atributo):
        # print("Adicionando atributo", chave_atributo, "com valor", valor_atributo)
        self.atributos[chave_atributo] = String(valor_atributo)
        # self.print()
    def __str__(self):
        return String("(chave: " + self.chave + ", atributos: " + String.concatenar(self.atributos) + ")")

class Parser:
    def __init__(self):
        self.prefixo_cabecalho = ""
        self.prefixo_chave = ""
        self.prefixos_atributos = []
    def parse(self, texto):
        resultado = TextoParseado()
        proximo_elemento = None
        # print("Parseando com cabecalho", self.prefixo_cabecalho)
        for linha in texto:
            # print("Parseando linha", linha)
            if self.prefixo_cabecalho in linha:
                # print("Cabecalho encontrado:", linha)
                resultado.add(proximo_elemento)
                proximo_elemento = ElementoParseado()
            if proximo_elemento is not None:
                if self.prefixo_chave in linha:
                    proximo_elemento.set_chave(linha[(linha.find(self.prefixo_chave) + len(self.prefixo_chave)):].strip())
                else:
                    for atributo in self.prefixos_atributos:
                        if atributo in linha:
                            # print("Atributo", atributo, "encontrado no index", linha.find(atributo))
                            proximo_elemento.add_atributo(atributo, linha[(linha.find(atributo) + len(atributo)):].strip())
                       # else:
                            #print("Atributo", atributo, "nao encontrado na linha.")
            # else:
                # print("Ignorando linha...")
        resultado.add(proximo_elemento)
        return resultado


