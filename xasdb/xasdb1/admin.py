from django.contrib import admin

from .models import XASFile, XASArray, XASMode

@admin.register(XASFile)
class XASFileAdmin(admin.ModelAdmin):
    readonly_fields = ('upload_file', 'upload_timestamp', 'atomic_number', 'element', 'edge', 'uploader', 'sample_name', 'beamline_name', 'facility_name', 'refer_used')

@admin.register(XASArray)
class XASArrayAdmin(admin.ModelAdmin):
    fields = ('file', 'name', 'unit')
    readonly_fields = fields

@admin.register(XASMode)
class XASModeAdmin(admin.ModelAdmin):
    fields = ('file', 'mode')
    readonly_fields = fields
