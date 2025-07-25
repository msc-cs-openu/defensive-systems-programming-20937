# compiler config
CXX      := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Wpedantic -Iincludes

# directories
DATADIR  := data
SRCDIR   := src
INCDIR   := includes
BUILDDIR := build
OBJDIR   := $(BUILDDIR)/obj
BINDIR   := $(BUILDDIR)/bin

# executables
EXECUTABLES := all_vecs my_vec read_csv

# targets
SOURCES := $(wildcard $(SRCDIR)/*.cpp)
OBJECTS := $(patsubst $(SRCDIR)/%.cpp,$(OBJDIR)/%.o, $(SOURCES))
TARGETS := $(addprefix $(BINDIR)/, $(EXECUTABLES))
HEADERS := $(wildcard $(INCDIR)/*.h)
SHARED  := $(patsubst $(INCDIR)/%.h, $(OBJDIR)/%.o, $(wildcard $(INCDIR)/*.h))

.PHONY: all

all: $(TARGETS)

# assert dirs exist
$(BINDIR) $(OBJDIR):
	@mkdir -p $@

# compilation rule
$(OBJDIR)/%.o: $(SRCDIR)/%.cpp $(HEADERS) | $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# executable rule
$(BINDIR)/%: $(OBJDIR)/%.o $(SHARED) | $(BINDIR)
	$(CXX) $(LDFLAGS) $^ -o $@

clean:
	rm -rf $(BUILDDIR) ./output.txt

exercise2: $(BINDIR)/my_vec
	@./$<

exercise3: $(BINDIR)/all_vecs
	@./$< $(NAME)

exercise4: $(BINDIR)/read_csv
	@./$< $(FILE)
