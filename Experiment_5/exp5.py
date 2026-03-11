"""
Aim: Write a program to demonstrate tuple & related functions in python.
"""

def demonstrate_tuples():
    print("--- TUPLE FUNCTIONS ---")
    
    my_tuple = (10, 20, 30, 40, 20, 50)
    print("Original Tuple:", my_tuple)
    
    print("Length of the tuple:", len(my_tuple))
    
    print("Number of times '20' appears:", my_tuple.count(20))
    
    print("Index of the first '30':", my_tuple.index(30))
    
    print("Maximum value:", max(my_tuple))
    
    print("Minimum value:", min(my_tuple))
    
    print("Sum of all elements:", sum(my_tuple))
    
    print("Sorted elements (returns a list):", sorted(my_tuple))
    
    my_list = [100, 200, 300]
    converted_tuple = tuple(my_list)
    print("Converted from list:", converted_tuple)
    
    bool_tuple = (0, False, 1)
    
    print("Any true element in", bool_tuple, "?:", any(bool_tuple))
    
    print("All true elements in", bool_tuple, "?:", all(bool_tuple))

demonstrate_tuples()
