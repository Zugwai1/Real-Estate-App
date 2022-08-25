from coreapi.compat import force_text
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.response import Response

from auth_app.auth.token_generator import account_activation_token


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({"message": 'Thank you for your email confirmation. Now you can login your account.', 'passed': True},
                        status=status.HTTP_200_OK)
    else:
        return Response({"message": 'Activation link is invalid or has been used!', 'passed': False}, status=status.HTTP_404_NOT_FOUND)
