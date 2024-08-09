import random
import os
from colorama import Fore, init
import time

init(convert=True)
version = '1'
github_url = 'https://github.com/apkaless'
instagram = 'https://instagram.com/apkaless'
region = 'IRAQ'
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
white = Fore.WHITE
cyan = Fore.CYAN
lw = Fore.LIGHTWHITE_EX
black = Fore.BLACK
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
lib = Fore.LIGHTBLACK_EX
res = Fore.RESET

def print_banner():
    os.system('cls')
    print(rf'''{cyan}
                  █████╗ ██████╗ ██╗  ██╗ █████╗        ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
                 ██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗      ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
                 ███████║██████╔╝█████╔╝ ███████║█████╗██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
                 ██╔══██║██╔═══╝ ██╔═██╗ ██╔══██║╚════╝██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
                 ██║  ██║██║     ██║  ██╗██║  ██║      ╚██████╗██║  ██║   ██║   ██║        ██║   
                 ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝       ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    
                                                                                                                                                                                       
          
                                ⍟ {green}Version     → {lc}{version}
                                ⍟ {green}Github      → {lc}{github_url}
                                ⍟ {green}Instagram   → {lc}{instagram}
                                ⍟ {green}Region      → {lc}{region}        

''')


def enc(file):
    with open(file, encoding='utf8') as f:
        contents = f.read()
    salt = "".join(str(random.randint(0,9)) for i in range(100))
    encrypted_data = ""
    print(f'\n{green}[+] Generating Encryption Key\n')
    time.sleep(3)
    print(f'{green}[+] Encryption Progress {white}10%\n')
    time.sleep(1)
    print(f'{green}[+] Encryption Progress {white}30%\n')
    time.sleep(1)
    print(f'{green}[+] Encryption Progress {white}50%\n')
    time.sleep(1)
    print(f'{green}[+] Encryption Progress {white}100%\n')
    time.sleep(1)
    for i in range(len(contents)):
        current_letter = contents[i]
        current_number = salt[i % len(salt)]
        encrypted_data += chr(ord(current_letter) ^ ord(current_number))
    c = repr(encrypted_data)
    d = c.replace("'", "")
    buff = f"""
wopvEaTEcopFEavc = "{d}"
iOpvEoeaaeavocp = "{salt}"
oIoeaTEAcvpae = ""
for i in range(len(wopvEaTEcopFEavc)):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[i]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[i % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))
eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))
    """
    with open('stub.py', 'w', encoding='utf8') as f:
        f.write(buff)
    print(f'\n{green}[+] Encrypted And Saved To →  {white}{os.path.abspath('stub.py')}')
    input('\n')
if __name__ == '__main__':
        while True:
            print_banner()
            file = input(f'{cyan}\n↳ Py File To Encrypt {cyan}→{white}  ')
            if file: 
                enc(file)
            else:
                print(f'\n{red}[-] Please Enter A File')
                time.sleep(2)
                continue
