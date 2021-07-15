# Task2-Client_Server
IPC and the PC communication protocol have exchange data. TwinCAT Function block is receiving and sending data using TF6310 TwinCAT TCP/IP Server. 
TwinCAT version used: v3.1.4020

## How to run

Open TF6310 TwinCAT TCP/IP Server and Run the TwinCAT program first.
Run the client Python program.
Send 'On1' to turn on bVar1, and 'On2' to turn on bVar2, otherwise to turn off both. TwinCAT will echo back all commands.

## How it works

What's happening inside the function block FB_TcpServer:

FB_SocketConnect opens the socket at the specified port.
Python client connects to the host and the port. 
Every 100ms FB_SocketAccept will accept any incoming connection, and populate the variable 'hSocket' with the local address of the server and remote address of the client.
FB_SocketSend and FB_SocketReceive use this 'hSocket' to send and receive data.

## State machine

![alt tag](https://puu.sh/sBxgh/a6d8de1c9a.png)



## Overview of running in Docker container
First we have to build our containers using docker compose
```sh
docker-compose build
```
Then we run our 2 containers
```sh
docker-compose up -d
```
We use the `-d` to run in detached mode

## Check the logs
Once our containers are running, we can check what is actually happening on the client and the server by checking the docker logs:

```sh
docker ps
```

```sh
docker logs --follow <CONTAINER_ID>
```

##
