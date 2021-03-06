from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db.models import Q
from chats.models import Chat, Member
from message.models import Message
from message.forms import SendMessageForm, ReadMessageForm
from django.contrib.auth.decorators import login_required


@csrf_exempt
@require_http_methods(["POST"])
@login_required
def send_message(request):
    form = SendMessageForm(request.POST)
    if form.is_valid():
        chat_id = request.POST["chat_id"]
        chat = get_object_or_404(Chat, id=chat_id)

        member = Member.objects.filter(Q(user_id=request.user.id) & Q(chat_id=chat_id))
        if len(member) == 0:
            return JsonResponse({"response": "user not in chat"})

        message = Message.objects.create(user_id=request.user.id, chat_id=chat_id, content=request.POST["content"])
        chat.last_message_id = message.id
        chat.save()

        members = Member.objects.filter(chat_id=chat.id)
        for member in members:
            if member.user_id == request.user.id:
                member.new_messages = 0
                member.last_read_message_id = message.id
            else:
                member.new_messages += 1
            member.save()
        return JsonResponse({"response": "ok"})
    print(form.errors)
    return JsonResponse({'errors': form.errors}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
@login_required
def read_message(request):
    form = ReadMessageForm(request.POST)
    if form.is_valid():
        chat_id = request.POST["chat_id"]
        chat = get_object_or_404(Chat, id=chat_id)

        member = list(Member.objects.filter(Q(user_id=request.user.id) & Q(chat_id=chat_id)))
        if len(member) == 0:
            return JsonResponse({"response": "user not in chat"})

        member[0].new_messages = 0
        member[0].last_read_message_id = chat.last_message_id
        member[0].save()

        return JsonResponse({"response": "ok"})
    return JsonResponse({'errors': form.errors}, status=400)
