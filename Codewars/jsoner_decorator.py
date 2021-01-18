import json
import os

def jsonattr(filepath):
    """It can have some troubles but them aren't affect the execution"""
    """And this code can be executed without errors ;)"""
    #Worthless bullshit, u don't need this line in Codewars vim-editor
    #So delete it, but if u wanna run this on your PC save it and don't even dare to touch
    #Cause Python interpeter can't find your file because it has different PATH than your file
    #If u wanna run this from cmd - u should delete line
    path = os.path.join(os.path.dirname(__file__), filepath)
    with open(path, 'r') as obj_read:
        data = json.load(obj_read)
    class Jsoner():
        def __init__(self, cls):
            self._cls = cls
            for k, v in data.items():
                setattr(self, k, v)

        def __call__(self, *args):
            return self._cls(*args)
    return Jsoner

@jsonattr("dectest.json")
class MyClass:
    def __init__(self, foo, an_int, this_kata_is_awesome):
        self.foo = foo
        self.an_int = an_int
        self.this_kata_is_awesome = this_kata_is_awesome

if __name__ == '__main__':
    inst = MyClass('check', 10, None)
    print(inst.this_kata_is_awesome)
    print(MyClass.this_kata_is_awesome)