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


import unittest
import PatternPy.registry

class DummyMeta(type):pass
class DummyBase(object):
    __metaclass__ = DummyMeta

class TestRegister(unittest.TestCase):

    def setUp(self,):
        pass


    def test_two_anonymous_registries_are_distinct(self,):
        reg1 = PatternPy.registry.NamedRegistry()
        reg2 = PatternPy.registry.NamedRegistry()
        self.assertIsNot(reg1,reg2)
        self.assertIsNot(reg1.REGISTRY,reg2.REGISTRY)

    def test_a_registry_is_valid_metaclass(self,):
        class X(object):
            __metaclass__  = PatternPy.registry.NamedRegistry()

    def test_a_registry_uses_specified_base_class(selfm):
        class X(DummyBase):
            __metaclass__  = PatternPy.registry.NamedRegistry(base_meta=DummyMeta)


    def test_a_registry_records_all(self,):
        class A(object):
            __metaclass__  = PatternPy.registry.NamedRegistry()

        class B(A):pass

        #Whitebox;
        self.assertEquals(len(A.REGISTRY),2)

        ##Blackbox
        self.assertEquals(A.get_registered("B"),B)
        self.assertEquals(A.get_registered("A"),A)



    def test_a_registry_records_subclasses_if_base_class_excluded(self,):
        class A(object):
            __metaclass__  = PatternPy.registry.NamedRegistry()
            exclude_from_registry = True

        class B(A):pass

        #Whitebox;
        self.assertEquals(len(A.REGISTRY),1)

        ##Blackbox
        self.assertEquals(A.get_registered("B"),B)
        with self.assertRaises(KeyError):
            A.get_registered("A")



    def test_a_registry_excluded_marked_subclasses(self,):
        # I'm not sure this is a particularly meaning full test 
        # compared tot the two above.
        class A(object):
            __metaclass__  = PatternPy.registry.NamedRegistry()

        class B(A):
            exclude_from_registry = True

        #Whitebox;
        self.assertEquals(len(A.REGISTRY),1)

        ##Blackbox
        self.assertEquals(A.get_registered("A"),A)
        with self.assertRaises(KeyError):
            A.get_registered("B")



    def test_a_registry_handle_exclude_false_marking(self,):
        # I'm not sure this is a particularly meaning full test 
        # compared tot the two above.
        class A(object):
            __metaclass__  = PatternPy.registry.NamedRegistry()

        class B(A):
            exclude_from_registry = False

        #Whitebox;
        self.assertEquals(len(A.REGISTRY),2)

        ##Blackbox
        self.assertEquals(A.get_registered("B"),B)
        self.assertEquals(A.get_registered("A"),A)


