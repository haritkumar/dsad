def dict_ops():
    """
    Dictionary in Python is an unordered collection of data values, used to
    store data values like a map, which unlike other Data Types that hold
    only single value as an element, Dictionary holds key:value pair. Key-value
    is provided in the dictionary to make it more optimized. Each key-value pair
    in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’.

    In Python, a Dictionary can be created by placing a sequence of elements within curly {}
    braces, separated by ‘comma’. Values in a dictionary can be of any datatype and
    can be duplicated, whereas keys can’t be repeated and must be immutable. Dictionary
    can also be created by the built-in function dict(). An empty dictionary can be created
    by just placing it to curly braces{}.

    Note – Dictionary keys are case sensitive, same name but different cases of Key will be
    treated distinctly.
    """
    # Creating an empty Dictionary
    Dict = {}
    print("Empty Dictionary: ")
    print(Dict)

    # Creating a Dictionary
    # with Integer Keys
    Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    print("\nDictionary with the use of Integer Keys: ")
    print(Dict)

    # Creating a Dictionary
    # with Mixed keys
    Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
    print("\nDictionary with the use of Mixed Keys: ")
    print(Dict)

    # Creating a Dictionary
    # with dict() method
    Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
    print("\nDictionary with the use of dict(): ")
    print(Dict)

    # Creating a Dictionary
    # with each item as a Pair
    Dict = dict([(1, 'Geeks'), (2, 'For')])
    print("\nDictionary with each item as a pair: ")
    print(Dict)

    # accessing a element from a Dictionary

    # Creating a Dictionary
    Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

    # accessing a element using key
    print("Accessing a element using key:")
    print(Dict['name'])

    # accessing a element using get()
    # method
    print("Accessing a element using get:")
    print(Dict.get(3))

if __name__ == '__main__':
    dict_ops()