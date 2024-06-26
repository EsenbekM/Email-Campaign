from rest_framework import status
from rest_framework.response import Response


class DeleteObjectMixin:
    def delete(self, request, *args, **kwargs):
        '''set is_active to False instead of deleting'''
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)