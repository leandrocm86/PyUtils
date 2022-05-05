import os
try:
    from strings import String
except ImportError:
    from PyUtils.strings import String

def ler(comandos):
    """ Executa os dados comandos no SO e retorna a saida deles no tipo PyUtils.strings.String """
    print("[SISTEMA] Executando '" + comandos + "'")                                                                                                                                                                                                                                                
    return String(os.popen(comandos).read().strip())

def exec(comandos, ignora_saida=False):
    """ Executa os dados comandos no SO. Nao espera retorno (saida).\n
    Se houver alguma saida, havera Exception, a menos que haja um segundo parametro True. """
    print("[SISTEMA] Executando '" + comandos + "'")
    if ignora_saida:
        os.popen(comandos)
    else:
        saida = os.popen(comandos).read()
        if saida and saida.strip():
            raise Exception("Retorno inesperado para sistema.exec():", saida)