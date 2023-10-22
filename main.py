import time
import psutil
import getpass
from fabric import Connection, Config

#Displays the CPU & RAM usage percentages as bars
def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage /100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}% ", end="\r")

#Establish an SSH connection to a remote machine
def establish_ssh_connection():
    password = getpass.getpass("Enter your root password: ")
    #password = "azerty123456"
    configg = Config(overrides={'connect_kwargs': {'password': password}}) 
    conn = Connection("127.0.0.1", user="rrm", config=configg)
    return conn

#Gets the current memory usage percentile from an existing connection and returns it as a float
def getMemoryUsage(remoteConnection):
    memoryUsage = float(remoteConnection.run("free | grep Mem | awk '{print $3/$2 * 100.0}'", hide=True).stdout.strip("\n").replace(",","."))

    return memoryUsage

#Fetchs the current cpu usage percentile from an existing connection and returns it as a float
def getCpuUsage(remoteConnection):
    cpuUsage = float(remoteConnection.run("top -b -n2 | grep 'Cpu(s)' | awk '{print $2+$4 ""}' | tail -n1", hide=True).stdout.strip("\n").replace(",","."))

    return cpuUsage

#Displays the current resources usage
def monitor():
    remoteConnection = establish_ssh_connection()
    while True:
        display_usage(getCpuUsage(remoteConnection), getMemoryUsage(remoteConnection), 30)
        time.sleep(0.5)

#A call to run the application
monitor()