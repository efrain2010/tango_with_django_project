from django.contrib import admin
from rango.models import Category, CategoryAdmin, Page, PageAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
