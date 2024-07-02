"""
Custom exceptions for the Student Data Management Program.
"""

class NoMatchingNameError(Exception):
    """
    Exception raised when no matching name is found.
    """
    def __init__(self, name, message="No matching name found"):
        self.name = name
        self.message = message
        super().__init__(self.message)

class NoMatchingIdError(Exception):
    """
    Exception raised when no matching ID is found.
    """
    def __init__(self, id, message="No matching ID found"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class AuthenticationError(Exception):
    """
    Exception raised when authentication fails.
    """
    def __init__(self, message="Authentication failed"):
        self.message = message
        super().__init__(self.message)
