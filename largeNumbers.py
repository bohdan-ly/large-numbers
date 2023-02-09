import decimal
import time
import random

# Key length options
key_lengths = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
output_to_file = True  # Set to false if you do not want to write output to file

# Calculate key space for each key length
if output_to_file:
    with open("key_space.txt", "w") as f:
        for key_length in key_lengths:
            key_space = 2 ** key_length
            line = f"Key length: {key_length}, Key space: {key_space}\n"
            print(line)
            f.write(line)
else:
    for key_length in key_lengths:
        key_space = 2 ** key_length
        print(f"Key length: {key_length}, Key space: {key_space}")

# Generate random key value for each key length
if output_to_file:
    with open("random_keys.txt", "w") as f:
        for key_length in key_lengths:
            key_space = 2 ** key_length
            key = decimal.Decimal(key_space * decimal.Decimal(random.random()))
            line = f"Key length: {key_length}, Key: {key}\n"
            print(line)
            f.write(line)
else:
    for key_length in key_lengths:
        key_space = 2 ** key_length
        key = decimal.Decimal(key_space * decimal.Decimal(random.random()))
        print(f"Key length: {key_length}, Key: {key}")


# Brute force function to find key
def find_key(key, key_space, output_to_file=False):
    start = time.time()
    for i in range(key_space):
        if i == key:
            end = time.time()
            duration = (end - start) * 1000
            if output_to_file:
                with open("key_search_result.txt", "a") as f:
                    line = f"Key found - {i}! Time taken: {duration} ms\n"
                    print(line)
                    f.write(line)
            else:
                print(f"Key found - {i}! Time taken: {duration} ms")
            return


# Test brute force function
for key_length in key_lengths:
    key_space = 2 ** key_length
    key = decimal.Decimal(key_space * decimal.Decimal(random.random()))
    find_key(key, key_space, output_to_file)
