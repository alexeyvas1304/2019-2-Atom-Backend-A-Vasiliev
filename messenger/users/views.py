from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from users.models import User
from chats.models import Chat, Member
# формы


@csrf_exempt
@require_http_methods(["GET"])
def search_users(request, nick=None):
    if nick is None:
        return JsonResponse({})
    res = list(User.objects.filter(nick__contains=nick).values('id', 'name', 'nick', 'avatar'))
    return JsonResponse({"response": res})


@csrf_exempt
@require_http_methods(["GET"])
def get_user_profile(request, user_id=None):
    # надо ли ?
    # if user_id is None:
    #     return JsonResponse({"response": "user_id is None"})

    user = get_object_or_404(User, id=user_id)

    return JsonResponse({"response": {
        "id": user_id,
        "name": user.name,
        "nick": user.nick,
        "avatar": user.avatar,
        "data_joined": user.date_joined
    }})


@csrf_exempt
@require_http_methods(["GET"])
def get_user_chats(request, user_id=None):
    # надо ли ?
    # if user_id is None:
    #     return JsonResponse({"response": "user_id is None"})

    user = get_object_or_404(User, id=user_id)

    chats = Chat.objects.filter(members__user_id=user_id).values()
    return JsonResponse({"response": list(chats)})


@csrf_exempt
@require_http_methods(["GET"])
def get_user_contacts(request, user_id=None):
    # надо ли ?
    # if user_id is None:
    #     return JsonResponse({"response": "user_id is None"})

    user = get_object_or_404(User, id=user_id)

    # возможно, не самый рациональный способ, но рабочий
    chats = Chat.objects.filter(members__user_id=user_id)
    list_of_contacts = []
    for us in User.objects.all():
        if us != user:
            chats_of_us = Chat.objects.filter(members__user_id=us.id)
            if set(chats & chats_of_us):
                list_of_contacts.append(us)

    return JsonResponse({"response": [{
        "id": contact.id,
        "name": contact.name,
        "nick": contact.nick,
        "avatar": contact.avatar,
        "data_joined": contact.date_joined
    } for contact in list_of_contacts]})
