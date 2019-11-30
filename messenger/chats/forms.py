from django import forms


class CreateChatForm(forms.Form):
    topic = forms.CharField(max_length=60)
    first_message = forms.CharField(max_length=5000)


class AddUserForm(forms.Form):
    invited_user_id = forms.IntegerField()
    chat_id = forms.IntegerField()
