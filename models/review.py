#!/usr/bin/python3
""" review class """


import models


class Review(models.base_model.BaseModel):
    """ class review """

    place_id = ""
    user_id = ""
    text = ""
