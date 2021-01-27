import datetime

def timer(func):
    start = datetime.datetime.now()
    def onCall(*args):
        result = func(*args)
        end = datetime.datetime.now()
        print(f'Ended in {(end - start).microseconds} microseconds')
        return result
    return onCall