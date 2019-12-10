import json

from braces.views import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView

from .forms import CreateCourseForm
from .models import Course

# from django.views.generic.edit import CreateView



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


class UserMixin:
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)


class UserCourseMixin(UserMixin, LoginRequiredMixin):
    model = Course
    login_url = '/account/login/'


class ManageCourseListView(UserCourseMixin, ListView):
    context_object_name = 'courses'
    template_name = 'course/manage/manage_course_list.html'


class CreateCourseView(UserCourseMixin, CreateView):
    fields = ['title', 'overview']
    template_name = 'course/manage/create_course.html'

    def post(self, request, *args, **kwargs):
        form = CreateCourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect('course:manage_course')
        return self.render_to_response({'form': form})


class DeleteCourseView(UserCourseMixin, DeleteView):
    # template_name = 'course/manage/delete_course_confirm.html'
    success_url = reverse_lazy('course:manage_course')

    def dispatch(self, *args, **kwargs):
        resp = super(DeleteCourseView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {'result': 'ok'}
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            return resp
