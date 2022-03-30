import os
import PyUtils.strings as s

def ler(comandos):
    print("[SISTEMA] Executando '" + comandos + "'")                                                                                                                                                                                                                                                
    return s.String(os.popen(comandos).read().strip())

def exec(comandos):
    print("[SISTEMA] Executando '" + comandos + "'")
    os.popen(comandos)