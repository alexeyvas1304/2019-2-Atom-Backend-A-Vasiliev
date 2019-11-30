from django import forms


class UploadAttachmentForm(forms.Form):
    chat_id = forms.IntegerField()
    url = forms.CharField()


