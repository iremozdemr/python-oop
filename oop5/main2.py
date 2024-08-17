class Numbers1:
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        self.a += 1
        return self.a
    
object1 = Numbers1()
iterator1 = iter(object1)

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))


class Numbers2:
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        if self.a <= 5:
            self.a += 1
            return self.a
        else:
            raise StopIteration
#iterasyonu durdurma
    
object2 = Numbers2()
iterator2 = iter(object2)

print(next(iterator2))
print(next(iterator2))
print(next(iterator2))