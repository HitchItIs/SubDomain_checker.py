import socket
from urllib.parse import urlparse
import argparse
import random
import string

# input
def data_read(filepath):
    try:
        with open (filepath) as file:
            for line in file:
                clean_line = (line.strip())
                yield clean_line
    except FileNotFoundError: 
        raise FileNotFoundError (f"[!] Wordlist could not been located {filepath}")

#url_cleaner
def clean_url(target):
    if "://" not in target:
        target = "http://" + target
    parsed = urlparse(target)
    return parsed.hostname
   
#DNS check
def dns_check(domain):
    try:
        ip=socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def wildcard_check(base_domain):
    random_sub = ''.join(random.choices(string.ascii_lowercase, k=12))
    test_domain = f"{random_sub}.{base_domain}"
    result = dns_check(test_domain)  # ← nutzt deine bestehende Funktion!
    if result:
        print(f"[!] Wildcard DNS detected on {base_domain} → results may be unreliable")
        return True
    return False

# Main control
def orchester():
    parser = argparse.ArgumentParser(description="Subdomain Scanner v 0.1")
    parser.add_argument("-t","--target", required=True, help="Domain to scan (e.g., google.com)")
    parser.add_argument("-w", "--wordlist", default="names.txt", help="Path to the wordlist file")
    args = parser.parse_args()
    base_domain = clean_url(args.target)
    try:
        raw_list = data_read(args.wordlist)
        wildcard_check(base_domain)       
        for line in raw_list:
            subdomain = line.strip()
            if not subdomain:
                continue
            full_target = f"{subdomain}.{base_domain}"
            ip_address = dns_check(full_target)
            if ip_address:
                print(f"Found: {full_target} -> {ip_address}")
    except FileNotFoundError as e:
            print (e)
            return

if __name__ == "__main__":
    orchester()
