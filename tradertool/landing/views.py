from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    try:
        response = render(request, 'landing/index.html', context={})  # Caminho para o template
        print(type(response))
        return response
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return HttpResponse(f"Erro na renderização: {e}")
