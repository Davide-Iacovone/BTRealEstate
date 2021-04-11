from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'list_date', 'realtor')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'price')
    list_display_links = ('id', 'title')

admin.site.register(Listing, ListingAdmin)