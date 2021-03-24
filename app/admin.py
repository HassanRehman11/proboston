from django.contrib import admin
from app.models import PostData


class CustomAdmin(admin.ModelAdmin):
    '''
    To restrict the addition of data from django admin site, 
    this function override the permission to add the data.
    '''
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(PostData, CustomAdmin)