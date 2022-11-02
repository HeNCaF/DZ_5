# import requests
#
# def func():
#     pass
# class Human:
#     pass
# rq = requests
# func = func
# nick = Human
# print(requests.__name__)
# print(rq.__name__)
# print(func.__name__)
# print(nick.__name__)
# import tkinter
#
# list = []
# for method in dir(list):
#     print(method)
# for method in dir(tkinter.mainloop):
#     print(method)
# test = "string"
# print(hasattr(test, "reverse"))
# print(hasattr(test, "index"))
# test = "test"
# def func():
#     pass
# print(callable(test))
# print(callable(func))
# class Father:
#     pass
# class Son(Father):
#     pass
# obj_son = Son()
# print(issubclass(Father, Son))
# print(issubclass(Son, Father))
# print(isinstance(obj_son, Son))
# print(isinstance(obj_son, Father))
# for _ in dir(__buildtins__):
#     printr(_)
import colorama
import inspect
print(inspect.ismodule(colorama))
print(callable(colorama))
for method in dir(colorama):
    print(method)
