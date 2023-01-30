from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from fluent_pages.adminui.utils import get_page_admin_url

from .models import PrivateNotesItem


@admin.register(PrivateNotesItem)
class PrivateNotesAdmin(admin.ModelAdmin):
    """
    Admin for private notes.
    """

    # date_hierarchy = 'date_created'
    readonly_fields = ("date_created", "date_modified", "parent_field")
    fieldsets = (
        (
            None,
            {
                "fields": ("notes",),
            },
        ),
        (
            _("Metadata"),
            {
                "fields": ("date_created", "date_modified", "parent_field"),
            },
        ),
    )

    class Media:
        css = {
            "screen": ("admin/fluentcms_privatenotes/privatenotes.css",),
        }

    def parent_field(self, object):
        parent = object.parent
        url = get_page_admin_url(parent)
        return format_html('<a href="{0}">{1} ({2})</a>', url, parent, parent.default_url)

    parent_field.short_description = _("Page")
