from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from users.models import User
from chats.models import Chat, Member
from django.contrib.auth.decorators import login_required
# формы


@csrf_exempt
@require_http_methods(["POST"])
@login_required
def change_user_profile(request):
    request.user.name = request.POST["name"]
    request.user.nick = request.POST["nick"]
    request.user.avatar = request.POST["avatar"]
    request.user.save()
    return JsonResponse({'response': 'ok'})


@csrf_exempt
@require_http_methods(["GET"])
@login_required
def search_users(request, nick=None):
    if nick is None:
        return JsonResponse({})
    res = list(User.objects.filter(nick__contains=nick).values('id', 'name', 'nick', 'avatar', 'username'))
    return JsonResponse({"response": res})


@csrf_exempt
@require_http_methods(["GET"])
@login_required
def get_user_profile(request):
    return JsonResponse({"response": {
        "id": request.user.id,
        "name": request.user.name,
        "nick": request.user.nick,
        "avatar": request.user.avatar,
        "data_joined": request.user.date_joined
    }})


@csrf_exempt
@require_http_methods(["GET"])
@login_required
def get_user_chats(request):
    chats = Chat.objects.filter(members__user_id=request.user.id).values()
    return JsonResponse({"response": list(chats)})


@csrf_exempt
@require_http_methods(["GET"])
@login_required
def get_user_contacts(request):
    chats = Chat.objects.filter(members__user_id=request.user.id)
    list_of_contacts = []
    for us in User.objects.all():
        if us != request.user:
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


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')

