import array


def arr():
    """
    An array is a vector containing homogeneous elements
    i.e. belonging to the same data type. Elements are allocated with
    contiguous memory locations allowing easy modification, that is,
    addition, deletion, accessing of elements. In Python, we have to
    use the array module to declare arrays. If the elements of an array
    belong to different data types, an exception “Incompatible data types” is thrown.
    """
    my_array = array.array('i', [1, 2])  # b, B, u, h, H, i, I, l, L, q, Q, f or d
    my_array.append(11)
    print(my_array)


def list_ds():
    """
    Lists are just like the arrays, declared in other languages which is a ordered
    collection of data. It is very flexible as the items in a list do not need to
    be of the same type.

    Python uses resizable vectors under the hood. They maintain knowledge of how many
    elements are in the list as well as what the current total capacity is. When you
    try to add another element beyond the size of the collection, it allocates a new
    array with more capacity and populates it with the pointers to items from the original
     backing array. This is similar to java's ArrayList type, except that there's no way to
     specify the capacity in python
    """
    # Creating a List
    List = []
    print("Initial blank List: ")
    print(List)

    # Creating a List with
    # the use of a String
    List = ['GeeksForGeeks']
    print("\nList with the use of String: ")
    print(List)

    # Creating a List with
    # the use of multiple values
    List = ["Geeks", "For", "Geeks"]
    print("\nList containing multiple values: ")
    print(List[0])
    print(List[2])

    # Creating a Multi-Dimensional List
    # (By Nesting a list inside a List)
    List = [['Geeks', 'For'], ['Geeks']]
    print("\nMulti-Dimensional List: ")
    print(List)
    print(List[1])


if __name__ == '__main__':
    # arr()
    list_ds()
