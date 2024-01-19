import json
import urllib.request
import webbrowser
import os
import colorama
from colorama import Fore

colorama.init(autoreset=True)

try:
    R = Fore.RED
    Y = Fore.YELLOW
    G = Fore.GREEN
    CY = Fore.CYAN
    W = Fore.WHITE
    RR = Fore.LIGHTBLACK_EX
    WB = Fore.LIGHTCYAN_EX
    PP = Fore.MAGENTA
    
    path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')

    def start():
        cmd = 'mode 120,28'
        os.system(cmd)
        os.system("cls && title IP Checker")

        print(f"""{PP}
              
██╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗     
██║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝     {RR}[+] Created By Jimo{PP}
██║██╔═══╝     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗     {RR}[+] .gg/LowCost{PP}
██║██║         ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                            
  {PP}""")
    def m3():
        try:
            print(f"""
{PP}[1] {RR}Check your IP info{W}
{PP}[2] {RR}Check other IP info{W}
{PP}[3] {RR}Exit{W}
""")
            ch = int(input(f"{PP}[>] {W}"))
            if ch == 1:
                main2()
                m3()
            elif ch == 2:
                main()
                m3()
            elif ch == 3:
                print("Exit...")
                exit()
            else:
                print(f"{R}\nInvalid choice! Please try again{W}\n")
                m3()
        except ValueError:
            print(f"{R}\nInvalid choice! Please try again{W}\n")
            m3()

    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)
                print("")
                print(f"{G}[>] {RR}IP Address{PP} [>] {W}{data['query']} {W}")
                print(f"{G}[>] {RR}Org{PP}        [>] {W}{data['org']} {W}")
                print(f"{G}[>] {RR}City{PP}       [>] {W}{data['city']} {W}")
                print(f"{G}[>] {RR}Region{PP}     [>] {W}{data['regionName']} {W}")
                print(f"{G}[>] {RR}Country{PP}    [>] {W}{data['country']} {W}")
                print(f"{G}[>] {RR}Lattitude{PP}  [>] {W}{data['lat']} {W}")
                print(f"{G}[>] {RR}Longitude{PP}  [>] {W}{data['lon']} {W}")
                l = 'https://www.google.com/maps/place/' + str(data['lat']) + '+' + str(data['lon'])
                path = os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link = 'am start -a android.intent.action.VIEW -d ' + str(l)
                    pr = input(f"\n{W}Open Map link{PP} [y/n]{W} > ")
                    if pr == "y":
                        lnk = str(link) + " > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr == "n":
                        print("\nCheck another IP or exit using Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print(f"{R}\nInvalid choice! Please try again{W}\n")
                        m3()
                else:
                    pr = input(f"\n{W}Open Map link{PP} [y/n]{W} > ")
                    if pr == "y":
                        webbrowser.open(l, new=0)
                        start()
                        m3()
                    elif pr == "n":
                        print("\n")
                        start()
                        m3()
                    else:
                        print(f"{R}\nInvalid choice! Please try again{W}\n")
                        m3()
                return
            except KeyError:
                print(f"{R}\nError! Invalid IP/Website Address!\n{W}")
                m3()
        except urllib.error.URLError:
            print("\nError! Please check your internet connection!\n")
            exit()

    def main():
        u = input(f"\n{G}Enter IP Address/Website > {W}")
        if u == "":
            print("\nEnter valid IP Address/website address!")
            main()
        else:
            url = 'http://ip-api.com/json/' + u
            finder(url)

    def main2():
        url = 'http://ip-api.com/json/'
        finder(url)

    start()
    m3()
except KeyboardInterrupt:
    print("\nJimoNeverDies")