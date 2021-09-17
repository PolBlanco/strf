import socket
import ipaddress
from mysql.connector import errorcode
import mysql.connector
from conf import subnetting, netmask, ip

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def net_scan():
    net_ips = []
    ip = get_ip_address()
    ip_ = ip.split('.')
    global subnetting
    if subnetting != False:
        global netmask
        if len(ip) == 0:
            ip = input("Introduce tu ip de red: ")
        if len(netmask) == 0:
            netmask = input("Introduce tu máscara de red: ")
    elif ip_[0] == '192' and ip_[1] == '168':
        ip = ip[:len(ip)-len(ip_[-1])] + str(0)
        netmask = '/24'
    elif ip_[0] == '172' and ip_[1] in [str(x) for x in range(16,32)]:
        ip = ip[:len(ip) - len(ip_[-2])] + ".0.0"
        netmask = '/16'
    elif ip_[0] == '10':
        ip = "10.0.0.0"
        netmask = '/8'
    net = ipaddress.IPv4Network(ip + netmask)
    for add in net:
        net_ips.append(add)
    return net_ips

def scan_servers(ips):
    servers = []
    '''for ip in ips:
        try:
            cnx = mysql.connector.connect(user='spectator',
                                          database='strf',
                                          host= str(ip),
                                          port=50000,
                                          connection_timeout=1)
            servers.append(ip)
        except mysql.connector.Error as err:
            print(err)
        else:
            cnx.close()'''
    try:
        cnx = mysql.connector.connect(user='spectator',
                                      database='strf',
                                      host=str(ips),
                                      port=50000,
                                      connection_timeout=1)
        servers.append(ips)
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.commit()
        cnx.close()
    return servers

def login(ip,p):
    cnx = mysql.connector.connect(user='spectator',
                                  database='strf',
                                  host=ip,
                                  port=50000,
                                  connection_timeout=1)
    cnx.autocommit = True
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM login{p}")
    #cursor.execute("CALL main()")
    passwd = cursor.fetchall()[0][0]
    cnx = mysql.connector.connect(user=f'p{p}',
                                  database='strf',
                                  password= passwd,
                                  host=ip,
                                  port=50000,
                                  connection_timeout=1)
    cursor = cnx.cursor()
    cursor.execute(f"UPDATE login{p} SET k = 0")
    cnx.commit()
    cnx.close()
    return passwd