my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
my_tuple[0] = 10  # This will raise an error because tuples are immutable
print(my_tuple)
for port in my_tuple:
    print(port)
