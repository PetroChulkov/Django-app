from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, ModelChoiceField, ModelMultipleChoiceField, Select, SelectMultiple
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=3000, required=False, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all(), widget=Select())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=SelectMultiple())

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
        exclude = []

class AuthorForm(ModelForm):

    fullname = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    borndate = DateField(required=True, widget=DateInput())
    location = CharField(max_length=50, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())


    class Meta:
        model = Author
        fields = ['fullname', 'borndate', 'location', 'description']

class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['name']