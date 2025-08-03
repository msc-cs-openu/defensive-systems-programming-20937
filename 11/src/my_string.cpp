#include "my_string.h"
#include <regex>
#include <stdexcept>

my_string::my_string(const std::string &str)
{
    static const std::regex pattern(R"([a-zA-Z_][a-zA-Z0-9_]*)");

    if (!std::regex_match(str, pattern))
    {
        throw std::invalid_argument("Invalid my_string value: " + str);
    }

    _str = str;
}

const std::string &my_string::value() const
{
    return _str;
}

bool my_string::operator==(const my_string &other) const
{
    return _str == other._str;
}
