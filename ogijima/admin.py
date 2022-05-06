from django.contrib import admin
from .models import *

class profileAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'roll')

admin.site.register(Work)
admin.site.register(Work_for_calender)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Notification)
admin.site.register(Profile, profileAdmin)
admin.site.register(Art)
admin.site.register(Restaurant)
admin.site.register(Hotel)
admin.site.register(Restaurant_and_hotel)
admin.site.register(Cat)
admin.site.register(Restaurant_sample)
admin.site.register(Slideshow_pc)
admin.site.register(Slideshow_mobile)
admin.site.register(Sponsor_name)
admin.site.register(Sponsor_banner)
admin.site.register(Contact)
admin.site.register(Apply_Contact)
admin.site.register(Application_contact)
admin.site.register(Application_contact)
