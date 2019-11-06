from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
@require_http_methods(["GET"])
def profil(request, pk=None):
    if pk is not None:
        return render(request, 'common.html')
    return JsonResponse({'test': 'profil'})


@csrf_exempt
@require_http_methods(["GET"])
def contacts(request):
    return JsonResponse({'test': 'contacts'})
