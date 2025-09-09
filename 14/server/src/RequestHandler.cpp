#include <iostream>
#include "RequestHandler.h"
#include "proto.h"

RequestHandler::RequestHandler(tcp::socket &&client)
    : client(std::move(client))
{
    //
}

void RequestHandler::handle()
{
    std::cout << "--------------------------------" << std::endl;
    std::cout << "Connection: " << client.remote_endpoint() << std::endl;

    auto req{get_request()};
    Response res{
        .version = req.version,
        .status = Status::ErrorGeneral,
        .name_len = 0,
        .filename = "",
        .size = 0,
        .payload = {}};

    std::cout << "Request{"
              << "user_id=" << req.user_id
              << ", version=" << static_cast<int>(req.version)
              << ", op=" << static_cast<int>(req.op)
              << ", name_len=" << req.name_len
              << ", filename=" << req.filename
              << ", size=" << req.size
              << ", payload_size=" << req.payload.size()
              << "}"
              << std::endl;

    try
    {
        switch (req.op)
        {
            // case Op::Save:
            //     break;
            // case Op::List:
            //     break;
            // case Op::Upload:
            //     break;
            // case Op::Retrieve:
            //     break;
        }
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
    }

    send_response(res);

    std::cout << "Response{"
              << "version=" << static_cast<int>(res.version)
              << ", status=" << static_cast<int>(res.status)
              << ", name_len=" << res.name_len
              << ", filename=" << res.filename
              << ", size=" << res.size
              << ", payload_size=" << res.payload.size()
              << "}"
              << std::endl;
    std::cout << "--------------------------------" << std::endl;
}

Request RequestHandler::get_request()
{
    Request req;

    boost::asio::read(client, boost::asio::buffer(&req.user_id, sizeof(req.user_id)));
    boost::asio::read(client, boost::asio::buffer(&req.version, sizeof(req.version)));
    boost::asio::read(client, boost::asio::buffer(&req.op, sizeof(req.op)));
    boost::asio::read(client, boost::asio::buffer(&req.name_len, sizeof(req.name_len)));

    // variable-length filename
    if (req.name_len > 0)
    {
        req.filename.resize(req.name_len);
        boost::asio::read(client, boost::asio::buffer(req.filename.data(), req.name_len));
    }

    // read size after filename
    boost::asio::read(client, boost::asio::buffer(&req.size, sizeof(req.size)));

    // variable-length payload
    if (req.size > 0)
    {
        req.payload.resize(req.size);
        boost::asio::read(client, boost::asio::buffer(req.payload.data(), req.size));
    }

    return req;
}

void RequestHandler::send_response(const Response &res)
{
    boost::asio::write(client, boost::asio::buffer(&res.version, sizeof(res.version)));
    boost::asio::write(client, boost::asio::buffer(&res.status, sizeof(res.status)));
    boost::asio::write(client, boost::asio::buffer(&res.name_len, sizeof(res.name_len)));

    // variable-length filename
    if (res.name_len > 0)
    {
        boost::asio::write(client, boost::asio::buffer(res.filename.data(), res.name_len));
    }

    // write size after filename
    boost::asio::write(client, boost::asio::buffer(&res.size, sizeof(res.size)));

    // variable-length payload
    if (res.size > 0)
    {
        boost::asio::write(client, boost::asio::buffer(res.payload.data(), res.size));
    }
}
