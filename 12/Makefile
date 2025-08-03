# Compiler configuration
CC = g++
CFLAGS = -Wall -Wextra -std=c++17 -m32 -g3

# Directories
OBJ_DIR = obj
BIN_DIR = bin

# Source files
SRCS = mmn12-q2.cpp

# Object files
OBJS = $(addprefix $(OBJ_DIR)/, $(SRCS:.cpp=.o))

# Executable name
TARGET = $(BIN_DIR)/mmn12-q2

# Build rules
all: $(TARGET)

$(TARGET): $(OBJS)
	mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: %.cpp
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

.PHONY: all clean
