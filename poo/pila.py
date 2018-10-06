from wrapper import Wrapper


class Pila(list):

    def __init__(self, max_size=10):
        super().__init__()

    def size(self):
        return len(self)

    def push(self, obj):
        super().append(obj)

    def pop(self):
        #last_eleme = super().pop()
        #print("Pop => ", last_eleme)
        return super().pop()

    def top(self, obj):
        return self[-1]

    def empty(self):
        return len(self) == 0

    def clear(self):
        super().clear()

    def __getattr__(self, attr):
        print('__getattr__ => ', attr)
        super().__getattr__(attr)


pila = Wrapper(Pila, props=['size', 'push'])
print(pila.size())
pila.push(9)
pila.push(6)
pila.push(2)
pila.push(8)
pila.push(1)
pila.push(3)
while not pila.empty():
    print('sacando {}'.format(pila.pop()))



pila.push(9)
pila.push(6)
pila.push(2)
pila.push(8)
pila.push(1)
pila.push(3)

pila.clear()