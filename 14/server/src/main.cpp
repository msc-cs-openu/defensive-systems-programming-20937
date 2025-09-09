#include <boost/algorithm/string.hpp>
#include <iostream>
#include <string>

int main(int argc, char const *argv[])
{
    std::string str = "Boost Libraries";
    boost::to_upper(str);
    std::cout << str << std::endl;

    return 0;
}
