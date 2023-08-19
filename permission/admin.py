from django.contrib import admin

from permission.models import *




@admin.register(RoleUser)
class RoleUserAdmin(admin.ModelAdmin):
    search_fields = ['id']

@admin.register(RoleAdmin)
class RoleAdminAdmin(admin.ModelAdmin):
    search_fields = ['id']
