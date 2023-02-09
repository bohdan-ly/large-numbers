# Key Space Calculator and Key Finder

## Overview and Purpose

The purpose of this project is to calculate the number of possible key options for a given key length and generate random key values within that range. It also implements a function to find a key through brute force method by iterating over the key values. 

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
