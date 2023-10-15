#!/usr/bin/python3
"""Defines the state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    child class of BaseModel
    represents a state, takes one attr - name of the state
    """
    name = ""
