from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About,Service,SelectedWorks

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





class BlogTemplateView(TemplateView):
	template_name ='core/blogs.html'