class TestRecursion():
    def __init__(self):
        pass

    def factorial(self, n):
        if n == 0:
            return 1
        elif n < 0:
            return None
        else:
            return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n <= 0:
            return None
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    test_example = TestRecursion()
    print(test_example.factorial(4), end=", ")
    print(test_example.factorial(0), end=", ")
    print(test_example.factorial(-4), end="\n")
    print(test_example.fibonacci(4), end=", ")
    print(test_example.fibonacci(0), end=", ")
    print(test_example.fibonacci(-4), end="\n")
