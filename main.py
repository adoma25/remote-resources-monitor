import time
from itertools import count
import getpass
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from fabric import Connection, Config

#Displays the CPU & RAM usage percentages as bars
def display_usage(cpuUsage, memoryUsage, bars=50):
    cpuUsagePercentage = (cpuUsage / 100.0)
    cpuUsageBar = '█' * int(cpuUsagePercentage * bars) + '-' * (bars - int(cpuUsagePercentage * bars))

    memoryUsagePercentage = (memoryUsage /100.0)
    memoryUsageBar = '█' * int(memoryUsagePercentage * bars) + '-' * (bars - int(memoryUsagePercentage * bars))

    print(f"\rCPU Usage: |{cpuUsageBar}| {cpuUsage:.2f}% ", end="")
    print(f"MEM Usage: |{memoryUsageBar}| {memoryUsage:.2f}% ", end="\r")

#Establish an SSH connection to a remote machine
def establish_ssh_connection():
    host = input("Enter host ip address: ")
    port = input("Enter port number (22 is the default ssh port): ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter your root password: ")
    
    configg = Config(overrides={'connect_kwargs': {'password': password}, 'port': port})
    
    try:
        conn = Connection(host, user=username, config=configg)
    except:
        print("Something went wrong, check provided details for errors.")
        

    return conn

#Gets the current memory usage percentile from an existing connection and returns it as a float
def getMemoryUsage(remoteConnection):
    memoryUsage = float(remoteConnection.run("free | grep Mem | awk '{print $3/$2 * 100.0}'", hide=True).stdout.strip("\n").replace(",","."))

    return memoryUsage

#Fetchs the current cpu usage percentile from an existing connection and returns it as a float
def getCpuUsage(remoteConnection):
    cpuUsage = float(remoteConnection.run("top -b -n2 | grep 'Cpu(s)' | awk '{print $2+$4 ""}' | tail -n1", hide=True).stdout.strip("\n").replace(",","."))

    return cpuUsage

#Displays the current resources usage over text
def textMonitor():
    remoteConnection = establish_ssh_connection()
    interval = input("Provide how often you want the data to be updated (in mintutes): ")
    while True:
        display_usage(getCpuUsage(remoteConnection), getMemoryUsage(remoteConnection), 15)
        time.sleep(float(interval)*60)

#Displays the current resources usage in a graph
def graphicalMonitor():
    remoteConnection = establish_ssh_connection()
    interval = float(input("Provide how often you want the data to be updated (in mintutes): "))
    plt.style.use('fivethirtyeight')

    time = []
    cpuValues = []
    ramValues = []

    index = count()

    def animate(i):
        
        time.append(next(index))
        cpuValues.append(getCpuUsage(remoteConnection))
        ramValues.append(getMemoryUsage(remoteConnection))

        plt.cla()
        plt.plot(time, cpuValues, label='CPU Usage')
        plt.plot(time, ramValues, label='RAM Usage')

        plt.legend(loc='upper left')
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interval=int(interval*60000), cache_frame_data=False)

    plt.tight_layout()
    plt.show()



#Calls to run the application
#textMonitor()
graphicalMonitor()