from django import forms
from django.forms import widgets
from webapp.models import Album, Photo

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name','description', 'private')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'signature', 'private')

    # def __init__(self, *args, **kwargs):
    #     super(PhotoForm, self).__init__(*args, **kwargs)
    #     self.fields['photo'].required = False


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')
