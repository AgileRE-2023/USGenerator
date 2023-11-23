from django.shortcuts import redirect


class RedirectIfAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == '/':
            return redirect('client:dashboardClient')

        response = self.get_response(request)
        return response
