# Remote-Resources-Monitor

## About
A python application that allows to monitor RAM &amp; CPU usages for a remote machine running <strong>linux </strong>.
Script connects to remote machine over ssh and fetchs current resources usage.
Works on Linux & Windows

## Brief

### Methodology
Fabric is used to establish a connection between the host and the remote machine.
Top and Free are used to fetch the CPU and RAM usage in order to insure compatibility accross all linux distributions.
A simple reaccuring bar is used to represnt the data over text
Matplotlib is used to plot the data into a graphical visualisation

### Issues
Complications arise when trying to run a GUI script in a docker container environment that would require the use something similar to a VNC or X server in order to give access of the hosts display

### Fixes
One ideal fix would be to change from Docker to Conda 

## Requirements
Docker || Python >= 3.8

## Instalation

### Linux && Docker

Clone the repository:

```git clone https://github.com/adoma25/remote-resources-monitor.git```

Navigate to the repo directory:

``` cd remote-resources-monitor ```

Build the image using docker:

``` sudo build -t rrmonitor . ```

Run the built image:

``` sudo docker run --interactive --tty rrmonitor ```

### Terminal-Version in Docker Linux

![image](https://github.com/adoma25/remote-resources-monitor/assets/37664899/36fbb2ef-817e-4a07-ba94-e9bab9947384)


### Windows

If python >= 3.8 is installed you can run ``` python main.py ``` . Alternatively, Docker can be used on windows following similar steps.

![image](https://github.com/adoma25/remote-resources-monitor/assets/37664899/32400ba2-79e4-4dc4-8e4b-28d7a8d1219e)

### GUI Graph

![Merged_document](https://github.com/adoma25/remote-resources-monitor/assets/37664899/36d36230-00b4-43ab-9e4a-305f0a8b4f4d)

### Command-Line Version

![image](https://github.com/adoma25/remote-resources-monitor/assets/37664899/6dc44e82-caa4-44d5-962c-b530124607f7)





