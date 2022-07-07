from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accommodation_support.providers import accommodation_app_provider
from auth_app.views.view_decorators import is_authenticated


class PropertySearchView(APIView):
    @is_authenticated
    def get(self, request, filter: str):
        response = accommodation_app_provider.property_service().search(filter)
        if response.status:
            return Response(data=response.__dict__, status=status.HTTP_200_OK)
        return Response(data=response.__dict__, status=status.HTTP_400_BAD_REQUEST)
