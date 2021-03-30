from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import About,Service,SelectedWorks,blogHaru,Contact
from django.http import HttpResponse


# Create your views here.
class HomeTemplateView(TemplateView):
	template_name ='core/index.html'

	def get_context_data (self,**kwargs):
		context =super().get_context_data(**kwargs)
		context['about']=About.objects.first()
		context['services']=Service.objects.all()
		context['works']=SelectedWorks.objects.all()
		return context

class ContactTemplateView(TemplateView):
	template_name ='core/contact.html'

	def post(self,request,*args,**kwargs):
		if request.method =="POST":
			contact = Contact()
			name= request.POST.get('name')
			email= request.POST.get('email')
			message= request.POST.get('message')
			contact.name=name
			contact.email=email
			contact.message=message
			contact.save()

			return redirect('/contact')
		# return render(request,"core/contact.html")


class BlogTemplateView(TemplateView):
	template_name ='core/blogs.html'

	def get_context_data (self,**kwargs):
		context =super().get_context_data(**kwargs)
		context['blogs']=blogHaru.objects.all()

		return context
		




