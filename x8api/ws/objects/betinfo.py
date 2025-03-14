#python
"""Module for X8 option Profile websocket object."""
from x8api.ws.objects.base import Base


class Game_betinfo_data(Base):
    """Class for X8 option Profile websocket object."""

    def __init__(self):
        super(Game_betinfo_data, self).__init__()
        self.__isSuccessful = None
        self.__dict = {}
 
    @property
    def isSuccessful(self):
        return self.__isSuccessful

    @isSuccessful.setter
    def isSuccessful(self, isSuccessful):

        self.__isSuccessful = isSuccessful
#--------------------------------------
    @property
    def dict(self):
        return self.__dict

    @dict.setter
    def dict(self, dict):
        self.__dict = dict
 

 