from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>I'm the home!</h1>")
