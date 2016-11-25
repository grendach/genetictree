from django.contrib.auth.models import User
from django import forms



from .models import Family, Person


class FamilyForm(forms.ModelForm):

    class Meta:
        model = Family
        fields = ['family_name', 'family_location', 'family_logo']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['family', 'first_name', 'second_name', 'person_photo', 'date_of_birth', 'person_descr', 'date_of_death', 'lives_in', 'is_married']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name','password']

