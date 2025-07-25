#include "my_vector.h"
#include <iostream>

my_vector::my_vector() = default;
my_vector::my_vector(const my_vector &other) : _x{other._x}, _y{other._y}, _z{other._z} {}
my_vector::my_vector(double x, double y, double z) : _x{x}, _y{y}, _z{z} {}

my_vector::~my_vector() = default;

double my_vector::getX() const { return _x; }
double my_vector::getY() const { return _y; }
double my_vector::getZ() const { return _z; }

void my_vector::setX(double x) { _x = x; }
void my_vector::setY(double y) { _y = y; }
void my_vector::setZ(double z) { _z = z; }

my_vector my_vector::operator+(const my_vector &rhs) const
{
    return my_vector(_x + rhs._x, _y + rhs._y, _z + rhs._z);
}

my_vector my_vector::operator-(const my_vector &rhs) const
{
    return my_vector(_x - rhs._x, _y - rhs._y, _z - rhs._z);
}

my_vector my_vector::operator*(const my_vector &rhs) const
{
    return my_vector(_x * rhs._x, _y * rhs._y, _z * rhs._z);
}

my_vector my_vector::operator*(double scalar) const
{
    return my_vector(_x * scalar, _y * scalar, _z * scalar);
}

my_vector my_vector::operator*(float scalar) const
{
    return my_vector(_x * scalar, _y * scalar, _z * scalar);
}

std::ostream &operator<<(std::ostream &os, const my_vector &v)
{
    os << "(" << v._x << ", " << v._y << ", " << v._z << ")";
    return os;
}

double operator*(double scalar, const my_vector &v)
{
    return scalar * (v._x + v._y + v._z);
}

float operator*(float scalar, const my_vector &v)
{
    return static_cast<float>(scalar * (v._x + v._y + v._z));
}
