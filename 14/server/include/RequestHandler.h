#ifndef REQUESTHANDLER_H
#define REQUESTHANDLER_H

#include <boost/asio.hpp>
#include "proto.h"

using boost::asio::ip::tcp;

class RequestHandler
{
private:
    tcp::socket client;

public:
    explicit RequestHandler(tcp::socket &&client);
    ~RequestHandler() = default;

    void handle();

    Request get_request();
    void send_response(const Response &res);
};

#endif // REQUESTHANDLER_H
