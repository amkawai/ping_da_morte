import subprocess
from wakeonlan import send_magic_packet

lista_mac = []

def get_mac_address(ip_address):
 arp_command = ['arp', '-n', ip_address]
 output = subprocess.check_output(arp_command).decode()
 mac_address = output[114:131]
 return mac_address

for i in range(1, 130):
 ip = '192.168.2.' + str(i)
 mac_address = get_mac_address(ip)
 lista_mac.append(mac_address)

def wake_on_lan():
 for mac in lista_mac:
  send_magic_packet(mac)
 
print(lista_mac)
#wake_on_lan()

hping_command = ['hping3', '-p', 80,'-V', '192.168.2.76']
output = subprocess.check_output(arp_command).decode()
