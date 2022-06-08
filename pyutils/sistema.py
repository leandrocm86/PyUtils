from subprocess import PIPE, Popen
from .strings import String

class Sistema:
    @staticmethod
    def ler(comandos, log_silent=False, timeout=10):
        """ Executa os dados comandos no SO e retorna a saida deles no tipo pyutils.String\n
            Esta chamada eh sempre sincrona, devido ao metodo communicate() que recupera a saida,\n
            mas existe um parametro opcional de timeout para configurar a espera maxima."""
        if not log_silent:
            print("[SISTEMA] Executando '" + comandos + "'")
        p = Popen(comandos, shell=True, stdout=PIPE, stderr=PIPE)
        if timeout > 0:
            p.wait(timeout)
        stdout, stderr = p.communicate()
        saida = ''
        if stdout:
            saida += str(stdout.decode("utf-8"))
        if stderr:
            saida += '[ERRO] ' + str(stderr.decode("utf-8"))
        return String(saida.strip())

    @staticmethod
    def exec(comandos, ignora_saida=False, log_silent=False, timeout=10):
        """ Executa os dados comandos no SO. Nao espera retorno (saida).\n
        Se houver alguma saida, havera Exception, a menos que haja um segundo parametro True. """
        if ignora_saida:
            if not log_silent:
                print("[SISTEMA] Executando '" + comandos + "'")
            p = Popen(comandos, shell=True)
            if timeout > 0:
                p.wait(timeout)
        else:
            saida = Sistema.ler(comandos, log_silent, timeout)
            if saida and saida.strip():
                raise Exception("Retorno inesperado para sistema.exec():", saida)
    
    @staticmethod
    def execAsync(comandos, log_silent=False):
        """ Executa um comando sem travar a thread esperando pelo retorno.\n 
        Para isso, nao eh possivel verificar a saida da execucao e nem definir um timeout."""
        Sistema.exec(comandos, True, log_silent, 0)
    
    @staticmethod
    def file_path(file):
        """ Retorna o diretorio completo do arquivo passado como parametro.\n
        Para saber o diretorio corrente do script em execucao, executar Sistema.file_path(__file__)"""
        import os
        return os.path.abspath(os.path.dirname(file)) + '/'
    