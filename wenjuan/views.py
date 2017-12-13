
import xlrd
# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
# from wenjuan.models import record_stu,question_list

from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):

    if request.POST:
        page_id = request.POST['page_id']
        if page_id == '1':
            return render(request, "t1s.html")
        if page_id == '2':
            return render(request, "t1.html")
        if page_id == '2a':
            return render(request, "2a.html")
        if page_id == '3':
            return render(request, "t2s.html")
        if page_id == '4':
            return render(request, "t2.html")
        if page_id == '4a':
            return render(request, "4a.html")
        if page_id == '5':
            return render(request, "t3s.html")
        if page_id == '6':
            return render(request, "t3.html")
        if page_id == '6a':
            return render(request, "6a.html")
        if page_id == '7':
            return render(request, "t4.html")
        if page_id == '7a':
            return render(request, "7a.html")
        if page_id == '8':
            return render(request, "t5.html")
        if page_id == '8a':
            return render(request, "8a.html")
        if page_id == '9':
            return render(request, "t6.html")
        if page_id == '9a':
            return render(request, "9a.html")
        if page_id == '10':

            u= '测试完成'
            return HttpResponse(u)
        else:
            return render(request, "t0.html")

    else:
        page_id=0
        return render(request, "index.html",{'page_id':page_id})




@csrf_exempt
def manage(request):

    return render(request, "manage.html")



def login(request):
    if request.POST:
        user= request.POST['username']
        paw= request.POST['password']
        if user == '1' and paw == '1':
            return HttpResponseRedirect('/manage')
        else:
            u='用户名或密码不正确'
            return render(request, "login.html",{'tip':u})
    else:
        return render(request, "login.html")

# def read_excel(request):
#     # 打开excel文件
#     ExcelFile = xlrd.open_workbook('问卷.xlsx')
#     # 获取表单
#     for i in range(1,4):
#
#         sheet = ExcelFile.sheet_by_index(i)
#         # 读取数据,列的数据
#         ncols = sheet.ncols
#
#         # 读取数据,行的数据
#         nrow=sheet.nrows
#
#         # if i==0:
#         #
#         #     for row in range(0, nrow):
#         #         for cols in range(0, ncols):
#         #             data = sheet.cell_value(row, cols)
#         #             #写入数据库
#         #             twz = question_list(t1s=data)
#         #             twz.save()
#         id = 461
#         if i == 1:
#             for row in range(0, nrow):
#                 for cols in range(0, ncols):
#                     data = sheet.cell_value(row, cols)
#                     #写入数据库
#
#                     t=question_list.objects.filter(id=id)
#                     t.update(t1=data)
#                     id=id+1
#
#
#         if i == 2:
#             for row in range(0, nrow):
#                 for cols in range(0, ncols):
#                     data = sheet.cell_value(row, cols)
#                     #写入数据库
#                     t = question_list.objects.filter(id=id)
#                     t.update(t1=data)
#                     id = id + 1
#
#
#         if i == 3:
#             for row in range(0, nrow):
#                 for cols in range(0, ncols):
#                     data = sheet.cell_value(row, cols)
#                     #写入数据库
#                     t = question_list.objects.filter(id=id)
#                     t.update(t1=data)
#                     id = id + 1
#
#
#     return  HttpResponse('完成')