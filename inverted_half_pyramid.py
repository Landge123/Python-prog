# Inverted Half Pyramid Pattern

# Method 1: Using stars (*)
print("Inverted Half Pyramid with Stars:")
n = 5
for i in range(n, 0, -1):
    print("* " * i)

print("\n" + "="*20 + "\n")

# Method 2: Using numbers
print("Inverted Half Pyramid with Numbers:")
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

print("\n" + "="*20 + "\n")

# Method 3: User input version
print("Inverted Half Pyramid (User Input):")
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("* " * i)
