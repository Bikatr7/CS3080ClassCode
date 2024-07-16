from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('/admin/')



@api_view(["POST"])
def loginView(request, *args, **kwargs):
    username = request.POST.get("username")
    password = request.POST.get("password")
    try:
        user = authenticate(username=username,
                            password=password)
    except:
        user = None
    if not user:
        return Response({
            "user_not_found": "There is no user \
            with this username and password !"
        })
    token = Token.objects.get(user=user)
    return Response({
        "token": token.key,
    })
