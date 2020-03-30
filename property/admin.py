from django.contrib import admin
from .models import Flat
from .models import Complaint

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address','owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building','has_balcony','rooms_number')
    raw_id_fields = ('liked_by',)
 
admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'complaint_text')
    raw_id_fields = ('user', 'flat')

admin.site.register(Complaint, ComplaintAdmin)