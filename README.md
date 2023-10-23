# Remote-Resources-Monitor

## About
A python application that allows to monitor RAM &amp; CPU usages for a remote machine running <strong>linux </strong>.
Script connects to remote machine over ssh and fetchs current resources usage.
Works on Linux & Windows

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

### Windows

If python >= 3.8 is installed you can run ``` python main.py ``` . Alternatively, Docker can be used on windows following similar steps.

![image](https://github.com/adoma25/remote-resources-monitor/assets/37664899/32400ba2-79e4-4dc4-8e4b-28d7a8d1219e)

### GUI Graph

![Merged_document](https://github.com/adoma25/remote-resources-monitor/assets/37664899/36d36230-00b4-43ab-9e4a-305f0a8b4f4d)

### Command-Line Version

![image](https://github.com/adoma25/remote-resources-monitor/assets/37664899/6dc44e82-caa4-44d5-962c-b530124607f7)





