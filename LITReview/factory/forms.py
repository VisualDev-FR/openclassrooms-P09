from django import forms
from LITReview.models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['user', 'time_created']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10}),
        }

class ReviewForm(forms.ModelForm):

    headline = forms.CharField(label='Titre')    
    rating = forms.ChoiceField(
        label='Note',
        widget=forms.RadioSelect(attrs={'class':'rate'}),
        initial=0,
        choices=[
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
    )

    body = forms.CharField(label='Commentaire', widget=forms.Textarea())

    class Meta:
        model = Review
        exclude = ['user', 'time_created', 'ticket']


class Ticket_ReviewForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(TicketForm().fields)
        self.fields.update(ReviewForm().fields)
