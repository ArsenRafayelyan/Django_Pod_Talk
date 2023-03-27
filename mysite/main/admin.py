from django.contrib import admin
from .models import (HomeLogo, HomeBgInfo, HomeSlider, Lastest_Episode,Topic,Trending,About_page,
                     About_boody,AboutSlider,Contact)
# Register your models here.

admin.site.register(HomeLogo)
admin.site.register(HomeBgInfo)
admin.site.register(Lastest_Episode)
admin.site.register(Topic)
admin.site.register(Trending)
admin.site.register(About_page)
admin.site.register(About_boody)
admin.site.register(AboutSlider)



@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'proff1', 'proff2']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','company']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email','company']