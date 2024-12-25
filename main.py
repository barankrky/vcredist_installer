import os
import redist_manager as rm

title = """--------------------------------------------------------------------------------
  Microsoft Visual C++ Runtimes All-in-One Installer by barankrky 
  https://github.com/barankrky/vcredist_installer 
--------------------------------------------------------------------------------
"""

if __name__ == '__main__':
    os.system("title Microsoft Visual C++ Runtimes All-in-One Installer by barankrky : Last Update = November 2024")
    os.system('cls')
    print(title)
    rm.start()