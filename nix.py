import os
import shutil
import time
import sys
import subprocess as sub
from colorama import init, Fore, Back, Style
import json


def clear():
    sub.call('clear', shell=True)

def wipeConfirm():
    clear()
    print(f"{Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}Are you sure you want to WIPE your Pico. EVERYTHING will be DELETED!")
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

class setup:
    def __init__(self):
        init(autoreset=True)
    
    
    def questionare(self):
        clear()
        self.user = os.getlogin().strip("'")
        self.pathToPico = f"/media/{self.user}/CIRCUITPY/lib"
        

        clear()
        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Is this the correct path to your Raspberry Pi Pico?\n\"{Fore.MAGENTA}{self.pathToPico}{Fore.BLUE}\"")
        self.sel = input(f"\n{Fore.YELLOW}{Style.DIM}[Y/n]").lower()
        if self.sel == "y":
            pass
        elif self.sel == "yes":
            pass
        elif self.sel == "n":
            self.pathToPico = input(f"{Fore.MAGENTA}{Style.BRIGHT}Please enter the correct path to your Raspberry Pi Pico: {Style.RESET_ALL}").strip("'\"")
        elif self.sel == "no":
            self.pathToPico = input(f"{Fore.MAGENTA}{Style.BRIGHT}Please enter the correct path to your Raspberry Pi Pico: {Style.RESET_ALL}").strip("'\"")
        else:
            print(f"{Fore.RED}Duh oh! Invalid response!..")
            sys.exit()
    
    
    def addCircuitPythonToPico(self):
        clear()
        
        self.src = "./data/circuitPy_pico_enUS_7.2.5.uf2"
        
        
        self.user = os.getlogin().strip("'")
        
        
        self.pathToPico = f"/media/{self.user}/CIRCUITPY/lib"

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


    def addAdafruitHIDToPico(self):
        self.src = "./data/adafruit_hid"
        clear()
        
        
        self.user = os.getlogin().strip("'")
        
        
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
    
    
    def addPicoDuckyToPico(self):
        self.src = "./data/code.py"
        clear()
        
        
        self.user = os.getlogin().strip("'")
        
        
        self.pathToPico = f"/media/{self.user}/CIRCUITPY/lib"

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

        
        print(f"{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT}Your pico is now all setup as a bad usb!...\nHappy PWNING!")
        sys.exit()



"""
WIPE CLASS
"""

class wipe:
    def __init__(self):
        init(autoreset=True)


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
        
        
        self.pathToPico = f"/media/{self.user}/CIRCUITPY/lib"
        

        clear()
        print(f"{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}Is this the correct path to your Raspberry Pi Pico?\n\"{Fore.MAGENTA}{self.pathToPico}{Fore.BLUE}\"")
        self.sel = input(f"\n{Fore.YELLOW}{Style.DIM}[Y/n]").lower()
        if self.sel == "y":
            pass
        elif self.sel == "yes":
            pass
        elif self.sel == "n":
            self.pathToPico = input(f"{Fore.MAGENTA}{Style.BRIGHT}Please enter the correct path to your Raspberry Pi Pico: {Style.RESET_ALL}").strip("'\"")
        elif self.sel == "no":
            self.pathToPico = input(f"{Fore.MAGENTA}{Style.BRIGHT}Please enter the correct path to your Raspberry Pi Pico: {Style.RESET_ALL}").strip("'\"")
        else:
            print(f"{Fore.RED}Duh oh! Invalid response!..")
            sys.exit()

        self.src = "./data/nuke/flash_nuke.uf2"

        wipeConfirm()

