
import os
import sys

class Daemonize:
    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError,e:
            sys.stderr.write("Fork 1 has failed --> %d--[%s]\n" \
                             % (e.errno,e.strerror))
            sys.exit(1)

        os.chdir('/')
        #detach from terminal
        os.setsid()
        #file to be created?
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                print "Daemon process pid %d" % pid
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("Fork 2 has failed --> %d--[%s]" \
                             % (e.errno, e.strerror))
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()

#www.iplaypy.com

    def start_daemon(self):
        self.daemonize()
        self.run_daemon()

    def run_daemon(self):
        '''override'''
        pass
