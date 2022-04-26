import django_filters
from .models import *
from django.forms.widgets import TextInput


class ContactFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(widget=TextInput(attrs={'placeholder':'Search for Name '}))
    contact_num=django_filters.CharFilter(widget=TextInput(attrs={'placeholder':'Search for Number '}))

    class Meta:
        model=contactregister
        fields=['name','contact_num']
        

    

# class AlphaFilter(django_filters.FilterSet):
#     CHOICES=(
#         ('ascending','Ascending'),
#         ('descending','Descending')
#     )

#     namesort=django_filters.ChoiceFilter(label='namesort',choices='CHOICES',method='filter_by_order')

#     def filter_by_order(self,queryset,name,value):
#         expression = 'created' if value=='ascending' else '-created'
#         return queryset.order_by(expression)


