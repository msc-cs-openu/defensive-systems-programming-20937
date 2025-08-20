# Compiler configuration
CC = g++
CFLAGS = -std=c++17 -m32 -g3 
# Directories
OBJ_DIR = obj
BIN_DIR = bin

# Source files and targets
SRCS = mmn12-q2.cpp fixed-mmn12-q2.cpp
TARGETS = $(addprefix $(BIN_DIR)/, $(SRCS:.cpp=))

# Object files
OBJS = $(addprefix $(OBJ_DIR)/, $(SRCS:.cpp=.o))

# Build rules
all: $(TARGETS)

$(BIN_DIR)/%: $(OBJ_DIR)/%.o
	mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: %.cpp
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

.PHONY: all clean
