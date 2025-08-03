#include <string>
#include <functional>

#ifndef MY_STRING_H
#define MY_STRING_H

class my_string
{
public:
    explicit my_string(const std::string &str);
    const std::string &value() const;
    bool operator==(const my_string &other) const;

private:
    std::string _str;
};

namespace std
{
    template <>
    struct hash<my_string>
    {
        std::size_t operator()(const my_string &s) const
        {
            return std::hash<std::string>()(s.value());
        }
    };
}

#endif // MY_STRING_H
