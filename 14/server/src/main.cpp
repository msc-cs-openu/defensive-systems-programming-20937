#include <iostream>
#include <atomic>
#include <csignal>
#include <thread>
#include "Server.h"
#include "RequestHandler.h"

std::atomic<bool> running(true);

int main(int argc, char const *argv[])
{
    // gracefull shutdown on SIGINT, SIGTERM
    std::signal(SIGINT, [](int)
                { running = false; });
    std::signal(SIGTERM, [](int)
                { running = false; });

    Server server;

    std::cout << "Server is running..." << std::endl;

    while (running)
    {
        try
        {
            std::thread([client = server.accept()]() mutable
                        {
                            std::cout << "Spawning thread " << std::this_thread::get_id() << std::endl;

                            while (running && client.is_open())
                            {
                                RequestHandler(std::move(client)).handle();
                            }

                            std::cout << "Thread " << std::this_thread::get_id() << " is terminating." << std::endl;
                        })
                .detach();
        }
        catch (const std::exception &e)
        {
            std::cerr << e.what() << '\n';
        }
    }

    std::cout << "Shutting down server..." << std::endl;

    return 0;
}
