import colorama
import inspect
print(inspect.ismodule(colorama))
print(callable(colorama))
for method in dir(colorama):
    print(method)
print(inspect.ismodule(colorama.init))
print(callable(colorama.init))
for method in dir(colorama.init):
    print(method)
