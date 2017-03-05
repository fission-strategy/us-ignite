from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]
    operations = [
            migrations.AddField(
                model_name='richtextpage',
                name='about_desc',
                field=mezzanine.core.fields.RichTextField(verbose_name="About description", blank=True, null=True),
            ),
    ]
