from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    voornaam = models.CharField(max_length=100)
    achternaam = models.CharField(max_length=100)

    def __str__(self):
        template = '{0.voornaam} {0.achternaam}'
        return template.format(self)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['voornaam', 'achternaam']
