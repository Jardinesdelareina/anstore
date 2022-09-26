from django.shortcuts import render

def google_auth(request):
    # Страница авторизации Google
    return render(request, 'account/google_auth.html')