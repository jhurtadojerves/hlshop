from django.contrib import admin

from import_export import resources, fields
from import_export.admin import ImportExportMixin

from .models import Shop


class ShopResource(resources.ModelResource):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'url', 'vault', 'stars', 'status']
        import_order = fields
        export_order = fields
        IMPORT_EXPORT_SKIP_ADMIN_LOG = True


@admin.register(Shop)
class ShopAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'vault', 'stars', 'opened', 'checked', 'error', 'last_month', ]
    list_editable = ['opened', 'checked', 'error', 'last_month', ]
    list_filter = ['opened', 'opened', 'checked', 'stars', 'error', 'last_month', ]
    search_fields = ['name', ]
    class_resource = ShopResource
