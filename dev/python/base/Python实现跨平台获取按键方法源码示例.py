
class _Getch:
    
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            try:
                self.impl = _GetchMacCarbon()
            except AttributeError:
                self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:

    def __init__(self):
        import tty, sys, termios # import termios now or else you'll get the Unix version on the Mac

    def __call__(self):

        import sys, tty, termios

        fd = sys.stdin.fileno()

        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


class _GetchMacCarbon:
    
    def __init__(self):
        import Carbon
        Carbon.Evt #see if it has this (in Unix, it doesn't)

    def __call__(self):
        import Carbon

        if Carbon.Evt.EventAvail(0x0008)[0]==0: # 0x0008 is the keyDownMask
            return ''

        else: #www.iplaypy.com

            return chr(msg & 0x000000FF)

if __name__ == '__main__': # a little test

   print 'Press a key'

   inkey = _Getch()

   import sys

   for i in xrange(sys.maxint):
      k=inkey()

      if k <> '': break

   print 'you pressed ',k

