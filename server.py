#!/usr/bin/env python3

import socket
import pymysql
import json
pymysql.install_as_MySQLdb()
import MySQLdb

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

CON = MySQLdb.connect(host="localhost",user="root",password="",database="udp_protocol")

CURSOR = CON.cursor()

def save_in_db(data):
    try:
        CURSOR.execute("INSERT INTO memory (memory_rate) VALUES(%s)", data['memory'])
        CURSOR.execute("INSERT INTO cpu (cpu_rate) VALUES(%s)", data['cpu'])
        CURSOR.execute("INSERT INTO disk (disk_rate) VALUES(%s)", data['disk'])
        CURSOR.execute("INSERT INTO process (process_rate) VALUES(%s)", data['process'])
        CURSOR.execute("INSERT INTO ip_address (ip_address) VALUES(%s)", data['ip_address'])
        
        CON.commit()
    except MySQLdb.Warning as w:
        print(w)
    except MySQLdb.Error as e:
        print("Erro executando", e)
        print(e)

while True:
    data, addr = sock.recvfrom(50000) # buffer size bytes
    data_decoded = json.loads(data)
    
    if(data_decoded):
        save_in_db(data_decoded)
