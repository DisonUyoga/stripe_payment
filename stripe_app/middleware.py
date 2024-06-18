# your_app/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class AdminCsrfExemptMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith(settings.ADMIN_URL):
            setattr(request, '_dont_enforce_csrf_checks', True)
