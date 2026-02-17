import socket
from urllib.parse import urlparse
import argparse


# input
def data_read(filepath):
    try:
        with open (filepath) as file:
            for line in file:
                clean_line = (line.strip())
                yield clean_line
    except FileNotFoundError: print ("No File was selected")


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
        return(f"Error: {domain} couldnt be resolved.")


# Main control
def orchester():
    parser = argparse.ArgumentParser(description="Subdomain Scanner v 0.1")
    parser.add_argument("-t","--target", required=True, help="Domain to scan (e.g., google.com)")
    parser.add_argument("-w", "--wordlist", default="names.txt", help="Path to the wordlist file")
    args = parser.parse_args()
    base_domain = clean_url(args.target)
    raw_list = data_read(args.wordlist)
    if not raw_list:
        print("Error: Wordlist is empty or could not be read.")
        return
    for line in raw_list:
        subdomain = line.strip()
        if not subdomain:
            continue
        full_target = f"{subdomain}.{base_domain}"
        ip_address = dns_check(full_target)
        if ip_address:
            print(f"Found: {full_target} -> {ip_address}")


if __name__ == "__main__":
    orchester()
