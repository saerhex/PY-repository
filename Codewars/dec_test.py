class Tracer:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args):
        self.calls += 1
        self.func(*args)

    def get_calls(self):
        print(f"Number of calls to {self.func.__name__} is {self.calls}")
    
@Tracer
def add(*args):
    return sum(args)


add(1,2,4,5,6,7)
add(11231,123231341,1321436583)
add(128380,3493294,9210239)
add.get_calls()