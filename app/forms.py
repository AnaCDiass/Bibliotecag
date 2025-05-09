#from django.views import TemplateView
#from django.shortcuts import FormHelper, Layout, Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib import messages
from .models import Livro

from django import forms

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        #fields = '__all__'
        fields = ['nome', 'autor', 'editora', 'genero', 'preco', 'data_plub', 'status']

    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',
            'autor',
            'editora',
            'genero',
            'preco',
            'data_pub',
            'status',
            Submit('submit', 'Salvar')
        )
