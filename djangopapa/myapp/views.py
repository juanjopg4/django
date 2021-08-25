from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from myapp.models import Article
from myapp.forms import formArticle
from django.contrib import messages

layout = ('''
<h1> Sitio web con django | Juanjosé Pérez Guerrero</h1>
<hr/>
<ul>
    <li>
    <a href='/index'>Inicio</a>
    </li>
    <li>
    <a href='/productos'>Productos</a>
    </li>
    <li>
    <a href='/años'>años</a>
    </li>
    <li>
    <a href='/contacto'>contacto</a>
    </li>
</ul>
<hr/>
''')

# Create your views here.
def años(request):
    html = '''<h1>años hasta el 2050</h1>
    <ul>
    '''
    """
    years = 2020
    while years < 2050:
        html += f'<li>{years}</li>'
        years += 1
    html += '</ul>'

    """
    
    year = 2021
    hasta = range(year, 2051)



    nombre = 'Juanjo'
    lenguajes = ['python','django','html']


    return render(request, 'index.html',{
    'nombre':nombre,
    'lenguajes':lenguajes,
    'years':hasta
    

    })
    

def index(request):
    return render(request, 'home.html')

def Hola_mundo(request):
    return HttpResponse(layout + '''
    <h1>Hola mundo con django!!</h1>
    <h3>Esto es un texto de prueba</h3>
    ''')


def contacto(request,nombre='',apellido=''):
    nombreCompleto = ''
    email = '<h4>email:django@django.com<h4/>'
    if nombre and apellido:
        nombreCompleto = f'<h3>Nombre:{nombre} {apellido}<h3/>'
    return render(request, 'contacto.html')

    """
    HttpResponse(layout+f'''
    <h2>Contacto<h2/>
    {nombreCompleto}
    {email}
    ''')
    """


def CrearArticulo(request, title, content, public):

    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f'Usuario creado {articulo.title} - {articulo.content}')

def SaveArticulo(request):
    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content, 
            public = public
        )

        articulo.save()

        return HttpResponse(f'Usuario creado {articulo.title} - {articulo.content}')
    
    #else:
        #return HttpResponse('<h2>No ha sido posible crear el articulo</h2>')

    

def create_article(request):
    return render(request, 'create_article.html')

def Articulo(request):

    Articulo = Article.objects.get(id=7)

    
    return HttpResponse(f'Articulo:{Articulo.title}')

def EditarArticulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = 'canserbero'
    articulo.content = 'mundo de piedra'

    articulo.save()

    return HttpResponse(f'<h1>Titulo:{articulo.title} </br> Contenido: {articulo.content}</h1>')

def articulos(request):
    articulos = Article.objects.all()

    return render(request, 'articulos.html',{
        'articulos':articulos
    })

def EliminarArticulos(request,id):
    
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    
    return redirect('articulos')

def create_full_article(request): 

    if request.method == 'POST': 
        
        formulario = formArticle(request.POST)

        if formulario.is_valid():
            form_data = formulario.cleaned_data

            title = form_data['title']
            content = form_data['content']
            public = form_data['public']

            articulo = Article(
            title = title,
            content = content, 
            public = public
            )

            articulo.save()

            #crear mensaje flash
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('articulos')

            #comprobar que se guarde bien
            #return HttpResponse(articulo.title + '-' + articulo.content + '-' + str(articulo.public))
    
    else:
        formulario = formArticle()
    
    

    return render(request,'create_full_article.html',{
        'form':formulario
    })
    