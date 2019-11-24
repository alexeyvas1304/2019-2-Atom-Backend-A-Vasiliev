from django import forms


class CreateChatForm(forms.Form):
    user_id = forms.IntegerField()
    topic = forms.CharField(max_length=60)
    first_message = forms.CharField(max_length=5000)


class AddUserForm(forms.Form):
    inviting_user_id = forms.IntegerField()
    invited_user_id = forms.IntegerField()
    chat_id = forms.IntegerField()
