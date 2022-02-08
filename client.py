#!/usr/bin/env python3
import psutil
import json
from time import time, sleep
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP


def get_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    # doesn't even have to be reachable
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
  except Exception:
    IP = '127.0.0.1'
  finally:
    s.close()
  return IP


def get_process():
  process_running = ""
  for proc in psutil.process_iter():
    processName = proc.name()
    processID = proc.pid
    process_running += str(processName) + " :: " + str(processID) + "\n"
  return process_running


def get_disk_usage():
  hdd = psutil.disk_usage('/')
  hard_disk_used = (int)(hdd.used/(2**30))
  return hard_disk_used


def send_data(memory, cpu, hard_disk_used, process_running, ip_address):
  data = {
    'memory': str(memory) + "%",
    'cpu': str(cpu) + "%",
    'disk': str(hard_disk_used) + "%",
    'process': str(process_running),
    'ip_address': str(ip_address)
  }
  result = json.dumps(data, indent = 2).encode('utf-8')
  sock.sendto(result, (UDP_IP, UDP_PORT))


while True:
  memory = psutil.virtual_memory().percent
  cpu = psutil.cpu_percent()
  hard_disk_used = get_disk_usage()
  process_running = get_process()
  ip_address = get_ip()

  send_data(
    memory,
    cpu,
    hard_disk_used,
    process_running,
    ip_address
  )
  sleep(60)
