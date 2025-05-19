# core/middleware.py
from django.http import HttpResponseForbidden

class RoleAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        required_roles = getattr(view_func, 'required_roles', None)
        if required_roles and not request.user.role in required_roles:
            return HttpResponseForbidden()