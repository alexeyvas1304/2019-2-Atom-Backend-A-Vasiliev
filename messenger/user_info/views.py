from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def profil(request):
    return JsonResponse({'test': 'profil'})


@require_http_methods(["GET"])
def contacts(request):
    return JsonResponse({'test': 'contacts'})
