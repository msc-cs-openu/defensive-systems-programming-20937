#ifndef SERVER_H
#define SERVER_H

#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

class Server
{
    const static size_t BUFF_SIZE;
    const static uint16_t DEFAULT_PORT;
    const static size_t DEFAULT_MAX_CONNECTIONS;

private:
    boost::asio::io_context _io_context;
    tcp::acceptor _acceptor;

public:
    Server(
        uint16_t port = Server::DEFAULT_PORT,
        size_t max_connections = Server::DEFAULT_MAX_CONNECTIONS);
    ~Server();

    tcp::socket accept();
};

#endif // SERVER_H