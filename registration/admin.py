from django.contrib import admin

# Register your models here.
from .models import qrvalues , participant


class participant_admin(admin.ModelAdmin):
  ordering = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
  list_display = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
  list_filter = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')  
  search_fields = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
  def get_list_display(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
  def get_list_filter(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
  def get_search_fields(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
  def get_ordering(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar')

admin.site.register(participant, participant_admin)

admin.site.register(qrvalues)
