# coding: utf-8

# The model module contains all the models class used in the project.
# In most of the times a class extends from ModelBase like the example:
#
# class Post(ModelBase):

#   ... sql fields
#
# The class ModelBase contains utils methods that is used
# for all sub classes like:
#   class Post(ModelBase):
#   .. sql fields
#       def to_dict():
#           return {}
# which returns a dict containing all the fields in the class,this is very
# helpful when building a api
