from django.http import HttpResponse, JsonResponse
from .models import Proyect, Tasks
from django.shortcuts import get_object_or_404, render
# Create your views here.
def hello(request):
       
       return HttpResponse(f"<h1>Pagina principal</h1>")
def about(request):
      return HttpResponse("About")

def category(request):
      return HttpResponse("<h1>Category</h1>")

def categorias(request,id):
      
      
      return HttpResponse(f"el id es:  {id*1000/10-434}")   

def proyects(request):
      res = list(Proyect.objects.values())
      return JsonResponse(res, safe=False)

def TasksList(request, id):
      res= get_object_or_404(Tasks,id=id)
      
      return HttpResponse("Tasks %s"% res.title)

def index(request):
      return render(request,"index.html",{
            "title":"Hola mundo",
      })
      
      