from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import qrvalues , participant, registrar ,  verification_status , entries


class participant_admin(ImportExportModelAdmin):
  ordering = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
  list_display = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
  list_filter = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')  
  search_fields = ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
  def get_list_display(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
  def get_list_filter(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
  def get_search_fields(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
  def get_ordering(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')
      return ('fullname','registrationnumber','email','phone','year','branch','institute','campus','registrar','qrtext', 'qrhash')

admin.site.register(participant, participant_admin)

@admin.register(qrvalues)
class qrvalues_admin(ImportExportModelAdmin):
  list_display = ('qrtext', 'qrhash')
  def get_list_display(self, request):
    return ('qrtext', 'qrhash')

@admin.register(registrar)
class registrar_admin(admin.ModelAdmin):
  list_display = ['email']
  def get_list_display(self, request):
    return ['email']


class verification_status_admin(ImportExportModelAdmin):
  ordering = ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
  list_display = ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
  list_filter = ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')  
  search_fields = ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
  def get_list_display(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
      return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
  def get_list_filter(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
      return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
  def get_search_fields(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
      return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
  def get_ordering(self, request):
      if request.user.is_superuser:
          return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')
      return ('fullname','registrationnumber','email','qrtext', 'qrhash' , 'status')

admin.site.register(verification_status, verification_status_admin)



class entries_admin(ImportExportModelAdmin):
  ordering = ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
  list_display = ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
  list_filter = ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
  search_fields = ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
  def get_list_display(self, request):
      if request.user.is_superuser:
          return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
      return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
  def get_list_filter(self, request):
      if request.user.is_superuser:
          return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
      return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
  def get_search_fields(self, request):
      if request.user.is_superuser:
          return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
      return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
  def get_ordering(self, request):
      if request.user.is_superuser:
          return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')
      return ('registrationnumber','qrtext', 'qrhash' , 'date', 'time', 'verifiedby')


admin.site.register(entries, entries_admin)