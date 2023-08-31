
from django.http import HttpResponse
from django.template import loader
from .models import Member


def BlogPost(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('product_list.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def products(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('product_list.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))