#coding: utf-8

from sqlobject import SQLObject

__author__ = 'iury'
__all__ = ['ModelBase']


class ModelBase(SQLObject):
    '''
    Base class for model classes

    if you need to override the __init__ method don't call Parent.__init__ instead call
    Parent._init(self, *args, **kwargs) or in a better way
    super(class, self)._init(self, *args, **kwargs)
    This is needed because sqlobject already uses the __init__ to create the object

    for future references: http://sqlobject.org/SQLObject.html#declaring-the-class
    '''

    def _init(self, *args, **kwargs):
        '''
        init method, if needed should be call in place of __init__ with the parameters:
            self, *args, **kwargs
        '''
        SQLObject._init(self, *args, **kwargs)

    def to_dict(self):
        '''
        return a dictionary with the the class attributes or a empty dictionary
        '''
        return {}

