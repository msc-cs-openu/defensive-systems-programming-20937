# MMN11

Here you can find the the files and solutions for the [mmn11](/11/mmn11-2024c.pdf) assignment for the course Defensive Systems Programming 20937.

## System Requirements

From any linux distro of your choice make sure you have the following installed:

- `make`
- `g++`

## Solutions

### Exercise 1

You can find the solution at [exercise1.docx](./exercise1.docx)

### Exercise 2

Files:

- [src/my_vec.cpp](./src/my_vec.cpp) with the `main` function.
- [src/my_vector.cpp](./src/my_vector.cpp) with implementation of the `my_vector` class.
- [includes/my_vector.h](./includes/my_vector.h) with the declaration of the `my_vector` class.

How to run:

```bash
make exercise2
```

### Exercise 3

Files:

- [src/all_vecs.cpp](./src/all_vecs.cpp) with the `main` function.
- [includes/my_string.h](./includes/my_string.h) with the declaration of the `my_string` class.
- [src/my_string.cpp](./src/my_string.cpp) with implementation of the `my_string` class.

How to run:

```bash
make exercise3 NAME=Vered # or any other name
```

### Exercise 4

Files:

- [data/example.csv](./data/example.csv) with example data.
- [src/csv_read.cpp](./src/read_csv.cpp) with the `main` function.

How to run:

```bash
make exercise4 FILE=./data/example.csv # or any other csv file
```
