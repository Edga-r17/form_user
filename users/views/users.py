from django.shortcuts import render, redirect
from users.models import User
from rest_framework import generics
from users.serializers.users import UserSerializer
from django.views.decorators.csrf import csrf_exempt

class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt 
def form_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        age = request.POST.get("age")

        if name and phone and age:
            User.objects.create(
                name=name,
                phone=phone,
                age=int(age)  
            )
        return redirect('lista-formularios')  

    return render(request, 'form.html')

def lista_formularios(request):
    data = User.objects.all()  
    return render(request, 'list.html', {'data': data})
