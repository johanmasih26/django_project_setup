from djangoTest.models import order
from django.contrib import admin

# Register your models he

class orderAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','city','amount','order_id']
admin.site.register(order,orderAdmin)

