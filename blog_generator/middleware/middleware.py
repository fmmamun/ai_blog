

from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddlewareForBlogGenerator:
    EXCLUDED_URLS = [
        reverse('login'),
        reverse('signup'),
        # '/admin/',  # Exclude admin URLs
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # if not request.user.is_authenticated and not any(request.path.startswith(url) for url in self.EXCLUDED_URLS):
        if not request.user.is_authenticated and request.path not in self.EXCLUDED_URLS:
            return redirect('login')
        
        response = self.get_response(request)
        return response
