from django.db import migrations


def create_missing_user_model(apps, schema_editor):
    UserModel = apps.get_model('project', 'UserModel')
    table_names = schema_editor.connection.introspection.table_names()

    if UserModel._meta.db_table not in table_names:
        schema_editor.create_model(UserModel)


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_usermodel_password'),
    ]

    operations = [
        migrations.RunPython(create_missing_user_model, migrations.RunPython.noop),
    ]