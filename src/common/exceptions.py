from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class ObjectNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Not found")
    default_code = "notFound"


class UniqueObjectException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _("Must be unique")
    default_code = "uniqueObjects"


class NothingToDoException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _("Nothing to do")
    default_code = "nothinToDo"


class ObjectDeletedException(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = _("Deleted")
    default_code = "deleted"


class TypeErrorException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Type error validation")
    default_code = "typeError"


class IncorrectPasswordException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Incorrect password error")
    default_code = "invalidPassword"


class AlreadyExist(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _("Already exist")
    default_code = "alreadyExist"


class UnkownException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _("A server error occurred.")
    default_code = "error"


class RequiredFieldException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Required field error")
    default_code = "fieldRequired"


class RequiredQueryException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Required query param error")
    default_code = "queryParamRequired"
