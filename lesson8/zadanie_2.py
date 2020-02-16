# from inspect import isfunction


# class Pep8Warrior:
#     def __new__(cls, *args, **kwargs):
#         name, parents, attrs = args
#         new_name = name.title().replace('_', '')
#         new_attrs = {}
#         print(new_name)
#         for attr, value in attrs.items():
#             if attr.startswith('__'):
#                 new_attrs[attr] = value
#             elif isfunction(value):
#                 new_attrs[attr.lower()] = value
#             elif callable(value):
#                 new_attrs[attr.title().replace('_', '')] = value
#             else:
#                 new_attrs[attr.upper()] = value
#         return type(new_name, parents, new_attrs)


# class my_class:
#     x = 1
#     __metaclass__ = Pep8Warrior

#     class my_AmAzInG_cLaSs:
#         pass

#     def FuNc(self):
#         return 5

#     def __str__(self):
#         return 'hello'

#     @classmethod
#     def second(cls): #classmethod
#         pass


#     @staticmethod
#     def third():  #
#         pass

#     def get_x_plus_one(self):
#         return self.x + 1

#     @property
#     def x_plus_one(self): #property
#         return self.x + 1


# obj = my_class()
# print(my_class.__name__)
# print(obj.x)
# # print(obj.X)  # correct
# # print(obj.Y)  # correct
# # # print(obj.FuNc())
# # print(obj.func())  # correct
# # print([attr for attr in dir(obj) if not attr.startswith('__')])

from inspect import isfunction
import inspect


class Pep8Warrior:
    def __new__(cls, *args, **kwargs):
        name,parents, attrs = args
        new_name = f'Decorated{name}'
        at = {}
        new_attrs = {}
        for attr, value in attrs.items():
            if attr.startswith('_'):
                at[attr] = value 
            elif isfunction(value):
                new_attrs[attr] = value      
        atters_of_decorators = {}
        print(new_attrs)
        for attr, value in new_attrs.items():
            list_of_args = list(inspect.signature(value).parameters.keys())
            if list_of_args == ['self']:
                value = property(value)
                atters_of_decorators[attr] = value
            elif list_of_args == ['cls']:
                value = classmethod(value)
                atters_of_decorators[attr] = value
            elif list_of_args == []:
                value = staticmethod(attr)
                atters_of_decorators[attr] = value 
        result = {**at,**atters_of_decorators}
        print()
        print(result)
        

                
        return type(new_name, parents, result)


class MyClass(metaclass = Pep8Warrior):
    def __init__(self, x):
        self.x = x

    def first(self):
        pass

    
    def second(cls):
        pass

    
    def third():
        print(5)

    def get_x_plus_one(self):
        return self.x + 1

    
    def x_plus_one(self):
        return self.x + 1


obj = MyClass(5)

# print(my_class.__name__)
# print(obj)
# # print(obj.x)
# print(obj.X)  # correct
# print(obj.Y)  # correct
# # print(obj.FuNc())
obj.third()
