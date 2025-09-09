# MMN 14

In this exercise, we will implement a server application for file backup and retrieval, and a client application to interact with it.  
The server will be written in C++ and the client in Python.

See the [mmn14.pdf](mmn14.pdf) for more details.

## Run the Server

Make sure you have `g++`, `make`, and `cmake` installed. Then, install Boost (required dependency):

```bash
sudo apt update
sudo apt install libboost-all-dev
```

Now, build the server:

```bash
cd server
cmake .
make

```

And run it:

```bash
./build/mmn14-server <port_number>
```

## Run the client

Make sure you have Python 3.11+ installed. Then, run the client script:

```bash
python3 client/main.py <Optional user_id>
```
