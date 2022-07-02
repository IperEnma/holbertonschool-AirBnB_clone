#!/usr/bin/python3
"""
class base model
"""

import uuid
import datetime
import models

class BaseModel():
    """
    defining the class
    """

    def __init__(self, *args, **kwargs):
        """ initialize class """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs['id']
                elif key == 'created_at':
                    self.created_at = datetime.datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ string representaion """
        return f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        """update public instance"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary"""
        new_dict = self.__dict__.copy()
        new_dict.update([('__class__', self.__class__.__name__)])
        for key, value in new_dict.items():
            if key == "created_at":
                new_dict.update([(key, value.isoformat())])
            elif key == "updated_at":
                new_dict.update([(key, value.isoformat())])
            else:
                new_dict.update([(key, value)])
        return new_dict

    def sett_atr(self, dic):
        """ set attr from dict """
        for key, value in dic.items():
            if key == 'created_at':
                self.created_at = datetime.datetime.strptime(dic['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            elif key == 'updated_at':
                self.updated_at = datetime.datetime.strptime(dic['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            elif key != '__class__':
                setattr(self, key, value)

