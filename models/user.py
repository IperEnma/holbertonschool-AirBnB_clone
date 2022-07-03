#!/usr/bin/python3
""" user class """

import models


class User(models.base_model.BaseModel):
    """ user class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
