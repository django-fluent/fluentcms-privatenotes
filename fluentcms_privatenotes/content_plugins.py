from django.utils.translation import gettext_lazy as _
from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import PrivateNotesItem


@plugin_pool.register
class PrivateNotesPlugin(ContentPlugin):
    """
    Plugin to place notes on a page.
    """

    model = PrivateNotesItem
    category = _("Internal")
    admin_form_template = ContentPlugin.ADMIN_TEMPLATE_WITHOUT_LABELS

    def render(self, request, instance, **kwargs):
        return ""

    class Media:
        css = {
            "screen": ("admin/fluentcms_privatenotes/privatenotes.css",),
        }
