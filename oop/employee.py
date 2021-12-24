class Employee:
    name: str = ''
    age: int = 0
    fee: float = 0.0
    active: bool = True

    # init method or constructor
    def __init__(self, name):
        self.name = name

    def __del__(self):
        # body of destructor
        self.name = ''

    def get_fee(self):
        return self.fee


if __name__ == '__main__':
    e = Employee('Harit')
    print(e.name)
    print(e.get_fee())
