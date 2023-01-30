from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fluent_contents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrivateNotesItem",
            fields=[
                (
                    "contentitem_ptr",
                    models.OneToOneField(
                        parent_link=True,
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        to="fluent_contents.ContentItem",
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(verbose_name="Created at", auto_now_add=True),
                ),
                (
                    "date_modified",
                    models.DateTimeField(verbose_name="Last modified at", auto_now=True),
                ),
                (
                    "notes",
                    models.TextField(
                        help_text="These notes are only visible for you as administrator",
                        verbose_name="Notes",
                    ),
                ),
            ],
            options={
                "db_table": "contentitem_fluentcms_privatenotes_privatenotesitem",
                "verbose_name": "Private note",
                "verbose_name_plural": "Private notes",
            },
            bases=("fluent_contents.contentitem",),
        ),
    ]
