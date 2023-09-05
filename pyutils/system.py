class System:

    @staticmethod
    def read(commands, log_silent=False, timeout=10.0):
        """ Executes the given commands on the OS and returns their output.\n
            This call is always synchronous, but there is a timeout parameter for maximum wait."""
        if not log_silent:
            print("[System] Executing '" + commands + "'")
        from subprocess import PIPE, Popen
        p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
        if timeout > 0:
            p.wait(timeout)
        stdout, stderr = p.communicate()
        output = ''
        if stdout:
            output += str(stdout.decode("utf-8"))
        if stderr:
            output += '[ERROR] ' + str(stderr.decode("utf-8"))
        from .strings import String
        return String(output.strip())

    @staticmethod
    def exec(commands, ignore_output=False, log_silent=False, timeout=10.0):
        """ Executes the given commands on the OS. Doesn't expect an output.\n
        An Exception is thrown if there is an output, unless the second parameter is True. """
        if ignore_output:
            if not log_silent:
                print("[System] Executing '" + commands + "'")
            from subprocess import Popen
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
        from .strings import String
        return String(os.path.abspath(os.path.dirname(file)) + '/')

    @staticmethod
    def append_parent_syspath(file, silent=False):
        """ Appends the parent folder's path to syspath\n
        Useful to import modules from parent folder. The reference for the file being used must be given.\n
        Usage: System.append_parent_syspath(__file__)"""
        import sys
        import os
        currentpath = os.path.dirname(os.path.realpath(file))
        parentpath = os.path.dirname(currentpath)
        if not silent:
            print(f'Appending {parentpath} on sys.path')
        sys.path.append(parentpath)

    @staticmethod
    def wait_for(func, timeout=0, poll_interval=2.0):
        """ Waits for a function evaluation to return an existing result (different than None, empty, etc).\n
        The function is evaluated during each poll (2-sec intervals by default).\n
        The result is returned when it exists (function output evaluated to True).\n
        A timeout may be set (0 = None by default), so an exception is raised if there's no result up to a given time.\n
        The timeout (if used) is not precise. It has an error margin equivalent to the poll_interval used."""
        from time import sleep
        waited = 0
        while timeout == 0 or waited < timeout:
            sleep(poll_interval)
            result = func()
            if result:
                return result
            waited += poll_interval
        from subprocess import TimeoutExpired
        raise TimeoutExpired(str(func), timeout)
