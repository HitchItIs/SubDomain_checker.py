import socket

# input
def data_read(filepath):
    try:
        with open (filepath) as file:
            data = [line.strip()for line in file if line.strip()]
        return data
    except FileNotFoundError:
        print("Error file was not found")


#url_cleaner
def clean_url(target):
    target = target.replace("https://", "").replace("http://","")
    target = target.split("/")[0]
    return target


#DNS check
def dns_check(domain):
    try:
        ip=socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return(f"Error: {domain} couldnt be resolved.")


# Main control
def orchester():
    raw_target = input("Which domain do you want to scan?")
    base_domain = clean_url(raw_target)
    raw_list =  data_read("names.txt")
    if not raw_list:
        print ("Error, try again")
        return
    for entry in raw_list:
        full_target = f"{entry}.{base_domain}"
        ip_adress = dns_check(full_target)
        print(f"Ergebnis für {full_target}: {ip_adress}")


if __name__ == "__main__":
    orchester()
