from django.urls import path
from .views import HomeTemplateView,ContactTemplateView,BlogTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(),name="home"),
    path('contact', ContactTemplateView.as_view(),),
    path('blogs', BlogTemplateView.as_view(),),
]

