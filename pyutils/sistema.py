from subprocess import PIPE, Popen
from .strings import String

class Sistema:
    @staticmethod
    def ler(comandos, log_silent=False):
        """ Executa os dados comandos no SO e retorna a saida deles no tipo PyUtils.strings.String """
        if not log_silent:
            print("[SISTEMA] Executando '" + comandos + "'")
        p = Popen(comandos, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        saida = ''
        if stdout:
            saida += str(stdout.decode("utf-8"))
        if stderr:
            saida += '[ERRO] ' + str(stderr.decode("utf-8"))
        return String(saida.strip())

    @staticmethod
    def exec(comandos, ignora_saida=False, log_silent=False):
        """ Executa os dados comandos no SO. Nao espera retorno (saida).\n
        Se houver alguma saida, havera Exception, a menos que haja um segundo parametro True. """
        if not log_silent:
            print("[SISTEMA] Executando '" + comandos + "'")
        if ignora_saida:
            Popen(comandos, shell=True)
        else:
            saida = Sistema.ler(comandos, log_silent=False)
            if saida and saida.strip():
                raise Exception("Retorno inesperado para sistema.exec():", saida)
