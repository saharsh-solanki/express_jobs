from django.contrib import admin

# Register your models here.
from .models import main_category , sub_category , Add_Job , Manager

admin.site.register(main_category)
admin.site.register(sub_category)
admin.site.register(Add_Job)
admin.site.register(Manager)