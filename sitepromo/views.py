from django.shortcuts import render

TEAM = [
    {"name": "Matías Aguayo Hernández", "role": "Líder de Proyecto - UI/UX", "img": "/static/sitepromo/img/team/team-matias.jpg"},
    {"name": "Álvaro Marchant Concha", "role": "Scrum Master", "img": "/static/sitepromo/img/team/team-alvaro.jpg"},
    {"name": "Sebastián Lagos Garces", "role": "Ingeniero de Datos", "img": "/static/sitepromo/img/team/team-seba.jpg"},
    {"name": "Bastián Berrios Pérez", "role": "Arquitectura de Software", "img": "/static/sitepromo/img/team/team-bastian.jpg"},
    {"name": "Javier Lucero Diaz", "role": "Encargado Backend", "img": "/static/sitepromo/img/team/team-javier.jpg"},
]

def home(request):
    # Activa/Desactiva modo streaming para el día de la feria
    LIVE_STREAM_ACTIVE = True  # <-- cámbialo a True cuando haya transmisión
    LIVE_STREAM_URL = "https://www.youtube.com/watch?v=__9losSphCg"  # pon aquí tu enlace real

    return render(request, "sitepromo/home.html", {
        "team": TEAM,
        "LIVE_STREAM_ACTIVE": LIVE_STREAM_ACTIVE,
        "LIVE_STREAM_URL": LIVE_STREAM_URL,
    })

def legal(request):
    return render(request, "sitepromo/legal.html")
