from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(
                {"detail": "You are already registered and logged in please log out to access the registrations."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().post(request, *args, **kwargs)
     