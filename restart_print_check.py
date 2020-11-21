#! /usr/bin/python3
import subprocess
import json
import time
from config import myConfig

def query_status(API=Config.X_API_KEY, IP=Config.IP_ADDRESS):
    proc = subprocess.Popen(["curl", "-s", "-H", "Content-Type: application/json", "-H", f"X-Api-Key: {API}", f"http://{IP}/api/printer"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out

def connect_printer(API=Config.X_API_KEY, IP=Config.IP_ADDRESS):
    subprocess.Popen(["curl", "-s", "-d", '{"command": "connect"}', "-H", "Content-Type: application/json", "-H", f"X-Api-Key: {API}", f"http://{IP}/api/connection"], stdout=subprocess.PIPE)
    return

print(time.strftime("%c"))

if query_status() == b"Printer is not operational":
    print("  Printer is not connected!")
    connect_printer()
    wait_time = Config.CONNECT_TIME
    print(f"  Waiting for {wait_time} seconds for connection...")
    time.sleep(wait_time)

printer_status = query_status()

if printer_status == b"Printer is not operational":
    print("  Not able to connect to printer, skipping restart.")
    exit()

state = json.loads(printer_status)["state"]["flags"]

if not state["printing"] and state["ready"]:
    # subprocess.run(["sudo", "reboot", "now"])
    print("  Restarted Pi at", time.strftime("%c"))