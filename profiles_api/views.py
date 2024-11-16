from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from profiles_api import serializer

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializer.HelloSerializer
    def get(self,request, format=None):
        """Returns a list of APIView Feature"""
        an_apiview = [
            "Uses HTTP method as fucntion(get,post,patch,put,delete)",
            "is similar to a traditional Django View",
            "Gives you most control over your application",
            "Is mapped manually to URLs",

        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    

    def post(self,request, format=None):
        """Create POST request for hello API"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'messaage': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        
    def put(self,request,pk=None):
        """Create PUT request"""
        return Response({'method': "PUT"})
    
    def patch(self,request,pk=None):
        return Response({'method': "PATCH"})
    
    def delete(self,request, pk=None):
        return Response({'method': 'DELETE'})
        
    

