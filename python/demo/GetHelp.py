"""import os
import sys


def main():
    LibName = "arcade"
    file = LibName+".txt"
    out = sys.stdout
    sys.stdout = open(file, "w")
    exec("help("+LibName+")")
    # help(request)
    sys.stdout.close()
    sys.stdout = out


if __name__ == "__main__":
    main()
"""


import os
import sys

out = sys.stdout
sys.stdout = open("help.txt", "w")
help(os)
sys.stdout.close()
sys.stdout = out