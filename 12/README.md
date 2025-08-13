# MMN12

Here you can find the solution for the [mmn12](./maman12.pdf) assignment for the course Defensive Systems Programming 20937.

## Exercise 1

You can find the solution at [exercise1.docx](./exercise1.docx).

## Exercise 2

You can find the solution at [exercise2.docx](./exercise2.docx).
And the fixed version of [mmn12-q2.cpp](./mmn12-q2.cpp) at [fixed-mmn12-q2.cpp](./fixed-mmn12-q2.cpp)

Build the solution with:

```bash
make 
```

If you're getting errors, install the `gcc-multilib` and `g++-multilib` packages:

```bash
sudo apt-get install gcc-multilib g++-multilib
```

Run the solution with:

```bash
./bin/mmn12-q2
```

*Note* that you have to disable the `ASLR` on your machine to run the solution. You can do this by running the following command:

```bash
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```
