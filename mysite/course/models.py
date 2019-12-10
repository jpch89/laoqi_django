from django.contrib.auth.models import User
from django.db import models
from slugify import slugify

from .fields import OrderField


class Course(models.Model):
    # 外键就是一对多，一个用户对应多个课程，定义在多的一侧
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_user')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


def user_directory_path(instance, filename):
    return 'courses/user_{0}/{1}'.format(instance.user.id, filename)

class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to=user_directory_path)
    attach = models.FileField(blank=True, upload_to=user_directory_path)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return '{}.{}'.format(self.order, self.title)
