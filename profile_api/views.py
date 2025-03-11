from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methodss as function (get, poet, patch,delete)'
            'Is similar to a traditional django view.'
            'Gives you thee most control over your appliication project.'
            'Is mapped manually to URLs.',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

