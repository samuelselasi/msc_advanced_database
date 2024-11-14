#!/usr/bin/python3
"""Module that defines error response messages"""


class BaseException(Exception):
    """Class that defines base exceptions"""

    def __init__(self, message: str = None):
        """Function that initializes error response messages"""

        self.message = message

    def _message(self):
        """Function that returns error message"""

        return self.message


class NotFoundError(BaseException):
    """Class that passes error message for NotFoundError"""
    pass


class UnAcceptableError(BaseException):
    """Class that passes error message for UnacceptableError"""
    pass


class UnAuthorised(BaseException):
    """Class that passes error message for UnAuthorised"""
    pass


class ExpectationFailure(BaseException):
    """Class that passes error message for ExpectationFailure"""
    pass


class FileReadFailed(BaseException):
    """Class that passes error message for FileReadFailed"""
    pass


class FileNameError(BaseException):
    """Class that passes error message for FileNameError"""
    pass


class MaxOccurrenceError(BaseException):
    """Class that passes error message for MaxOccurenceError"""
    pass


class CreateFolderError(BaseException):
    """Class that passes error message for CreateFolderError"""
    pass
