# Generated by Django 4.0.5 on 2023-11-08 14:36

import json
from django.conf import settings
from django.db import migrations


def forward_func(apps, schema_editor):

    area_json = {
        "Career Opportunities": "career.json",
        "Eligibility Criteria": "criteria.json",
        "Curriculum": "curriculum.json",
        "Payment Options": "payment.json",
        "Program Duration": "program_duration.json"
    }
    
    data_dir = settings.BASE_DIR.parent/"data"

    Area = apps.get_model("bot", "Area")
    FAQ = apps.get_model("bot", "FAQ")
    db_alias = schema_editor.connection.alias

    for area,file in area_json.items():
        area = Area.objects.using(db_alias).create(area=area)
        with open(data_dir/file) as f:
            responses = json.loads(f.read())
            for question,answer in responses.items():
                FAQ.objects.using(db_alias).create(area=area,
                                                    question=question,
                                                    answer=answer)

def reverse_func(apps, schema_editor):

    Area = apps.get_model("bot", "Area")
    db_alias = schema_editor.connection.alias

    Area.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward_func,reverse_func)
    ]
