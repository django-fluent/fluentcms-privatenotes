from django.test import TestCase
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items

from fluentcms_privatenotes.models import PrivateNotesItem


class PrivateNotesTests(TestCase):
    """
    Testing private notes
    """

    def test_no_output(self):
        """
        Test that the item doens't produce output.
        """
        item = create_content_item(PrivateNotesItem, notes="HIDDEN-NOTES!")
        self.assertEqual(render_content_items([item]).html, "")
