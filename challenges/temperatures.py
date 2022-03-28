"""
In this exercise, you have to analyze records of temperature to find the closest to zero.

Write a program that prints the temperature closest to 0 among input data.
If two numbers are equally close to zero, positive integer has to be considered closest to zero
(for instance, if the temperatures are -5 and 5, then display 5).

Game Input
Your program must read the data from the standard input and write the result on the standard output.

# Input
Line 1: N, the number of temperatures to analyze

Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

# Output
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000

Example
Input               |  Output
5                   |       1
1 -2 -8 4 5         |


@author Codeingame

https://www.codingame.com/ide/puzzle/temperatures
"""

import sys

n = int(input())  # the number of temperatures to analyse
temperatures = []
closest_to_zero = []
count = 0

if not n:
    print('0')
else:
    for i in input().split():
        t = int(i)
        temperatures.append(t)
        temperatures = sorted(temperatures)

    for temperature in temperatures:
        if temperature < 0:
            count += 1
            to_zero = temperature * -1
            closest_to_zero.append(to_zero)
        else:
            closest_to_zero.append(temperature)

    if count == len(temperatures):
        print(sorted(temperatures)[-1])
    else:
        print(sorted(closest_to_zero)[0])
