# Generated by Django 1.11.27 on 2020-01-14 16:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0027_auto_20180105_1631_squashed_0028_auto_20180606_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofile',
            name='access',
            field=models.CharField(choices=[('public', 'Public'), ('public-invite', 'Public (invite-only)'), ('private', 'Private')], default="public'", help_text='Public: Any registered user can view and join a public group.<br>Public (invite-only):Any registered user can view the group.  Only invited users can join.<br>Private: Registered users cannot see any details about the group, including membership.  Only invited users can join.', max_length=15, verbose_name='Access'),
        ),
    ]
