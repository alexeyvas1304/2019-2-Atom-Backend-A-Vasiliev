from django import forms


class UploadAttachmentForm(forms.Form):
    user_id = forms.IntegerField()
    chat_id = forms.IntegerField()
    url = forms.CharField()
    # content = forms.CharField(max_length=5000)


# class downloadAttachmentForm(forms.Form):
#     user_id = forms.IntegerField()
#     chat_id = forms.IntegerField()