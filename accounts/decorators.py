from django.shortcuts import redirect
from django.contrib import messages


def role_required(allowed_roles):

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:

                return redirect('login')

            if not hasattr(request.user, 'profile'):

                messages.error(
                    request,
                    'Profile not found.'
                )

                return redirect('home')

            if request.user.profile.role not in allowed_roles:

                messages.error(
                    request,
                    'You do not have permission to access this page.'
                )

                return redirect('home')

            return view_func(
                request,
                *args,
                **kwargs
            )

        return wrapper

    return decorator