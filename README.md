# Key Space Calculator and Key Finder

## Overview and Purpose

The purpose of this project is to calculate the number of possible key options for a given key length and generate random key values within that range. It also implements a function to find a key through brute force method by iterating over the key values.

## Instruction

This script tests the brute force function to find a key given its key length and key space. The test runs for multiple key lengths and generates a random key for each one. The brute force function then attempts to find the key and the time taken is recorded. 

### Prerequisites

- Python 3 installed on your machine
- Required Libraries:
  - decimal
  - time
  - random
  
### Running the script

To run the script, follow these steps:

1. Clone the repository or download the script file.
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Type the following command to run the script:

``` 
python3 key_brute_force_testing.py
```

4. The script will output the key space and random key generated for each key length, followed by the time taken to find the key using the brute force function.

## System Content

This project utilizes the bignum type from the `struct` library (PEP 237) to handle large integer values and perform operations with them.

## Interaction with Other Components

This project does not interact with any other components.

## Product Features

- Calculation of key space for 8- to 4096-bit key lengths
- Generation of random key values within the given key length range
- Brute force key finder function that outputs the time taken to find the key

## Security Requirements

This project does not handle any sensitive information and does not have any specific security requirements.

## Characteristics of Users

This project is intended for individuals interested in understanding the concept of key space and key generation in cryptography.

## Restrictions

The key length input must be in the range of 8 to 4096. The brute force key finder function may take a long time to find the key for larger key lengths. 
