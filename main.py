import os
import shutil
import time
import sys
import subprocess as sub
from colorama import init, Fore, Back, Style

"""
Turn your RPI Pico into a bad usb.
pico-ducky is made by dbisu.


Made by: QÆZZ (QAEZZ)
View LICENSE for legal shit or something.

Enjoy this messy code...
"""

def clear():
    sub.call('clear')

def wipeConfirm():
    clear()
    print(f"{Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}Are you sure you want to WIPE your pico. EVERYTHING will be DELETED!")
    sel = input(f"\n{Fore.YELLOW}{Style.DIM}[Yes/no]").lower()
    if sel == "y":
        print(f"{Fore.RED}\"{Fore.MAGENTA}Yes{Fore.RED}\" or \"{Fore.MAGENTA}No{Fore.RED}\" is required! Not Y/n.")
        time.sleep(2)
        wipeConfirm()
    elif sel == "yes":
        pass
    elif sel == "n":
        print(f"{Fore.RED}\"{Fore.MAGENTA}Yes{Fore.RED}\" or \"{Fore.MAGENTA}No{Fore.RED}\" is required! Not Y/n.")
        time.sleep(2)
        wipeConfirm()
    elif sel == "no":
        sys.exit()
    else:
        print(f"{Fore.RED}Duh oh! Invalid response!.. NOT wiping!")
        sys.exit()

"""
CLASSES
"""

class setup:
    def __init__(self):
        init(autoreset=True)
        print("Init'd...")

    def picoDucky(self):
        self.src = "./data/code.py"
        self.pathToPico = f"/media/{self.user}/CIRCUITPY/"

        clear()
        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Setting up pico-ducky by dbisu on your pico.")
        time.sleep(0.5)
        print(f"{Style.RESET_ALL}{Fore.CYAN}{Style.BRIGHT}Sending \"{Fore.MAGENTA}{self.src}{Fore.CYAN}\" to \"{Fore.MAGENTA}{self.pathToPico}{Fore.CYAN}\".")

        try:
            shutil.copy(self.src, self.pathToPico)
        except:
            print(f"{Fore.RED}{Style.BRIGHT}Some sort of fatal error")
            sys.exit()

        print(f"{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}Sent pico-ducky file to \"{Fore.MAGENTA}{self.pathToPico}{Fore.GREEN}\"")
        time.sleep(1)

        clear()
        print(f"{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}Your pico is now all setup as a bad usb!...\nHappy PWNING!")
        sys.exit()

    def adafruitHID(self):
        self.user = os.getlogin().strip("'")
        self.src = "./data/adafruit_hid"
        self.pathToPico = f"/media/{self.user}/CIRCUITPY/lib"

        clear()
        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Setting up Adafruit's HID libray on your pico.")
        time.sleep(0.5)
        print(f"{Style.RESET_ALL}{Fore.CYAN}{Style.BRIGHT}Sending \"{Fore.MAGENTA}{self.src}{Fore.CYAN}\" to \"{Fore.MAGENTA}{self.pathToPico}{Fore.CYAN}\".")

        try:
            self.dirname = os.path.basename(self.src)
            self.pathToPico = os.path.join(self.pathToPico, self.dirname)
            shutil.copytree(self.src, self.pathToPico)
        except FileNotFoundError:
            print(f"{Fore.RED}{Style.BRIGHT}Directory does not exist! Did you plug it in? Is it showing in your file explorer?")
            sys.exit()
        except KeyboardInterrupt:
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            sys.exit()
        except:
            print(f"{Fore.RED}{Style.RED}Some sort of fatal error")
            sys.exit()
        
        print(f"{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}Sent Adafruit's HID library folder to \"{Fore.MAGENTA}{self.pathToPico}{Fore.GREEN}\"")

    def circuitPython(self):
        self.user = os.getlogin().strip("'")

        self.pathToPico = f"/media/{self.user}/RPI-RP2/"

        self.src = "./data/circuitPy_pico_enUS_7.2.5.uf2"

        clear()
        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Setting up CircuitPython for your Raspberry Pi Pico.")
        time.sleep(0.5)
        print(f"{Style.RESET_ALL}{Fore.CYAN}{Style.BRIGHT}Sending \"{Fore.MAGENTA}{self.src}{Fore.CYAN}\" to \"{Fore.MAGENTA}{self.pathToPico}{Fore.CYAN}\".")

        try:
            shutil.copy(self.src, self.pathToPico)
        except FileNotFoundError:
            print(f"{Fore.RED}Directory does not exist! Did you plug it in? Is it showing in your file explorer?")
            sys.exit()
        except KeyboardInterrupt:
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            sys.exit()
        except:
            print(f"{Fore.RED}{Style.BRIGHT}Some sort of fatal error!")

        print(f"{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}Sent CircuitPy's .uf2 file to \"{Fore.MAGENTA}{self.pathToPico}{Fore.GREEN}\"")
        time.sleep(1)

        input(f"\n{Style.RESET_ALL}{Fore.YELLOW}{Style.BRIGHT}Please remount your pico...\n{Style.DIM}Press enter once done so.")

    def questionare(self):
        self.user = os.getlogin().strip("'")

        self.pathToPico = f"/media/{self.user}/RPI-RP2/"

        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Is your pico mounted onto your system?")
        self.sel = input(f"\n{Fore.YELLOW}{Style.DIM}[Y/n]").lower()
        if self.sel == "y":
            pass
        elif self.sel == "yes":
            pass
        elif self.sel == "n":
            print(f"{Fore.RED}Please mount your pico.")
            sys.exit()
        elif self.sel == "no":
            sys.exit()
        else:
            print(f"{Fore.RED}Duh oh! Invalid response!..")
            print(f"{Fore.RED}{Style.DIM}Please mount your pico.")
            sys.exit()

        clear()
        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Is this the correct path to your Raspberry Pi Pico?\n\"{Fore.MAGENTA}{self.pathToPico}{Fore.BLUE}\"")
        self.sel = input(f"\n{Fore.YELLOW}{Style.DIM}[Y/n]").lower()
        if self.sel == "y":
            pass
        elif self.sel == "yes":
            pass
        elif self.sel == "n":
            sys.exit()
        elif self.sel == "no":
            sys.exit()
        else:
            print(f"{Fore.RED}Duh oh! Invalid response!..")
            sys.exit()
    

"""
WIPE CLASS
"""

class wipe:
    def __init__(self):
        init(autoreset=True)
        print("Init'd...")

    def wipe(self):
        clear()
        print(f"{Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}Nuking your Raspberry Pi Pico!..")
        time.sleep(0.5)
        print(f"{Fore.CYAN}{Style.BRIGHT}Sending \"{Fore.MAGENTA}{self.src}{Fore.CYAN}\" to \"{Fore.MAGENTA}{self.pathToPico}{Fore.CYAN}\".")

        try:
            shutil.copy(self.src, self.pathToPico)
        except FileNotFoundError:
            print(f"{Fore.RED}{Style.BRIGHT}Directory does not exist! Did you plug it in? Is it showing in your file explorer?")
            sys.exit()
        except KeyboardInterrupt:
            print(f"{Fore.GREEN}{Style.BRIGHT}Goodbye!")
            sys.exit()
        except:
            print(f"{Fore.RED}{Style.BRIGHT}Some sort of fatal error")

        print(f"{Fore.GREEN}{Style.BRIGHT}Please wait for the pico's LED to flash signifying that the wipe has completed.")
        sys.exit()

    def questionare(self):
        clear()
        self.user = os.getlogin().strip("'")

        self.pathToPico = f"/media/{self.user}/RPI-RP2/"

        input(f"""{Style.RESET_ALL}{Style.BRIGHT}Please unplug your pico and do the following...{Style.DIM}
...Hold down the BOOT SEL button
...Plug in your pico
...Release the BOOT SEL button
...Mount your pico onto your system

{Style.RESET_ALL}Press enter once done...
    """)

        clear()
        print(f"{Fore.BLUE}{Style.BRIGHT}Is your pico mounted onto your system?")
        self.sel = input(f"\n{Fore.YELLOW}{Style.DIM}[Y/n]").lower()
        if self.sel == "y":
            pass
        elif self.sel == "yes":
            pass
        elif self.sel == "n":
            print(f"{Fore.RED}Please mount your pico.")
            sys.exit()
        elif self.sel == "no":
            sys.exit()
        else:
            print(f"{Fore.RED}Duh oh! Invalid response!..")
            print(f"{Fore.RED}Please mount your pico.")
            sys.exit()
        

        clear()
        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Is this the correct path to your Raspberry Pi Pico?\n\"{Fore.MAGENTA}{self.pathToPico}{Fore.BLUE}\"")
        self.sel = input(f"\n{Fore.YELLOW}{Style.DIM}[Y/n]").lower()
        if self.sel == "y":
            pass
        elif self.sel == "yes":
            pass
        elif self.sel == "n":
            sys.exit()
        elif self.sel == "no":
            sys.exit()
        else:
            print(f"{Fore.RED}Duh oh! Invalid response!..")
            sys.exit()

        self.src = "./data/nuke/flash_nuke.uf2"

        wipeConfirm()



if __name__ == "__main__":
    init(autoreset=True)
    setup = setup()
    wipe = wipe()
    clear()
    sel = input(f"{Fore.BLUE}{Style.BRIGHT}Would you like to setup({Fore.MAGENTA}1{Fore.BLUE}) or wipe({Fore.MAGENTA}3{Fore.BLUE}) your pico...\n{Fore.YELLOW}{Style.DIM}> ")
    if sel == '1':
        clear()
        setup.questionare()
        setup.circuitPython()
        setup.adafruitHID()
        setup.picoDucky()
    elif sel == '3':
        clear()
        wipe.questionare()
        wipe.wipe()
    else:
        print(f'{Fore.RED}Duh oh! Invalid response!')
        sys.exit()
else:
    print(f"{Fore.RED}{Style.BRIGHT}__name__ != \"__main__\"")
    sys.exit()
