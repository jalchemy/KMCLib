""" Module containing error handling. """


# Copyright (c)  2012  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#


from exceptions import Exception


class Error(Exception):
    """ Class for describing an error. """

    def __init__(self, msg=''):
        """
        Constructor for the error class.

        @param msg: A message to the user describing what went wrong.
        @type     : String
        @default  : An empty string.
        """
        self.__msg = msg

    def __str__(self):
        """ Get a string representation of the error. """
        return self.__msg

