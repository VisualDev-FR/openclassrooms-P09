from django import forms
from factory.models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['user', 'time_created']