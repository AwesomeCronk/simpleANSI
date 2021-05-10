# Resources:
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
# https://bluesock.org/~willkg/dev/ansi.html
import ctypes # Used to enable VT-100 mode on windows conhost

def conhostEnableANSI():
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    