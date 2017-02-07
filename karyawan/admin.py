from django.contrib import admin
from karyawan.models import *

class KaryawanAdmin (admin.ModelAdmin):
    list_display = ['nama', 'alamat','jenis_karyawan','email']
    list_filter = ()
    search_fields = ['nama', 'alamat', 'email']
    list_per_page = 25

admin.site.register(Karyawan, KaryawanAdmin)

class AkunAdmin (admin.ModelAdmin):
    list_display = ['akun', 'karyawan', 'jenis_akun']
    list_filter = ()
    search_fields = []
    list_per_page = 25

admin.site.register(Akun, AkunAdmin)