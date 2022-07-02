#!/usr/bin/python3


<<<<<<< HEAD
from models.base_model import BaseModel

class User(BaseModel):
=======
import models

class User(models.base_model.BaseModel):
>>>>>>> ema
    """ user class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
