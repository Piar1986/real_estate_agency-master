from django.contrib import admin
from .models import Flat
from .models import Complaint
from .models import Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building','has_balcony','rooms_number')
    raw_id_fields = ('liked_by', 'owner')
 
admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('author', 'flat', 'complaint_text')
    raw_id_fields = ('author', 'flat')

admin.site.register(Complaint, ComplaintAdmin)

class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('phone_pure',)
    list_display = ('name',)
    raw_id_fields = ('flat',)

admin.site.register(Owner, OwnerAdmin)
