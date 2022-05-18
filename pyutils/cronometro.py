import time

class Cronometro:
    ts = 0
    @staticmethod
    def start():
        Cronometro.ts = time.time()
    @staticmethod
    def check(texto=''):
        """Imprime quanto tempo foi transcorrido desde o ultimo check (ou desde o inicio, para o primeiro check).
        Pode receber um texto para ser impresso antes do valor numerico.
        Retorna o valor numerico com o tempo transcorrido."""
        transcorrido = time.time() - Cronometro.ts
        if texto:
            print(texto, str(transcorrido))
        Cronometro.ts = time.time()
        return transcorrido

    