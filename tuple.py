def tuple_ops():
    """
    Just like list, tuple is also an ordered collection of Python objects.
    The only difference between tuple and list is that tuples are immutable
     i.e. tuples cannot be modified after it is created. It is represented by tuple class.
    """
    # Creating an empty tuple
    Tuple1 = ()
    print("Initial empty Tuple: ")
    print(Tuple1)

    # Creating a Tuple with
    # the use of Strings
    Tuple1 = ('Geeks', 'For')
    print("\nTuple with the use of String: ")
    print(Tuple1)

    # Creating a Tuple with
    # the use of list
    list1 = [1, 2, 4, 5, 6]
    print("\nTuple using List: ")
    print(tuple(list1))

    # Creating a Tuple with the
    # use of built-in function
    Tuple1 = tuple('Geeks')
    print("\nTuple with the use of function: ")
    print(Tuple1)

    # Creating a Tuple
    # with nested tuples
    Tuple1 = (0, 1, 2, 3)
    Tuple2 = ('python', 'geek')
    Tuple3 = (Tuple1, Tuple2)
    print("\nTuple with nested tuples: ")
    print(Tuple3)

    tuple1 = tuple([1, 2, 3, 4, 5])

    # Accessing element using indexing
    print("First element of tuple")
    print(tuple1[0])

    # Accessing element from last
    # negative indexing
    print("\nLast element of tuple")
    print(tuple1[-1])

    print("\nThird last element of tuple")
    print(tuple1[-3])