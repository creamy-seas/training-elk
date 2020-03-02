from async_request import run_logger


class Typing():
    def __init__(name, str):
        print(name)
        
    @run_logger
    def hello():
        print('hello')

g = Typing('bruce')
g.hello()
