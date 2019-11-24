from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db.models import Q
from users.models import User
from chats.models import Chat, Member
from message.models import Message
from attachments.models import Attachment
from chats.forms import CreateChatForm, AddUserForm


@csrf_exempt
@require_http_methods(["POST"])
def create_chat(request):

    form = CreateChatForm(request.POST)
    if form.is_valid():
        user_id = request.POST["user_id"]

        user = get_object_or_404(User, id=user_id)

        chat = Chat.objects.create(topic=request.POST["topic"])
        message = Message.objects.create(user_id=int(user_id), chat_id=chat.id, content=request.POST["first_message"])
        chat.last_message_id = message.id
        chat.save()
        member = Member.objects.create(user_id=user_id, chat_id=chat.id, last_read_message_id=message.id)
        return JsonResponse({"response": "ok"})
    return JsonResponse({'errors': form.errors}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def add_user_to_chat(request):
    form = AddUserForm(request.POST)
    if form.is_valid():
        inviting_user_id = request.POST["inviting_user_id"]
        inviting_user = get_object_or_404(User, id=inviting_user_id)
        invited_user_id = request.POST["invited_user_id"]
        invited_user = get_object_or_404(User, id=invited_user_id)
        chat_id = request.POST["chat_id"]
        chat = get_object_or_404(Chat, id=chat_id)

        inviting_member = Member.objects.filter(Q(user_id=inviting_user_id) & Q(chat_id=chat_id))
        if len(inviting_member) == 0:
            return JsonResponse({"response": "inviting user not in chat"})

        invited_member = Member.objects.filter(Q(user_id=invited_user_id) & Q(chat_id=chat_id))
        if len(invited_member) != 0:
            return JsonResponse({"response": "invited user is already in chat"})

        member = Member.objects.create(user_id=invited_user_id, chat_id=chat_id, last_read_message_id=chat.last_message_id)
        chat.is_group_chat = True
        chat.save()
        return JsonResponse({"response": "user is successfully invited"})
    return JsonResponse({'errors': form.errors}, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_messages(request, chat_id=None):
    # надо ли это ? Тогда надо править urls.py
    # if chat_id is None:
    #     return JsonResponse({"response": "chat_id is None"})

    chat = get_object_or_404(Chat, id=chat_id)

    messages = list(Message.objects.all().filter(chat=chat_id).values())
    attachments = list(Attachment.objects.all().filter(chat=chat_id).values())  # ???

    return JsonResponse({"response": messages+attachments})


@csrf_exempt
@require_http_methods(["GET"])
def get_chat_page(request, chat_id=None):
    # надо ли это ? Тогда надо править urls.py
    # if chat_id is None:
    #     return JsonResponse({"response": "chat_id is None"})

    chat = get_object_or_404(Chat, id=chat_id)

    return JsonResponse({"response": {
        "id": chat_id,
        "topic": chat.topic,
        "is_group_chat": chat.is_group_chat,
        "last_message_id": chat.last_message_id,
    }})
