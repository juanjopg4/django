from django import forms
from django.core import validators

class formArticle(forms.Form):
    
    title = forms.CharField(
        label='Título',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Introduzca el titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(5,'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ñ]*$', message='El titulo esta mal formado')
        ]
        
    )

    content = forms.CharField(
        label='Contenido',
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20,'Mucho texto')
        ]
    )

    content.widget.attrs.update({
        'placeholder':'Introduzca el contenido',
        'class':'contenido_form_article'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = '¿Publicado?',
        choices = public_options
        
    )    
