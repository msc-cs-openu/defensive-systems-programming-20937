#include <atomic>
#include <csignal>
#include <initializer_list>
#include <thread>
#include <vector>
#include <memory>

std::atomic<bool> running = true;

int main(int argc, char const *argv[])
{
    // RAII wrapper for worker threads
    auto workers = std::make_unique<std::vector<std::thread>>(
        [](auto &&...args)
        {
            for (auto &worker : *workers)
            {
                if (worker.joinable())
                {
                    worker.join();
                }
            }
        });

    // graceful shutdown
    for (auto &&sig : {SIGINT, SIGTERM})
    {
        std::signal(sig, [](int signum)
                    { running = false; });
    }

    // setup server socket

    while (running)
    {
        //
    }

    return 0;
}
