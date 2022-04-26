from django.contrib import admin
from .models import contactregister

# Register your models here.

#--------------display all datas in admin page without modification
#admin.site.register(contactregister)

#--------------display all datas in admin page with modification
class ContactregisterAdmin(admin.ModelAdmin):
    list_display=('name','contact_num')
    ordering=('name',)
    search_fields=('name','contact_num')
admin.site.register(contactregister,ContactregisterAdmin)
