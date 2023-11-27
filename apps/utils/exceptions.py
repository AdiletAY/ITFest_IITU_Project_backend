from rest_framework.exceptions import APIException


class ApplicationNotFound(APIException):
    status_code = 404
    default_detail = "The specified Application does not exist"
    default_code = "application_not_found"


class IncorrectCredentials(APIException):
    status_code = 400
    default_detail = "The login or password is incorrect or something went wrong!"
    default_code = "incorrect_credentials"


class NotAllowed(APIException):
    status_code = 403
    default_detail = "You cannot apply more than once!"
    default_code = "not_allowed"
