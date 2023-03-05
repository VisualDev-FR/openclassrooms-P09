from django import forms
from LITReview.models import UserFollows


class FollowForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        exclude = ['user']
