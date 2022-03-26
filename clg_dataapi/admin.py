from django.contrib import admin
from .models import TeacherData, Branch, StudentData
# Register your models here.
admin.site.register(Branch)
admin.site.register(TeacherData)
admin.site.register(StudentData)