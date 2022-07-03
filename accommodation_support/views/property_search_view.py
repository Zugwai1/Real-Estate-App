from rest_framework.views import APIView


class PropertySearchView(APIView):
    def get(self, request, filter: str):
        ...