from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def services(request):
    return render(request, 'myapp/services.html')

def blog(request):
    return render(request, 'myapp/blog.html')

def portfolio(request):
    projects = [
        {'name':" Pagina de Restaurante", 'description': 'Proyecto para cadena de restaurantes chilenos', 'image':'https://media.vandal.net/i/1280x720/10-2023/17/202310171642263_4.jpg'},
        {'name':" Pagina de Inmobiliaria", 'description': 'Proyecto para venta de departamentos', 'image':'https://image.api.playstation.com/vulcan/ap/rnd/202211/2222/l8QTN7ThQK3lRBHhB3nX1s7h.png'},
        {'name':" Pagina de Escuela", 'description': 'Proyecto para Escuela de Psicologia', 'image':'https://cdn.sortiraparis.com/images/80/66131/1024452-star-wars-bientot-un-jeu-the-mandalorian-developpe-par-respawn-entertainment.jpg'},
    ]
    return render(request, 'myapp/portfolio.html', {'projects': projects})

def teams(request):
    return render(request, 'myapp/teams.html')

def testimonial(request):
    testimonial_data = [
        {'nombre':" Roberto", 'puesto':" CEO of MIT", 'testimonio':" Excelente servicio"},
        {'nombre':" Andrea", 'puesto':" CEO of MIT", 'testimonio':" Excelente servicio"},
        {'nombre':" Carlos", 'puesto':" CEO of MIT", 'testimonio':" Excelente servicio"},
    ]
    return render(request, 'myapp/testimonial.html', {'testimonial': testimonial_data})