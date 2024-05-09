import requests
from bs4 import BeautifulSoup
import urllib3
import sys
import click
from colorama import Fore

# Temporarily disabling warnings
urllib3.disable_warnings()

# URL = "https://redtiger.labs.overthewire.org/level1.php"

links = []
urls = []
inputs = []

def get_links(url, verify):
    # Get links from URL and check for endpoints
    hrefs = []
    re = requests.get(url, verify=verify)
    soup = BeautifulSoup(re.content, 'html.parser')
    for link in soup.find_all('a'):
        hrefs.append(link.get('href'))
        for href in hrefs:
            if '?' in href:
                links.append(href)
            else:
                urls.append(href)


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
            else:
                print(f"{Fore.RED}[-] URL {re.url} not found.")


def input_fuzz():
    pass


@click.command()
@click.option('-u', '--url', prompt="Enter the URL to fuzz")
@click.option('-v', '--verify', prompt="Should python verify SSL certificates?", default=True)
@click.option('-w', '--wordlist', prompt="Enter the path to URL fuzzing wordlist or use default", default="url_fuzz.txt")
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
    
    try:
        get_links(url, verify)
        get_input(url, verify)
        url_fuzz(url, verify, wordlist)
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTCYAN_EX} User raised keyboard interrupt.")
        print(f"{Fore.LIGHTCYAN_EX} Exiting...")
        sys.exit(0)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()