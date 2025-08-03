#include <iostream>
#include <string>
#include <unordered_map>
#include "my_vector.h"
#include "my_string.h"

typedef std::unordered_map<my_string, my_vector> my_vector_map;

int main(int argc, char const *argv[])
{
    my_vector_map vectors{
        {my_string{"David"}, my_vector(1, 2, 3)},
        {my_string{"Dana"}, my_vector(4, 5, 6)},
        {my_string{"Moshe"}, my_vector(7, 8, 9)},
        {my_string{"Vered"}, my_vector(10, 11, 12)},
        {my_string{"Mohammed"}, my_vector(13, 14, 15)},
        {my_string{"Yasmin"}, my_vector(16, 17, 18)},
        {my_string{"Ahmed"}, my_vector(19, 20, 21)},
        {my_string{"Lucy"}, my_vector(22, 23, 24)},
        {my_string{"Naftali"}, my_vector(25, 26, 27)},
        {my_string{"Ayelet"}, my_vector(28, 29, 30)}};

    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <vector-name>" << std::endl;
        return 1;
    }

    my_string vector_name(argv[1]);

    if (vectors.find(vector_name) == vectors.end())
    {
        std::cerr << "Vector '" << vector_name.value() << "' not found." << std::endl;
        return 1;
    }

    std::cout << "Vector " << vector_name.value() << ": " << vectors[vector_name] << std::endl;

    return 0;
}
