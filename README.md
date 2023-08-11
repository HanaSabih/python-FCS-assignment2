# Functions and POS System

This repository contains Python functions that demonstrate various tasks, including string manipulation, list analysis, and a simple Point of Sale (POS) system.

## Functions

### 1. Reverse Concatenate Function

This function takes a string `s` and an integer `i` as parameters and returns a string where `s` is reversed and concatenated `i` times. If `i` is 0, the function returns an empty string.

### 2. Rearrange Case Function

This function takes a string `s` as a parameter and returns another string where all the letters in `s` have been re-arranged such that uppercase letters appear before lowercase letters.

### 3. Reordering Check Function

This function takes two strings `s1` and `s2` as parameters and returns `True` if `s1` is a reordering of the characters in `s2`.

### 4. Maximum Value Function

This function takes a list of numbers `l` as a parameter and returns the highest number in the list along with its index.

### 5. Recursive Digit Counting Function

This function counts the digits of a given number recursively.

## List Jumps Analysis

### List Jumps Function

Given a list of positive and negative integers representing forward or negative jumps, this function analyzes the jumps and returns "cycle" if the index will never leave the boundaries of the input list, otherwise it returns "out-of-bounds".

## Point of Sale (POS) System

This part of the repository contains a simple POS system for a store. The system keeps track of items available for purchase, including their barcode, name, and price. The following steps outline its functionality:

1. The system prompts the user to start a new receipt.
2. If the user chooses to start a receipt, they will be prompted to input item barcode and quantity.
3. The user can add multiple items to the receipt.
4. Once the user is done adding items, the system displays the receipt with each item's details and the total cost.
5. The user can choose to start a new receipt and repeat the process.

The POS system provides a basic interface for managing sales transactions.

## Usage

To use any of the functions provided, simply import the respective module and call the function with appropriate parameters. For the POS system, run the script and follow the prompts to simulate the process.

---

Feel free to clone or fork this repository and use the functions and POS system in your projects. If you have any questions or improvements, feel free to contribute or reach out!

---

**Note:** The examples and descriptions provided here are for illustrative purposes. Be sure to adapt and integrate the code as needed for your specific use case.
