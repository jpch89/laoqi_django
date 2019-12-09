from django.urls import path

# from django.views.generic import TemplateView
from .views import AboutView

app_name = 'course'

urlpatterns = [
    # path('about/', TemplateView.as_view(template_name='course/about.html')),
    path('about/', AboutView.as_view(), name="about"),
]
