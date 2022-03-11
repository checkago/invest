from django.contrib import admin
from .models import Project, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'text')


admin.site.register(Project)
admin.site.register(Order, OrderAdmin)
