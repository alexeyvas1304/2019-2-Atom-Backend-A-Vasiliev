from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db.models import Q
from users.models import User
from chats.models import Chat, Member
from message.models import Message
from attachments.models import Attachment
from attachments.forms import UploadAttachmentForm #, DownloadAttachmentMessageForm
from django.core.files.images import ImageFile
import magic


@csrf_exempt
@require_http_methods(["POST"])
def upload_attachment(request):
    form = UploadAttachmentForm(request.POST)
    if form.is_valid():
        print("hhh")
        user_id = request.POST["user_id"]
        user = get_object_or_404(User, id=user_id)
        chat_id = request.POST["chat_id"]
        chat = get_object_or_404(Chat, id=chat_id)

        member = Member.objects.filter(Q(user_id=user_id) & Q(chat_id=chat_id))
        if len(member) == 0:
            return JsonResponse({"response": "user not in chat"})

        message = Message.objects.create(user_id=int(user_id), chat_id=chat_id, content="вложение") ####
        chat.last_message_id = message.id
        chat.save()

        members = Member.objects.filter(chat_id=chat.id)
        for member in members:
            if member.user_id == int(user_id):
                member.new_messages = 0
                member.last_read_message_id = message.id
            else:
                member.new_messages += 1
            member.save()

        attachment = Attachment.objects.create(user_id=int(user_id), chat_id=int(chat_id), message_id=int(message.id))
        url = request.POST["url"]
        attachment.url = url

        a = magic.from_buffer((open(url, "rb")).read(), mime=True)
        attachment.type_of_attachment = a
        attachment.data = ImageFile(open(url, "rb"))
        attachment.save()

        print(form.errors)
        return JsonResponse({"response": "ok"})
    return JsonResponse({'errors': form.errors}, status=400)
#
#
@csrf_exempt
@require_http_methods(["GET"])
def download_attachment(request, url=None):
    attachments = Attachment.objects.filter(url=url)
    urls = []
    for attachment in attachments:
        urls.append(attachment.data.url)
    response = []
    for url in urls:
        response.append("<img src={}>".format(url))
    return HttpResponse("".join(response))
