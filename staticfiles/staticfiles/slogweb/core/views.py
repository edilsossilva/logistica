from django.shortcuts import render
from .forms import ContatoForm


# Create your views here.
def home(request, template_name = 'core/home.html'):
    return render(request, template_name)


def dashboard(request, template_name = 'core/dashboard.html'):
    return render(request, template_name)


def contato(request, template_name = 'core/contato.html'):
    form = ContatoForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)
