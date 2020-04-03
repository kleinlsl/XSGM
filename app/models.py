from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models

# Create your models here.
# 定义共同类

class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)
    class Meta:
        abstract = True #不生成表


class User(BaseModel):
    user_name = models.CharField(verbose_name="账号", max_length=100, primary_key=True)
    user_pass = models.CharField(verbose_name="密码", max_length=300)
    user_id = models.CharField(verbose_name="身份", max_length=300,choices=[("学生","学生"),("教师","教师")])
    message_name = models.CharField(verbose_name="姓名", max_length=300)
    message_sex = models.CharField(verbose_name="性别", max_length=300,choices=[("男","男"),("女","女")])
    message_age = models.IntegerField(verbose_name="年龄")
    message_phone = models.CharField(verbose_name="联系方式", max_length=300)
    message_image = models.ImageField(verbose_name="用户头像", max_length=300,upload_to="config/user/%Y/%m",null=True,blank=True)
    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.message_name)

class Course(BaseModel):
    course_id = models.CharField(verbose_name="课程id", max_length=100, primary_key=True)
    course_name = models.CharField(verbose_name="课程名", max_length=300)
    semester = models.CharField(verbose_name="学期", max_length=300)
    course_teacher = models.ForeignKey(verbose_name="任课教师", to="User", on_delete=models.CASCADE,limit_choices_to={'user_id': u'教师'})
    class Meta:
        verbose_name = "课程管理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.course_name


class Grade(BaseModel):
    user_name = models.ForeignKey('User',verbose_name="学号", on_delete=models.CASCADE,limit_choices_to={'user_id':u'学生'})
    course_id = models.ForeignKey('Course',verbose_name="课程id",on_delete=models.CASCADE)
    grade_value = models.DecimalField(verbose_name="成绩", max_digits=5, decimal_places=2)
    grade_complain = models.CharField(verbose_name="成绩申诉", max_length=300,null=True,blank=True)
    class Meta:
        verbose_name = "成绩管理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.pk)

class Message(BaseModel):
    sender = models.ForeignKey(verbose_name="发送人",to="User",related_name='sender',on_delete=models.CASCADE,limit_choices_to={'user_id':u'教师'})
    receive = models.ForeignKey(verbose_name="接收人",to="User",related_name='receive',on_delete=models.CASCADE,limit_choices_to={'user_id':u'学生'})
    message = models.CharField(verbose_name="内容", max_length=300)
    read = models.CharField(verbose_name="是否阅读", max_length=300,choices=[("0","否"),("1","是")])
    class Meta:
        verbose_name = "消息管理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.read)





