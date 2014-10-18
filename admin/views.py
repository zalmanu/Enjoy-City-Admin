from django.http import HttpResponse

def home(request):
    return HttpResponse('You`re home.')
