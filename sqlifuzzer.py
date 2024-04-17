import requests
from bs4 import BeautifulSoup
import urllib3
import sys
import click
from colorama import Fore, Back

# URL = "https://redtiger.labs.overthewire.org/level1.php"

links = []
inputs = []

def get_links(url, verify):
    # Get links from URL and do not check for SSL (for now)
    re = requests.get(url, verify=verify)
    soup = BeautifulSoup(re.content, 'html.parser')
    for link in soup.find_all('a'):
        links.append(link.get('href'))


def get_input(url, verify):
    # Get all input values
    re = requests.get(url, verify=verify)
    soup = BeautifulSoup(re.content, 'html.parser')
    for input in soup.find_all('input'):
        inputs.append(input.get('name'))


def url_fuzz(url, verify, wordlist):
    print(f"{Fore.WHITE}---> Fuzzing URL parameters")
    # Read fuzz parameters from the file
    f = open(wordlist, 'r')
    lines = f.readlines()

    # Append link and fuzz parameters in the URL
    for link in links:
        base = requests.get(url + link, verify=verify)
        for line in lines:
            re = requests.get(url + link + ' ' + line, verify=verify)
            print(f"{Fore.YELLOW}[*] Trying {re.url} ...")
            # Check for BOTH match from base.content and a 200 OK Status
            if re.content == base.content and re.status_code == 200:
                print(f"{Fore.GREEN}[*] Success! {re.url} works!")
            elif re.content != base.content:
                print(f"{Fore.RED}[-] Error. The response did not match the base content.")
            elif re.status_code != 200:
                print(f"{Fore.RED}[-] Error. The server sent Status Code: {Fore.MAGENTA}{re.status_code}.")
            else:
                print(f"{Fore.RED}[-] URL {re.url} not found.")


def input_fuzz():
    pass


@click.command()
@click.option('-u', '--url', help="The URL to fuzz")
@click.option('-v', '--verify', help="SSL certificate verification. Default True", default=True)
@click.option('-w', '--wordlist', help="/path/to/wordlist.txt", default="url_fuzz.txt")
def main(url, verify, wordlist):
    print(f"""{Fore.LIGHTMAGENTA_EX}


  /$$$$$$   /$$$$$$  /$$       /$$       /$$$$$$$$                                               
 /$$__  $$ /$$__  $$| $$      |__/      | $$_____/                                               
| $$  \__/| $$  \ $$| $$       /$$      | $$    /$$   /$$ /$$$$$$$$ /$$$$$$$$  /$$$$$$   /$$$$$$ 
|  $$$$$$ | $$  | $$| $$      | $$      | $$$$$| $$  | $$|____ /$$/|____ /$$/ /$$__  $$ /$$__  $$
 \____  $$| $$  | $$| $$      | $$      | $$__/| $$  | $$   /$$$$/    /$$$$/ | $$$$$$$$| $$  \__/
 /$$  \ $$| $$/$$ $$| $$      | $$      | $$   | $$  | $$  /$$__/    /$$__/  | $$_____/| $$      
|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$      | $$   |  $$$$$$/ /$$$$$$$$ /$$$$$$$$|  $$$$$$$| $$      
 \______/  \____ $$$|________/|__/      |__/    \______/ |________/|________/ \_______/|__/      
                \__/                                                                             
                                                                                                 
                                                                                                 

""")
    if verify == None or verify == True:
        print(f"{Back.RED}{Fore.WHITE}WARNING!{Back.RESET}{Fore.RED} SSL verification check is set to True. This may cause errors in the fuzzing process.")
        print(f"{Fore.YELLOW}To turn SSL verification off, use switch [-v False] in the arguments.")
    elif verify == False:
        print(f"{Back.RED}{Fore.WHITE}WARNING!{Back.RESET}{Fore.RED} SSL verification check is set to False. Suppressing SSL warnings.")
        urllib3.disable_warnings()
    else:
        print(f"{Fore.RED}Not enough arguments.")
        print(f"{Fore.LIGHTCYAN_EX}Exiting...")
        sys.exit(0)

    try:
        get_links(url, verify)
        get_input(url, verify)
        url_fuzz(url, verify, wordlist)
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTCYAN_EX} User raised keyboard interrupt.")
        print(f"{Fore.LIGHTCYAN_EX} Exiting...")
        sys.exit(0)
    except requests.exceptions.SSLError:
        print(f"{Fore.RED}SSL Verification failed. Try again with [-v False] switch.")
        print(f"{Fore.LIGHTCYAN_EX}Exiting...")
        sys.exit(0)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
