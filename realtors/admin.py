from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
  list_display = ('name','id','is_mvp','email','phone','hire_date',)
  list_editable = ('is_mvp',)


admin.site.register(Realtor,RealtorAdmin)
