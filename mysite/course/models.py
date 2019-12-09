from django.contrib.auth.models import User
from django.db import models
from slugify import slugify


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
