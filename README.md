# NQT Preparation

This repository contains solutions to various coding problems, primarily focused on NQT (National Qualifier Test) preparation. The problems cover a range of topics including basic programming concepts, data structures, algorithms, and common interview questions.

## Table of Contents

- [Problem Categories](#problem-categories)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Problem Categories

The problems are organized into the following categories:

- **Basic**: Fundamental programming concepts, arithmetic operations, conditional statements, loops.
- **String**: String manipulation, pattern matching, character operations.
- **Array**: Array manipulation, searching, sorting, dynamic programming on arrays.
- **Data Structures**: Implementations and problems related to Linked Lists, Trees, Graphs, etc.
- **Top 100**: A collection of frequently asked interview questions.
- **NQT2025**: Specific problems encountered or expected in NQT 2025.
- **Practice**: General practice problems.

## How to Use This Repository

Each problem typically has its own file (e.g., `problem_name.py`) within its respective category.

### Example Problem Structure

Let's consider an example problem: `Basic/armstrong.py`

```python
# Problem: Check if a number is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

def is_armstrong(num):
    # Convert number to string to get its length (number of digits)
    num_str = str(num)
    n = len(num_str)
    
    sum_of_powers = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum_of_powers += digit ** n
        temp_num //= 10
        
    return num == sum_of_powers

# Test cases
print(f"Is 153 an Armstrong number? {is_armstrong(153)}") # Expected: True (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153)
print(f"Is 9 an Armstrong number? {is_armstrong(9)}")     # Expected: True (9^1 = 9)
print(f"Is 10 an Armstrong number? {is_armstrong(10)}")    # Expected: False
print(f"Is 371 an Armstrong number? {is_armstrong(371)}") # Expected: True (3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371)
```

### Running a Solution

To run a specific solution, navigate to the directory containing the file and execute it using Python:

```bash
cd Basic
python armstrong.py
```

## Contribution Guidelines

Contributions are welcome! If you'd like to add a new problem or improve an existing solution, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Add your problem/solution in the appropriate category.
4.  Ensure your code is well-commented and includes test cases.
5.  Commit your changes (`git commit -m 'Add new problem: Problem Name'`).
6.  Push to the branch (`git push origin feature/your-feature-name`).
7.  Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
