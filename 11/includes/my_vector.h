#include <iostream>

#ifndef MY_VECTOR_H
#define MY_VECTOR_H

class my_vector
{
    friend std::ostream &operator<<(std::ostream &os, const my_vector &v);
    friend double operator*(double scalar, const my_vector &v);
    friend float operator*(float scalar, const my_vector &v);

private:
    double _x{0.};
    double _y{0.};
    double _z{0.};

public:
    my_vector();
    my_vector(const my_vector &other);
    my_vector(double x, double y, double z);

    ~my_vector();

    double getX() const;
    double getY() const;
    double getZ() const;

    void setX(double x);
    void setY(double y);
    void setZ(double z);

    my_vector operator+(const my_vector &rhs) const;
    my_vector operator-(const my_vector &rhs) const;
    my_vector operator*(const my_vector &rhs) const;
    my_vector operator*(double scalar) const;
    my_vector operator*(float scalar) const;
};

#endif // MY_VECTOR_H
