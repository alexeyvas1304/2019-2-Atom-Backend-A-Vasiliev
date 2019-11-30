from django import forms


class SendMessageForm(forms.Form):
    chat_id = forms.IntegerField()
    content = forms.CharField(max_length=5000)


class ReadMessageForm(forms.Form):
    chat_id = forms.IntegerField()
