from django import template

from job_management.models import main_category, sub_category, sub_sub_category

register = template.Library()


@register.filter
def menu_data(value):
    x=main_category.objects.all()
    return x

@register.filter
def menu_data1(value,id):
    p=main_category.objects.get(id=id)
    x=sub_category.objects.filter(main_category_name=p.main_category_name)
    print(x)
    return x

@register.filter
def menu_data2(value,id):
    p=sub_category.objects.get(id=id)
    x=sub_sub_category.objects.filter(sub_category_name=p.sub_category_name)
    return x