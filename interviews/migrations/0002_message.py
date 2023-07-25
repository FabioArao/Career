# Generated by Django 4.2.3 on 2023-07-24 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('system', 'System'), ('user', 'Candidate'), ('assistant', 'Interviewer')], max_length=9)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='interviews.chat')),
            ],
        ),
    ]