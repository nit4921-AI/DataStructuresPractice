'''Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .'''
def staircase(n):
    for i in range(1, n + 1):
        spaces = n - i
        print(' ' * spaces + '#' * i)


if __name__ == "__main__":
    n = int(input("Enter staircase size: "))
    staircase(n)