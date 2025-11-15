from geo.utils import add, subtract, multiply

def test():
    assert add(1, 2) == 3
    assert subtract(5, 3) == 2
    assert multiply(2, 4) == 8
    print("Success!")

if __name__ == "__main__":
    test()
