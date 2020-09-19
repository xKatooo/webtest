import requests
from bs4 import BeautifulSoup
from dire_cat import *
import os
import sys
from colorama import init
init(autoreset=True)

os.system("clear")
print ("""\033[33m
 __          __  _  _______       _   
 \ \        / / | ||__   __|     | |  
  \ \  /\  / /__| |__ | | ___ ___| |_ 
   \ \/  \/ / _ \ '_ \| |/ _ \ __| __|
    \  /\  /  __/ |_) | |  __\__ \ |_ 
     \/  \/ \___|_.__/|_|\___|___/\__|              
                                      
                                      
                                \033[32mCreado por xKatooo
                                Github.com/xKatooo

""")
print("""\033[34m
Usa este programa con precaucion y siempre en sistemas en los que tengas permiso de testearlos
""")

print ("""\033[31m
Que deseas hacer?

1) iniciar
2) salir

""")

respuestaaa = input("\033[31m> ")

if respuestaaa == "2":
    print("\033[36mOki, byeee ^-^ ")
    sys.exit()

ruta = input("\033[36mEscribe la URL de pa página a testear ej. 'github.com' : ")

print("Por favor espere un momento...")

url = 'https://who.is/whois/'+ruta
#obtiene Cookies
s = requests.Session()

re = s.get(url)

#html Texto
soup = BeautifulSoup(re.text, 'html.parser')


if soup is not None:
    print("""\033[45m
Info DeL Dominio
""")
    #entra a La Clase rawWhois De Un Div(Probablemente El Primero)
    articles = soup.find_all("div",{"class":"rawWhois"})
    #print (articles)
    
    #Buscar Adentro De article Es articles El Anterior
    
    for article in articles:
        for articleu in article.find_all("div",{"class":"rawWhois"}):
            info_cero = articleu.find("strong").getText()
            print("\033[46m"+info_cero)
            print("""
            """)
            for info_uno in articleu.find_all("div",{"class":"row"}):
                info_unoss =info_uno.find("strong").getText()
                info_doss = info_uno.find("div",{"class":"col-md-7"}).getText()
                print (info_unoss)
                print (info_doss)
                
                
                
print("""\033[45mBuscando cPanel o Un Panel De Administrador""")
print("")
print("""\033[45mPor favor espere un momento...""")

url = 'https://'+ruta
add_php = requests.get(url+admin_php)

if add_php.status_code == 200 or add_php.status_code == 503:
    print (encontrado+url+admin_php)
    
else:
    cpan_dos = requests.get(url+cpanel_dos)
    
    if cpan_dos.status_code == 200 or cpan_dos.status_code == 503:
        print (encontrado +url+cpanel_dos)
    else:
        cpan_tres = requests.get(url+cpanel_tres)
        if cpan_tres.status_code == 200 or cpan_tres.status_code == 503  :
            print (encontrado+url+cpanel_tres)
        else:
            cpan = requests.get(url+cpanel)
            if cpan.status_code == 200 or cpan.status_code == 503:
                print (encontrado+url+cpanel)
            else:
                    whms = requests.get(url+whmcs)
                    if whms.status_code == 200 or whms.status_code == 503:
                        print(encontrado+url+whmcs)
                    else:
                        print ('No Se Encontro Nada')



print ("""\033[45m
Escaneando puertos """)
print("")
rutaa = "nmap "+ruta
print("\033[45mejecutando nmap en "+ruta)
os.system(rutaa)

