from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from django.contrib.auth import authenticate, login


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'user_id': user.id, 'username': user.username, 'email': user.email})
        return Response({'error': 'Invalid credentials'}, status=HTTP_401_UNAUTHORIZED)