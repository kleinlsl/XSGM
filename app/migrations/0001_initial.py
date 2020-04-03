# Generated by Django 2.2 on 2019-12-16 14:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course_id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='课程id')),
                ('course_name', models.CharField(max_length=300, verbose_name='课程名')),
                ('semester', models.CharField(max_length=300, verbose_name='学期')),
            ],
            options={
                'verbose_name': '课程管理',
                'verbose_name_plural': '课程管理',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user_name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='账号')),
                ('user_pass', models.CharField(max_length=300, verbose_name='密码')),
                ('user_id', models.CharField(choices=[('学生', '学生'), ('教师', '教师')], max_length=300, verbose_name='身份')),
                ('message_name', models.CharField(max_length=300, verbose_name='姓名')),
                ('message_sex', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=300, verbose_name='性别')),
                ('message_age', models.IntegerField(verbose_name='年龄')),
                ('message_phone', models.CharField(max_length=300, verbose_name='联系方式')),
                ('message_image', models.ImageField(blank=True, max_length=300, null=True, upload_to='config/user/%Y/%m', verbose_name='用户头像')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('grade_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='成绩')),
                ('grade_complain', models.CharField(blank=True, max_length=300, null=True, verbose_name='成绩申诉')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course', verbose_name='课程id')),
                ('user_name', models.ForeignKey(limit_choices_to={'user_id': '学生'}, on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='学号')),
            ],
            options={
                'verbose_name': '成绩管理',
                'verbose_name_plural': '成绩管理',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_teacher',
            field=models.ForeignKey(limit_choices_to={'user_id': '教师'}, on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='任课教师'),
        ),
    ]
