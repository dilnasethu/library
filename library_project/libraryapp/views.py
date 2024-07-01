from django.shortcuts import render,HttpResponse,redirect
from libraryapp.forms import LibraryRegisterForm,UserLoginForm,UserEditForm
from django.views import View
from django.views.generic import TemplateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from libraryapp.models import LibraryModel
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class LibraryRegisterView(View):
    def get(self,request):
        form=LibraryRegisterForm()
        return render(request,'register.html',{"form":form})
    def post(self,request):
        data=LibraryRegisterForm(request.POST)
        if data.is_valid():
            formdata=data.cleaned_data
            LibraryModel.objects.create_user(**formdata)
            return HttpResponse("saved")
        else:
            return HttpResponse("inavalid credentials")
        
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            return HttpResponse(" Login successfull")
        else:
            return HttpResponse("invalid") 
        

class ReadAllView(View):
    def get(self,request):
        userlist=LibraryModel.objects.all()
        return render(request,'listall.html',{'userlist':userlist})
    
class ReadUserView(View):
    def get(self,request):
        user=LibraryModel.objects.filter(username=request.user)
        return render(request,'user.html',{'user':user})
    
class UserEditView(UpdateView):
    model=LibraryModel
    form_class=UserEditForm
    template_name="useredit.html"
    success_url=reverse_lazy('home_view')
    pk_url_kwarg='id'
    
    
class UserDeleteView(DeleteView):
    model=LibraryModel
    pk_url_kwarg='id'
    success_url=reverse_lazy('home_view')
    template_name='docdelete.html'


class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log_view')