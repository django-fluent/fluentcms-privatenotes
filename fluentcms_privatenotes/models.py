from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from fluent_contents.models import ContentItem


@python_2_unicode_compatible
class PrivateNotesItem(ContentItem):
    """
    Private notes
    """
    date_created = models.DateTimeField(_("Created at"), auto_now_add=True)
    date_modified = models.DateTimeField(_("Last modified at"), auto_now=True)
    notes = models.TextField(_("Notes"), help_text=_("These notes are only visible for you as administrator"))

    class Meta:
        verbose_name = _("Private note")
        verbose_name_plural = _("Private notes")

    def __str__(self):
        return self.notes
