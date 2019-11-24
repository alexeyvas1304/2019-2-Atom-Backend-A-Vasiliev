from django import forms


class SendMessageForm(forms.Form):
    user_id = forms.IntegerField()
    chat_id = forms.IntegerField()
    content = forms.CharField(max_length=5000)


class ReadMessageForm(forms.Form):
    user_id = forms.IntegerField()
    chat_id = forms.IntegerField()
