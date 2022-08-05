import time
import sys
import subprocess as sub
from colorama import init, Fore, Style
import platform as plat

import win
import nix

"""
Turn your RPI Pico into a bad usb.
pico-ducky is made by dbisu.


Made by: QÆZZ (QAEZZ)
View LICENSE for legal shit or something.

Enjoy this messy code...
"""


if __name__ == "__main__":
    init(autoreset=True)
    
    input(f"""{Style.RESET_ALL}{Style.BRIGHT}Please unplug your pico and do the following...{Style.DIM}
...Hold down the BOOT SEL button
...Plug in your pico
...Release the BOOT SEL button
...Mount your pico onto your system

{Style.RESET_ALL}Press enter once done...
    """)
    

    if plat.system().lower() == "windows":
        sub.call("cls", shell=True)
        
        print(f"You are using {Fore.BLUE}{Style.BRIGHT}Windows{Fore.RESET}{Style.RESET_ALL}\nMake sure \"{Fore.MAGENTA}pywin32{Style.RESET_ALL}\" is installed\n")

        sel = input(f"""What would you like to do?
[1] - Wipe your Pico
[2] - Add pico-ducky to your Pico
[3] - Exit
""")    
        sub.call("cls", shell=True)
        
        if sel == "1":
            """
            wipe
            """
            win.setup = win.setup()
            win.wipe = win.wipe()
            
            win.setup.getPath()
            time.sleep(2)
            
            win.wipe.questionare()
            win.wipe.wipe()
            
        
        elif sel == "2":
            """
            add pico-ducky to pico
            """
            win.setup = win.setup()
            
            win.setup.getPath()
            time.sleep(2)
            
            win.setup.questionare()
            win.setup.addCircuitPythonToPico()
            
            win.setup.getPath()
            time.sleep(2)
            
            win.setup.addAdafruitHIDToPico()
            win.setup.addPicoDuckyToPico()
        
        elif sel == "3":
            sys.exit()
        
    else:
        sub.call("clear", shell=True)
        
        print(f"You are using {Fore.BLUE}{Style.BRIGHT}{plat.system()}{Fore.RESET}{Style.RESET_ALL}\n")
        
        sel = input(f"""What would you like to do?
[1] - Wipe your Pico
[2] - Add pico-ducky to your Pico
[3] - Exit
""")    
        sub.call("clear", shell=True)
        
        if sel == "1":
            """
            wipe
            """
            nix.wipe = nix.wipe()
        
            nix.wipe.questionare()
            nix.wipe.wipe()
            
        elif sel == "2":
            """
            add pico-ducky to pico
            """
            nix.setup = nix.setup()
            
            nix.setup.questionare()
            nix.setup.addCircuitPythonToPico()
            nix.setup.addAdafruitHIDToPico()
            nix.setup.addPicoDuckyToPico()
        
        elif sel == "3":
            sys.exit()
        
        

else:
    print(f"{Fore.RED}{Style.BRIGHT}__name__ != \"__main__\"{Style.RESET_ALL}")
    print(__name__)
    sys.exit()




'''
win

    setup = setup()
    wipe = wipe()

    clear()
    
    
    input(f"""{Style.RESET_ALL}{Style.BRIGHT}Please unplug your pico and do the following...{Style.DIM}
...Hold down the BOOT SEL button
...Plug in your pico
...Release the BOOT SEL button
...Mount your pico onto your system

{Style.RESET_ALL}Press enter once done...
    """)

    clear()
    sel = input("What would you like to do?\nPlease make sure your RPI Pico is mounted!\n\n[1] Wipe\n[2] Setup Pico\n[3] Exit\n")
    clear()
    
    if sel == "1":
        setup.getPath()
        time.sleep(2)
        wipe.questionare()
        wipe.wipe()
    elif sel == "2":
        setup.getPath()
        time.sleep(2)
        
        setup.questionare()
        setup.addCircuitPythonToPico()
        
        setup.getPath()
        
        setup.addAdafruitHIDToPico()
        setup.addPicoDuckyToPico()
        
    elif sel == "3":
        sys.exit()
    else:
        print("Duh oh! Invalid response!..")
        sys.exit()
'''

'''
nix

    setup = setup()
    wipe = wipe()

    clear()
    
    
    input(f"""{Style.RESET_ALL}{Style.BRIGHT}Please unplug your pico and do the following...{Style.DIM}
...Hold down the BOOT SEL button
...Plug in your pico
...Release the BOOT SEL button
...Mount your pico onto your system

{Style.RESET_ALL}Press enter once done...
    """)

    clear()
    sel = input("What would you like to do?\nPlease make sure your RPI Pico is mounted!\n\n[1] Wipe\n[2] Setup Pico\n[3] Exit\n")
    clear()
    
    if sel == "1":
        wipe.questionare()
        wipe.wipe()
    elif sel == "2": 
        setup.questionare()
        setup.addCircuitPythonToPico()
        
        
        setup.addAdafruitHIDToPico()
        setup.addPicoDuckyToPico()
        
    elif sel == "3":
        sys.exit()
    else:
        print("Duh oh! Invalid response!..")
        sys.exit()
'''
