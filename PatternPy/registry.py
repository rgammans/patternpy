#! /usr/bin/env python
#
# MIT License
# 
# Copyright (c) 2017 Roger Gammans
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


def NamedRegistry( name = "NewRegistry", base_meta = type ):
    """Returns a newly created class usable as a registry system, for a 
    registered set of classes.

    Use by Creating a custom base class for each registry and assign
    the return value as it's metaclass.

    The exclude_from_registry attribute can be assigned to a class to 
    prevebt it from being added to the registry

    Example:
   
    class ObjectTypes(object):
        __metaclass__ = NamedRegistry("ShapeRegistry")
        exclude_from_registry = True
        ...

    """
    #Create a variable in the funciton closure for  new class.
    # which is needed for the py2 super.
    new_base= None
    def __new__(cls, name, bases, attrs):
        ## TODO Use six to py2/3 compat
        new_cls = super(new_base, cls ).__new__(cls, name, bases, attrs )

        if 'exclude_from_registry' not in attrs or not attrs['exclude_from_registry']:
            cls.REGISTRY[name] = new_cls
        return new_cls

    def get_registered(self,named):
        """Find an entry in the registry by it's registered name"""
        return self.REGISTRY[named]


    new_base =  type(name,(base_meta,),{
        "get_registered":get_registered,
        "__new__":__new__,
        "REGISTRY":dict(), })


    return new_base
