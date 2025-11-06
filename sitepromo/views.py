from django.shortcuts import render

TEAM = [
    {"name": "Matías Aguayo Hernández", "role": "Líder de Proyecto - UI/UX", "img": "/static/sitepromo/img/team/team-matias.jpg"},
    {"name": "Álvaro Marchant Concha", "role": "Scrum Master", "img": "/static/sitepromo/img/team/team-alvaro.jpg"},
    {"name": "Sebastián Lagos Garces", "role": "Ingeniero de Datos", "img": "/static/sitepromo/img/team/team-seba.jpg"},
    {"name": "Bastián Berrios Pérez", "role": "Arquitectura de Software", "img": "/static/sitepromo/img/team/team-bastian.jpg"},
    {"name": "Javier Lucero Diaz", "role": "Encargado Backend", "img": "/static/sitepromo/img/team/team-javier.jpg"},
]

def home(request):
    return render(request, 'sitepromo/home.html', {"team": TEAM})

def legal(request):
    return render(request, 'sitepromo/legal.html')
