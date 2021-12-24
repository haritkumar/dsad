def set_ops():
    """
    In Python, Set is an unordered collection of data type that is iterable,
    mutable and has no duplicate elements. The order of elements in a set is
    undefined though it may consist of various elements.

    Creating Sets
    Sets can be created by using the built-in set() function with an iterable object
    or a sequence by placing the sequence inside curly braces, separated by ‘comma’.
    Type of elements in a set need not be the same, various mixed-up data type values
    can also be passed to the set.

    The data structure used in this is Hashing, a popular technique to perform insertion,
    deletion, and traversal in O(1) on average.

    If Multiple values are present at the same index position, then the value is appended
    to that index position, to form a Linked List. In, CPython Sets are implemented using a
    dictionary with dummy variables, where key beings the members set with greater optimizations
    to the time complexity.
    """

    set_o = set([1, 3, 3 ,2])
    print(type(set_o))
    print(set_o)

    # Creating a Set
    set1 = set()
    print("Initial blank Set: ")
    print(set1)

    # Creating a Set with
    # the use of a String
    set1 = set("GeeksForGeeks")
    print("\nSet with the use of String: ")
    print(set1)

    # Creating a Set with
    # the use of a List
    set1 = set(["Geeks", "For", "Geeks"])
    print("\nSet with the use of List: ")
    print(set1)

    # Creating a Set with
    # a mixed type of values
    # (Having numbers and strings)
    set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
    print("\nSet with the use of Mixed Values")
    print(set1)

    """
    Set items cannot be accessed by referring to an index, since sets are unordered 
    the items has no index. But you can loop through the set items using a for 
    loop, or ask if a specified value is present in a set, by using the in keyword.
    """
    # Creating a set
    set1 = set(["Geeks", "For", "Geeks"])
    print("\nInitial set")
    print(set1)

    # Accessing element using
    # for loop
    print("\nElements of set: ")
    for i in set1:
        print(i, end=" ")

        # Checking the element
    # using in keyword
    print("Geeks" in set1)


if __name__ == '__main__':
    set_ops()