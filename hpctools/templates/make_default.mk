# ================================
#   HPC Tools - Default Makefile
# ================================

CC = {compiler}
CFLAGS = {flags}
LDFLAGS = {ldflags}

SRC = {src}
OBJ = $(SRC:.c=.o)
TARGET = {output}

# --- Build rules ---
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) $(LDFLAGS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET)

# --- Documentation (optional) ---
docs:
	@doxygen ./Doxyfile || echo "No Doxyfile found."

.PHONY: all clean docs
