from django.http import JsonResponse


def user_logged_in(function):
    def wrap(request, *args, **kwargs):
        if  request.COOKIES.get('token'):
            return function(request, *args, **kwargs)
        else:
            return JsonResponse({"Error":"User not Logged in!"})
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap