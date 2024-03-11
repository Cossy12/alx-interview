#!/usr/bin/python3
""" creates a Pascal's triangle of n rows and returns  a list.

: n:  input parameter for the function ,
 an integer representing the number of rows to generate
in the Pascal's triangle """

def pascal_triangle(n):
    """ list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []
    else:
        # Create an empty list to hold each row 
        triangle = []
        for i in range(n):
            # Create a new list for each row
            row = []
            for j in range(i+1):
                # Calculate the value of each element in the row
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # Append the row to the triangle list
            triangle.append(row)
        # Print the triangle
        return triangle
