from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id','title','is_published','price','list_date','realtors')
  list_filter = ['realtors']
  list_display_links = ('id','title')
  list_editable = ('is_published',)
  search_fields = ('title', 'description','address','city', 'state', 'pincode',)


admin.site.register(Listing,ListingAdmin)
