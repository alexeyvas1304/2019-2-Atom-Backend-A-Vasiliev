from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["GET"])
def chat_list(request):
    return JsonResponse({'test': 'chat_list'})


@csrf_exempt
@require_http_methods(["GET"])
def chat_page(request):
    return JsonResponse({'test': 'chat_page'})

