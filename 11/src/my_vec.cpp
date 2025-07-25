#include <ostream>
#include "my_vector.h"

int main()
{
    my_vector v1(1.0, 2.0, 3.0);
    my_vector v2(4.0, 5.0, 6.0);

    std::cout << "v1: " << v1 << std::endl;
    std::cout << "v2: " << v2 << std::endl;
    std::cout << "(v1 + v2): " << (v1 + v2) << std::endl;
    std::cout << "(v1 - v2): " << (v1 - v2) << std::endl;
    std::cout << "(v1 * v2): " << (v1 * v2) << std::endl;

    std::cout << "(v1 * 2.0): " << (v1 * 2.0) << std::endl;
    std::cout << "(2.0 * v2): " << (2.0 * v2) << std::endl;

    std::cout << "(v1 * 3.0f): " << (v1 * 3.0f) << std::endl;
    std::cout << "(3.0f * v2): " << (3.0f * v2) << std::endl;

    return 0;
}
