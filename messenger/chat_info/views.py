from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def chat_list(request):
    return JsonResponse({'test': 'chat_list'})
    

@require_http_methods(["GET"])
def chat_page(request):
    return JsonResponse({'test': 'chat_page'})

