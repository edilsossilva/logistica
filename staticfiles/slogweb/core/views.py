from django.shortcuts import render

# Create your views here.
def home(request, template_name = 'core/home.html'):
    return render(request, template_name)


def dashboard(request, template_name = 'core/dashboard.html'):
    return render(request, template_name)