class Jar:
    def __init__(self, capacity=12):
        self.jar_count = 0
        self.capacity = capacity

    def __str__(self):
        return (self.size * "🍪")

    def deposit(self, n):
        for char in range(n):
            self.jar_count = self.jar_count + 1
        if self.size > self.capacity:
            raise ValueError


    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            for char in range(n):
                self.jar_count = self.jar_count - 1

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return (self.jar_count)


jar = Jar()
jar.deposit(6)
print(jar)
jar.withdraw(4)
print(jar)