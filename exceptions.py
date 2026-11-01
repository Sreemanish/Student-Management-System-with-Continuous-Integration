class InvalidAgeError(Exception):
    """Raised when age is invalid."""
    pass


class InvalidMarkError(Exception):
    """Raised when mark is outside valid range."""
    pass


class DuplicateStudentError(Exception):
    """Raised when student ID already exists."""
    pass


class StudentNotFoundError(Exception):
    """Raised when student cannot be found."""
    pass
