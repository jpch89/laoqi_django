from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView

from .models import Course


class AboutView(TemplateView):
    template_name = 'course/about.html'


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/course_list.html'
    # queryset = Course.objects.filter(user=User.objects.get(username='jpch89'))

    def get_queryset(self):
        qs = super(CourseListView, self).get_queryset()
        return qs.filter(user=User.objects.get(username='jpch89'))
