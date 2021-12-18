from django.contrib import admin
from .models import *

class profileAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'roll')

admin.site.register(Work)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Notification)
admin.site.register(Profile, profileAdmin)
admin.site.register(Art)
admin.site.register(Restaurant)
admin.site.register(Hotel)
admin.site.register(Cat)
admin.site.register(Restaurant_sample)
