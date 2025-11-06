import environ
from django.conf import settings

env = environ.Env()

def branding(request):
    return {
        "PROJECT_NAME": env('PROJECT_NAME', default='AgroPredict'),
        "TAGLINE": env('TAGLINE', default='Predicción frutícola clara y accionable'),
        "FERIA_URL": env('FERIA_URL', default='https://www.feriadesoftware.cl/vina'),
        "ENTRADAS_URL": env('ENTRADAS_URL', default='https://welcu.com/ibtinf-svm/feria-de-software-vina-2025'),
        "IG_URL": env('IG_URL', default='https://www.instagram.com/treering.agropredict'),
        "LI_URL": env('LI_URL', default='https://www.linkedin.com/company/treeringagropredict/'),
        "GRADIENT_START": env('PRIMARY_GRADIENT_START', default='#ff5bbd'),
        "GRADIENT_END": env('PRIMARY_GRADIENT_END', default='#7b61ff'),
        "DEBUG": settings.DEBUG,
    }
