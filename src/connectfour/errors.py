"""Typed exceptions for ConnectFour."""


class connectfourError(Exception):
 """Base error for the whole package."""

 exit_code = 1


class ConfigurationError(connectfourError):
 """Raised when configuration is invalid or missing."""

 exit_code = 2


class ValidationError(connectfourError):
 """Raised when input data fails validation."""

 exit_code = 3


class NotFoundError(connectfourError):
 """Raised when a requested resource does not exist."""

 exit_code = 4


class ConflictError(connectfourError):
 """Raised when an operation conflicts with existing state."""

 exit_code = 5


class RateLimitError(connectfourError):
 """Raised when a rate limit is exceeded."""

 exit_code = 6


class TimeoutError(connectfourError):
 """Raised when an operation takes too long."""

 exit_code = 7


class UnsupportedError(connectfourError):
 """Raised for unsupported inputs or platforms."""

 exit_code = 8


class StateError(connectfourError):
 """Raised when internal state is inconsistent."""

 exit_code = 9


def guard(condition, message, exc=ValidationError):
 """Raise exc(message) when condition is False."""
 if not condition:
 raise exc(message)