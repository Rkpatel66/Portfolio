from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import*
from.models import*
# Create your views here.


def home(request):
    return render(request, "home.html")


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         desc = request.POST['desc']
#         print(name, email, phone, desc)
#         ins = Contact(name=name, email=email, phone=phone, desc=desc)
#         ins.save()
#     return render(request, "Contact.html")
@api_view(['GET'])
def contact(request):
    Contact_obj = Contact.objects.all()
    serializer = ContactSerializer(Contact_obj, many=True)
    return Response("serializer.data")


def aboutus(request):
    return render(request, "about.html")


def projects(request):
    return render(request, "projects.html")
