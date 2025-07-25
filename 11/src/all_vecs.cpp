#include <iostream>
#include <string>
#include <unordered_map>
#include "my_vector.h"

typedef std::unordered_map<std::string, my_vector> my_vector_map;

int main(int argc, char const *argv[])
{
    my_vector_map vectors{
        {"David", my_vector(1, 2, 3)},
        {"Dana", my_vector(4, 5, 6)},
        {"Moshe", my_vector(7, 8, 9)},
        {"Vered", my_vector(10, 11, 12)},
        {"Mohammed", my_vector(13, 14, 15)},
        {"Yasmin", my_vector(16, 17, 18)},
        {"Ahmed", my_vector(19, 20, 21)},
        {"Lucy", my_vector(22, 23, 24)},
        {"Naftali", my_vector(25, 26, 27)},
        {"Ayelet", my_vector(28, 29, 30)}};

    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <vector-name>" << std::endl;
        return 1;
    }

    if (vectors.find(argv[1]) == vectors.end())
    {
        std::cerr << "Vector '" << argv[1] << "' not found." << std::endl;
        return 1;
    }

    std::cout << "Vector " << argv[1] << ": " << vectors[argv[1]] << std::endl;

    return 0;
}
