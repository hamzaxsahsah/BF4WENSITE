from django.contrib import admin  
from .models import Article  
from .models import Service
from .models import Member
# Register your models here.  
admin.site.register(Article)  
admin.site.register(Service)  
admin.site.register(Member) 