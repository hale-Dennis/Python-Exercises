
class FibIterator:

    def __init__(self, limit):
        self.fib_series = [0,1]
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self
    

    def __next__(self):
        try:
            if self.count != self.limit:
                if self.count <=1:
                    self.count += 1
                    return self.fib_series[self.count-1]
                else:
                    new_item = self.fib_series[self.count -1] + self.fib_series[self.count -2]
                    self.fib_series.append(new_item)
                    self.count += 1
                    return new_item
            else: 
                raise StopIteration
        except StopIteration as e:
            print(e.__str__())
        
fib = FibIterator(10)
it = iter(fib)

print(next(it))
for i in it:
    print(i)