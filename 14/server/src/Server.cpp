#include "Server.h"

const size_t Server::BUFF_SIZE = 4096;
const uint16_t Server::DEFAULT_PORT = 4321;
const size_t Server::DEFAULT_MAX_CONNECTIONS = 10;

Server::Server(uint16_t port, size_t max_connections)
    : _io_context(static_cast<int>(max_connections)),
      _acceptor(_io_context, tcp::endpoint(tcp::v4(), port))
{
    //
}

tcp::socket Server::accept()
{
    return std::move(_acceptor.accept());
}

Server::~Server()
{
    _acceptor.cancel();
    _acceptor.close();
    _io_context.stop();
}
