from django.contrib import admin
from rango.models import Category, CategoryAdmin, Page, PageAdmin, UserProfile

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
