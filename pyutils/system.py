from subprocess import PIPE, Popen
from .strings import String


class System:

    @staticmethod
    def read(commands, log_silent=False, timeout=10):
        """ Executes the given commands on the OS and returns their output.\n
            This call is always synchronous, but there is a timeout parameter for maximum wait."""
        if not log_silent:
            print("[System] Executing '" + commands + "'")
        p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
        if timeout > 0:
            p.wait(timeout)
        stdout, stderr = p.communicate()
        output = ''
        if stdout:
            output += str(stdout.decode("utf-8"))
        if stderr:
            output += '[ERROR] ' + str(stderr.decode("utf-8"))
        return String(output.strip())

    @staticmethod
    def exec(commands, ignore_output=False, log_silent=False, timeout=10):
        """ Executes the given commands on the OS. Doesn't expect an output.\n
        An Exception is thrown if there is an output, unless the second parameter is True. """
        if ignore_output:
            if not log_silent:
                print("[System] Executing '" + commands + "'")
            p = Popen(commands, shell=True)
            if timeout > 0:
                p.wait(timeout)
        else:
            output = System.read(commands, log_silent, timeout)
            if output and output.strip():
                raise Exception("Unexpected output for System.exec():", output)
    
    @staticmethod
    def exec_async(commands, log_silent=False):
        """ Execute the commands on the OS, not waiting for their output.\n 
        It's not possible to check the output, nor setting a timeout."""
        System.exec(commands, True, log_silent, 0)
    
    @staticmethod
    def file_path(file):
        """ Returns the full path of the given file.\n
        To know the current directory of the script being executed, run System.file_path(__file__)"""
        import os
        return String(os.path.abspath(os.path.dirname(file)) + '/')
    