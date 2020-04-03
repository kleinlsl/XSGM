from django.contrib import admin

# Register your models here.
from app.models import User, Course, Grade, Message


class UserAdmin(admin.ModelAdmin):
    fields = ('user_name', 'user_pass', 'user_id', 'message_name', 'message_sex', 'message_age', 'message_phone', 'message_image')
    list_display = ('user_name', 'user_pass', 'user_id', 'message_name', 'message_sex', 'message_age', 'message_phone', 'message_image','add_time')


class CourseAdmin(admin.ModelAdmin):
    fields = ('course_id', 'course_name', 'semester', 'course_teacher')
    list_display =('course_id', 'course_name', 'semester', 'course_teacher','add_time')


class GradeAdmin(admin.ModelAdmin):
    fields = ('user_name', 'course_id', 'grade_value', 'grade_complain')
    list_display = ('user_name', 'course_id', 'grade_value', 'grade_complain','add_time')

class MessageAdmin(admin.ModelAdmin):
    fields = ('sender', 'receive', 'message', 'read')
    list_display = ('sender', 'receive', 'message', 'read','add_time')


admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Message, MessageAdmin)

#修改网页title和站点header
admin.site.site_title = "学生成绩后台"
admin.site.site_header = "学生成绩管理"