from .models import property
from django import forms


class PropertyForm(forms.ModelForm):
    class Meta:
        model = property

        fields = ["name", "type", "email", "choice","date_of_viewing", "messages" ]