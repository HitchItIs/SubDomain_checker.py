import socket



# input
def data_read(filepath):
    with open (filepath) as file:
        data = [line.strip()for line in file if line.strip()]
        return data




#url_cleaner
def clean_url(target):
    target = target.replace("https://", "").replace("http://","")
    target = target.split("/")[0]
    return target





#DNS check
def dns_check(domain):
    for name in data:
        full_domain= (f"{name}")
    try:
        ip=socket.gethostbyname(full_domain)
        print(f"{name} hat die ip {ip} ")
    except socket.gaierror:
        return(f"Error: {full_domain} couldnt be resolved.")








# Main control
def orchester():








   # if __name__ == "__main__":


























     


