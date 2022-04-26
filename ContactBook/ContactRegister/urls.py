from django.urls import path
from . import views


app_name="contact"

urlpatterns = [
    path('', views.home,name="home"),
    path('Reg',views.register,name="register"),
    path('View',views.allcontacts,name="viewall"),

    path('Save',views.Addcontact,name="Save"),
    
    
    path('Edit/<int:id>',views.edit),
    path('Del',views.delete,name="Del"),
    path('Delete',views.delete_view,name="Delete"),
    path('Update/<int:id>',views.update),
    
        
]