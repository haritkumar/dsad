import list
import set
import tuple


def numeric():
    a = 5
    print("Type of a: ", type(a))

    b = 5.0
    print("\nType of b: ", type(b))

    c = 2 + 4j
    print("\nType of c: ", type(c))


def string():
    # Creating a String
    # with single Quotes
    String1 = 'Welcome to the Geeks World'
    print("String with the use of Single Quotes: ")
    print(String1)

    # Creating a String
    # with double Quotes
    String1 = "I'm a Geek"
    print("\nString with the use of Double Quotes: ")
    print(String1)
    print(type(String1))

    # Creating a String
    # with triple Quotes
    String1 = '''I'm a Geek and I live in a world of "Geeks"'''
    print("\nString with the use of Triple Quotes: ")
    print(String1)
    print(type(String1))

    # Creating String with triple
    # Quotes allows multiple lines
    String1 = '''Geeks 
                For 
                Life'''
    print("\nCreating a multiline String: ")
    print(String1)

    # Python Program to Access
    # characters of String
    String1 = "GeeksForGeeks"
    print("Initial String: ")
    print(String1)

    # Printing First character
    print("\nFirst character of String is: ")
    print(String1[0])

    # Printing Last character
    print("\nLast character of String is: ")
    print(String1[-1])


def sequence():
    """
    In Python, Strings are arrays of bytes representing Unicode characters.
    A string is a collection of one or more characters put in a single quote,
    double-quote or triple quote. In python there is no character data type,
    a character is a string of length one. It is represented by str class.
    """
    string()
    list.list_ds()
    tuple.tuple_ops()

if __name__ == '__main__':
    # numeric()
    # sequence()
    set.set_ops()
