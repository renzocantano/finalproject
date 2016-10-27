from django.contrib import admin

from.models import Jeep

class JeepModelAdmin(admin.ModelAdmin):
    list_display = ['route', 'updated', 'timestamp']
    search_fields = ['route', 'place']
    class Meta:
        model = Jeep

admin.site.register(Jeep, JeepModelAdmin)
# Register your models here.
