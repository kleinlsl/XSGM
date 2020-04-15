import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from app.models import User, Grade, Message,Course


class IndexView(View):
    def get(self,request,*args,**kwargs):


        return render(request, 'index.html',{

        })

class UserView(View):
    # def dispatch(self, request, *args, **kwargs):  # 反射调用 类中的方法     其实和上面的写法一样
    #     # 调用父类中的dispatch
    #     print('before')
    #     result = super(UserView, self).dispatch(request, *args, **kwargs)
    #     print('after')
    #     return result
    def get(self, request):
        users = User.objects.all()
        data = json.loads(serializers.serialize("json", users))
        # print(data)
        # return HttpResponse("success")
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        print("进入post请求")
        action = request.POST.get('action')
        if action=="find_all_user":
            return self.find_all_user(request)
        elif action=="find_user":
            return self.find_user(request)
        elif action=="user_login":
            return self.user_login(request)
        elif action=="add_user":
            return self.add_user(request)
        elif action=="updata_user":
            return self.updata_user(request)
        elif action=="find_all_stu":
            return self.find_all_stu(request)
        elif action=="find_all_tea":
            return self.find_all_tea(request)

        data = {"msg":action}
        # type(data)
        # print(type(data))
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def find_all_user(self,request):
        print("find_all_user")
        users = User.objects.all()
        data = json.loads(serializers.serialize("json", users))
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def find_all_stu(self, request, *args, **kwargs):
        print("find_all_stu")
        users = User.objects.filter(user_id="学生")
        data = json.loads(serializers.serialize("json", users))
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def find_all_tea(self, request, *args, **kwargs):
        print("find_all_tea")
        users = User.objects.filter(user_id="教师")
        data = json.loads(serializers.serialize("json", users))
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def find_user(self,request):
        print("find_user")
        user_n=request.POST.get("user_name")
        user=User.objects.filter(user_name=user_n)

        data=json.loads(serializers.serialize("json", user))
        print(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def user_login(self,request):
        print("user_login")
        name=request.POST.get("user_name")
        password=request.POST.get("user_pass")
        id=request.POST.get("user_id")
        if id=="student":
            id="学生"
        else:
            id="教师"
        try:
            User.objects.get(user_name=name,user_pass=password,user_id=id)
        except:
            return JsonResponse({"msg":"error"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"msg":"success"}, safe=False, json_dumps_params={'ensure_ascii': False})

    def add_user(self,request):
        add_data = request.POST.get("user_data")
        data = json.loads(add_data)
        try:
            User.objects.get(user_name=data['pk'])
        except:
            user = User()
            user.user_name = data["pk"]
            user.user_pass = data["fields"]["user_pass"]
            user.user_id = data["fields"]["user_id"]
            user.message_name = data["fields"]["message_name"]
            user.message_sex = data["fields"]["message_sex"]
            user.message_age = data["fields"]["message_age"]
            user.message_phone = data["fields"]["message_phone"]
            user.save()

            return JsonResponse({"msg": "success"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"msg": "error"}, safe=False, json_dumps_params={'ensure_ascii': False})

    def updata_user(self, request):
        print("updata_user")
        user_data = request.POST.get("user_data")
        data = json.loads(user_data)
        try:
            user = User.objects.get(user_name=data['pk'])
        except:
            return JsonResponse({"msg": "error"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            user.user_pass = data["fields"]["user_pass"]
            user.user_id = data["fields"]["user_id"]
            user.message_name = data["fields"]["message_name"]
            user.message_sex = data["fields"]["message_sex"]
            user.message_age = data["fields"]["message_age"]
            user.message_phone = data["fields"]["message_phone"]
            user.save()
            return JsonResponse({"msg":"success"}, safe=False, json_dumps_params={'ensure_ascii': False})


class GradeView(View):
    def get_user(self,pk):
        user_data=User.objects.filter(pk=pk)
        data = json.loads(serializers.serialize("json", user_data))
        return data[0]

    def get_course(self,pk):
        course_data=Course.objects.filter(pk=pk)
        data = json.loads(serializers.serialize("json", course_data))
        return data[0]

    def get(self,request):
        #获取到成绩集合
        grades = Grade.objects.all()
        data = json.loads(serializers.serialize("json", grades))
        print(data)
        #构造Gson字典
        for i in range(0,len(data)):
            # print(data[i])
            data[i]["user_info"]=self.get_user(data[i]["fields"]['user_name'])
            data[i]["course_info"] = self.get_course(data[i]["fields"]['course_id'])
        # print(data[0]['fields'])
        print(data)
        # return HttpResponse("success")
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        print("GradeView  post")
        action = request.POST.get('action')
        if action == "find_grade_stu":
            return self.find_grade_stu(request)
        elif action=="find_grade_all_stu":
            return self.find_grade_all_stu(request)
        elif action == "updata_grade_complain":
            return self.updata_grade_complain(request)
        elif action=="updata_grade_value":
            return  self.updata_grade_value(request)
        elif action=="add_grade_stu":
            return self.add_grade_stu(request)
        elif action == "get":
            return self.get(request)
        data = {"action": action}
        # data['action'] = body
        # type(data)
        # print(type(data))
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def find_grade_stu(self, request):
        user_name=request.POST.get("user_name")
        #获取成绩集合
        grades = Grade.objects.filter(user_name=user_name)
        data = json.loads(serializers.serialize("json", grades))
        # print(data)
        #构造Gson字典
        for i in range(0,len(data)):
            # print(data[i])
            data[i]["user_info"]=self.get_user(data[i]["fields"]['user_name'])
            data[i]["course_info"] = self.get_course(data[i]["fields"]['course_id'])
        # print(data[0]['fields'])
        print(data)
        # return HttpResponse("success")
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def find_grade_all_stu(self, request):
        #获取成绩集合
        grades = Grade.objects.filter()
        data = json.loads(serializers.serialize("json", grades))
        for i in range(0,len(data)):
            data[i]["user_info"]=self.get_user(data[i]["fields"]['user_name'])
            data[i]["course_info"] = self.get_course(data[i]["fields"]['course_id'])
        print(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def updata_grade_complain(self, request):
        pk = request.POST.get("pk")
        grade_complain = request.POST.get("grade_complain")
        try:
            grade = Grade.objects.get(pk=int(pk))
        except:
            return JsonResponse({"msg": "error"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            grade.grade_complain = grade_complain
            grade.save()
            return JsonResponse({"msg": "success"}, safe=False, json_dumps_params={'ensure_ascii': False})

    def updata_grade_value(self, request):
        pk = request.POST.get("pk")
        grade_value = request.POST.get("grade_value")
        try:
            grade = Grade.objects.get(pk=int(pk))
        except:
            return JsonResponse({"msg": "error"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            grade.grade_value = grade_value
            grade.save()
            return JsonResponse({"msg": "success"}, safe=False, json_dumps_params={'ensure_ascii': False})

    def add_grade_stu(self, request):
        user_name = request.POST.get("user_name")
        course_id = request.POST.get("course_id")
        grade_value=request.POST.get("grade_value")
        # teacher_name = request.POST.get("teacher_name")
        try:
            Grade.objects.get(user_name=user_name,course_id=course_id)
        except:
            try:
                course = Course.objects.get(course_id=course_id)
                user = User.objects.get(user_name=user_name, user_id="学生")
                grade = Grade()
                grade.grade_value = grade_value
                grade.course_id=course
                grade.user_name=user
                grade.save()
            except:
                return JsonResponse({"msg": "error"}, safe=False, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({"msg": "success"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"msg": "该记录已经存在"}, safe=False, json_dumps_params={'ensure_ascii': False})


class MessageView(View):
    def get(self,request):
        messages = Message.objects.all()
        data = json.loads(serializers.serialize("json", messages))
        print(data)
        # return HttpResponse("success")
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        print("进入message  post")
        action = request.POST.get('action')
        if action == "find_message_stu":
            return self.find_message_stu(request)
        elif action == "updata_message_state":
            return self.updata_message_state(request)
        elif action == "get":
            return self.get(request)
        elif action=="add_message":
            return self.add_message(request)
        data = {"action": action}
        # data['action'] = body
        # type(data)
        # print(type(data))
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def find_message_stu(self, request):
        receive = request.POST.get("receive")
        read=request.POST.get("read")
        messages = Message.objects.filter(receive=receive, read=read)
        # data = {}
        data = json.loads(serializers.serialize("json", messages))
        print(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

    def updata_message_state(self, request):
        read = request.POST.get("read")
        pk = request.POST.get("pk")
        try:
            message = Message.objects.get(pk=int(pk),read=read)
        except:
            return JsonResponse({"msg": "error"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            message.read = '1'
            message.save()
            return JsonResponse({"msg": "success"}, safe=False, json_dumps_params={'ensure_ascii': False})

    def add_message(self, request):
        add_data = request.POST.get("message_data")
        data = json.loads(add_data)
        try:
            sender=User.objects.get(user_name=data["fields"]["sender"],user_id="教师")
            receive=User.objects.get(user_name=data["fields"]["receive"],user_id="学生")
            message = Message()
            message.sender=sender
            message.receive=receive
            message.message=data["fields"]["message"]
            message.read=data["fields"]["read"]
            message.save()
        except:
            return JsonResponse({"msg": "error"}, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"msg": "success"}, safe=False, json_dumps_params={'ensure_ascii': False})


class CourseView(View):
    def get(self,request):
        courses = Course.objects.all()
        data = json.loads(serializers.serialize("json", courses))
        print(data)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})



