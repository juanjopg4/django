from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(value):
    return (f'<h1 style="background:green;color:white;"> Bienvenido {value}!!</h1>')
    
        