def main():

    #Q1
    x, y, z, *k = range(5)
    # What would you see print(k)?
    #print(k)

    #Q2
    a = '123456'
    b = a[1] + a[3]
    # What would you see with print(b)
    #print(b)

    #Q3
    a, b = 1_2_3, 4
    # What would you see with print(a*b)
    #print(a*b)

    #Q4
    data = {True, 1, not False}
    # What would you see with print(len(data))
    #print(len(data))

    #Q5
    x = True
    y = x + 2
    # What would you see with print(y-1)
    #print(y-1)

    #Q6
    queue = [3, 7, 1, 8].sort()
    # What would you see with print(queue[0])
    #print(queue[0])

    #What can you tell me about Apache, Nginx, HAProxy
    # Why is Nginx it so used?
    # 4) Explain how Nginx can handle HTTP requests?
    # Nginx uses the reactor pattern.  The main event loop waits for the OS to signal a readiness event-
    # such that the data is accessible to read from a socket, at which instance it is read into the buffer and processed.
    # A Single thread can serve tens of thousands of simultaneous connections.

    class BaseClass:
        def __init__(self):
            self.__i = 1
            self.j = 5

        def display(self):
            print(self.__i, self.j)

    class DerivedClass(BaseClass):
        def __init__(self):
            super().__init__()
            self.__i = 2
            self.j = 7

    # What will be displayed?
    var = DerivedClass()
    var.display()


if __name__ == '__main__':
    main()
