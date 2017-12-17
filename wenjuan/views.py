
import xlrd
# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from wenjuan import models
from django.http import StreamingHttpResponse
from django.http import HttpResponseRedirect
import xlwt #写入数据
from django.views.decorators.csrf import csrf_exempt
import random
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login', redirect_field_name=None)
@csrf_exempt
def manage(request):
    rec = models.stu_record.objects.all()

    class_1=0
    class_2 =0
    class_3 = 0
    for class_num in rec:
        if class_num.game6:
            if class_num.stu_class=='1':
                class_1=class_1+1
            if class_num.stu_class=='2':
                class_2 = class_2 + 1
            if class_num.stu_class == '3':
                class_3 = class_3 + 1

    return render(request, "manage.html",{'record':rec,'class_1':class_1,'class_2':class_2,'class_3':class_3})

@login_required(login_url='/login', redirect_field_name=None)
def admin_manage(request):

    return render(request,'admin_manage.html')

def login(request):
    if request.POST:
        user= request.POST['username']
        paw= request.POST['password']
        user = auth.authenticate(username=user, password=paw)
        if user is None:

            return render(request, 'login.html', {'tip': '用户名不存在'})

        else:
            auth.login(request, user)
            # 如果登录成功就自动跳转到页面
            return HttpResponseRedirect('/manage')

    else:
        return render(request, "login.html")

def register(request):
    return render(request, 'register.html')

def register_check(request):
    username = request.POST['username']
    password = request.POST['password']
    check = request.POST['check']
    if check == 'qiulonghui':
        User.objects.create_user(username=username, password=password)
        return render(request, "login.html")
    else:
        tip = '输入的校验码不正确'
        return render(request, 'register.html',{'tip':tip})

#第一个连接：能力（Merit）
@csrf_exempt
def Merit(request):
    if request.POST:
        page_id = request.POST['page_id']

        if page_id == '1':
            stu_name = request.POST.get('name')
            stu_num = request.POST.get('stu_id')
            stu_class = request.POST.get('stu_class')
            stu_sex = request.POST.get('stu_sex')

            # 检查学生学号
            check = models.stu_record.objects.all()
            check_flag = 0
            for stu in check:
                if stu.stu_num == stu_num:
                    check_flag = 1

            if check_flag == 0:

                rec = models.stu_record(stu_name=stu_name, stu_num=stu_num, stu_class=stu_class, stu_sex=stu_sex)
                rec.save()

                data = []
                row = []

                num = models.list_t1s.objects.all()

                for j in range(2):
                    for i in range(0, 3):
                        row.append(num[i + j].t1s)
                    data.append(row)
                    row = []

                return render(request, "t1s.html", {'data': data, 'stu_num': stu_num})
            else:
                return HttpResponse('你的学号被人占用了，你需要请求老师的帮助')

        if page_id == '2':
            stu_num = request.POST.get('stu_id')
            data = []
            row = []

            num_lst = models.list_t1.objects.all()

            for j in range(31):
                for i in range(0, 6):
                    row.append(num_lst[i + j].t1)
                data.append(row)
                row = []

            # nu= request.POST.get('num')

            return render(request, "t1.html", {'data': data, 'stu_num': stu_num})

        # if page_id == '2a':
        #     return render(request, "2a.html")
        # 第二题explain
        if page_id == '3':
            # 收集第一题的数据
            stu_num = request.POST.get('stu_id')
            game1 = request.POST.get('game1')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game1 = game1
            rec.save()

            #读取示例数据
            data = []
            row = []

            num = models.list_t3s.objects.all()

            for j in range(2):
                for i in range(0, 4):
                    row.append(num[i + j].t3s)
                data.append(row)
                row = []


            return render(request, "t3s.html", {'stu_num': stu_num,'data': data})
        #

        if page_id == '4':
            stu_num = request.POST.get('stu_id')

            #显示t3的数据

            data = []
            row = []

            num_lst = models.list_t3.objects.all()

            for j in range(20):
                for i in range(0, 6):
                    row.append(num_lst[i + j].t3)
                data.append(row)
                row = []

            return render(request, "t3.html", {'stu_num': stu_num,'data': data})

        #已省去
        if page_id == '4a':
            stu_num = request.POST.get('stu_id')


            return render(request, "6a.html", {'stu_num': stu_num})

        # 第三题：黑方块

        if page_id == '5':
            # 收集第二题的数据
            game2 = request.POST.get('game2')
            stu_num = request.POST.get('stu_id')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game2 = game2
            rec.save()

            return render(request, "t2s.html", {'stu_num': stu_num})

        if page_id == '6':
            stu_num = request.POST.get('stu_id')
            return render(request, "t2.html", {'stu_num': stu_num})

        if page_id == '6a':
            stu_num = request.POST.get('stu_id')
            return render(request, "4a.html", {'stu_num': stu_num})
        # 第四题
        if page_id == '7':
            # 收集第三题的数据
            game3 = request.POST.get('game3')
            stu_num = request.POST.get('stu_id')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game3 = game3
            rec.save()

            return render(request, "t4.html", {'stu_num': stu_num})

        if page_id == '7a':
            stu_num = request.POST.get('stu_id')
            return render(request, "7a.html", {'stu_num': stu_num})
        # 第五题
        if page_id == '8':
            # 收集第四题的数据
            stu_num = request.POST.get('stu_id')
            game4 = request.POST.get('game4')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game4 = game4
            rec.save()

            return render(request, "t5.html", {'stu_num': stu_num})
        if page_id == '8a':
            stu_num = request.POST.get('stu_id')
            return render(request, "8a.html", {'stu_num': stu_num})
        # 第六题
        if page_id == '9':
            # 收集第五题的数据

            stu_num = request.POST.get('stu_id')
            game5 = request.POST.get('game5')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game5 = game5
            rec.save()

            return render(request, "t6.html", {'stu_num': stu_num})
        if page_id == '9a':
            stu_num = request.POST.get('stu_id')
            return render(request, "9a.html", {'stu_num': stu_num})

        if page_id == '10':
            # 收集第六题的数据
            stu_num = request.POST.get('stu_id')
            game6 = request.POST.get('game6')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game6 = game6
            rec.save()

            return render(request, "pass.html", {'stu_num': stu_num})

        if page_id == '11':
            stu_num = request.POST.get('stu_id')

            return render(request, "directator.html", {'stu_num': stu_num})

        if page_id == '12':

            #收集directator的数据

            stu_num = request.POST.get('stu_id')
            SH_self_m = request.POST.get('SH_self_m')
            SH_allot_stu_m = request.POST.get('SH_allot_stu_m')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]





            # #选择分配以班级为单位
            radom_stu=models.stu_record.objects.filter(stu_class=rec.stu_class)

            if len(radom_stu)>4:
                for i in range(0,len(radom_stu)-1):
                    #获取一个随机整数
                    random_num=random.randint(0,len(radom_stu)-1)
                    #判断是否为当前学生
                    if radom_stu[random_num].game6:
                        if stu_num != radom_stu[random_num].stu_num:

                            radom_stu_one = radom_stu[random_num]
                            SH_allot_stu_a = radom_stu_one.stu_num
                            rec.SH_self_m = SH_self_m
                            rec.SH_allot_stu_a_m = SH_allot_stu_m
                            rec.SH_allot_stu_a = SH_allot_stu_a
                            rec.save()
                            break
                return render(request, "merit.html", {'stu_num': stu_num})
            else:
                return HttpResponse('做游戏的人数太少，无法做分配决定')




        if page_id == '13':

            #收集merit的数据

            stu_num = request.POST.get('stu_id')
            M_allot = request.POST.get('M_allot')
            ma=0
            mb=0
            if M_allot == '1':
                ma = 24
                mb = 0
            if M_allot == '2':
                ma = 20
                mb = 4
            if M_allot == '3':
                ma = 16
                mb = 8
            if M_allot == '4':
                ma = 12
                mb = 12
            if M_allot == '5':
                ma = 8
                mb = 16
            if M_allot == '6':
                ma = 4
                mb = 20
            if M_allot == '7':
                ma = 0
                mb = 24


            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            radom_stu = models.stu_record.objects.filter(stu_class=rec.stu_class)

            len_rad=len(radom_stu)
            #计算game1和game2的总成绩
            class_all = 0

            for one in radom_stu:
                if one.game6:
                    class_all=int(one.game1)+int(one.game2)+class_all


            #计算班级均值
            class_aver=class_all/len(radom_stu)

            #是否分配大值和小值的标志
            flag_max=0
            flag_min=0
            #存放没有完成game2的记录
            cop_null=[]
            cop=[]

            for j in range(len_rad):
                # 随机数存储
                cop.append(j)

            for i in range(0,len_rad):
                #获取一个随机整数
                if flag_max==1 and flag_min==1:
                    break
                else:
                    random_num=random.choice(cop)
                    #不重复抽取
                    cop.remove(random_num)

                        #判断是否完成第二个游戏
                    if radom_stu[random_num].game2:

                        # 判断是否为当前学生
                        if stu_num != radom_stu[random_num].stu_num:
                            # 计算学生游戏1和游戏2的值

                            count_stu_game = int(radom_stu[random_num].game1) + int(radom_stu[random_num].game2)
                            if flag_max == 0 and count_stu_game >= int(class_aver):

                                # 分配大值
                                M_allot_stu_a = radom_stu[random_num].stu_num
                                rec.M_allot_stu_a = M_allot_stu_a
                                flag_max = 1
                            else:
                                if flag_min == 0 and count_stu_game < int(class_aver):
                                    # 分配小值
                                    M_allot_stu_b = radom_stu[random_num].stu_num
                                    rec.M_allot_stu_b = M_allot_stu_b

                                    flag_min = 1
                        else:
                            continue
                    else:
                        continue





            rec.M_allot_stu_b_m = mb
            rec.M_allot_stu_a_m = ma


            rec.save()


            return HttpResponse('您已经做完游戏了，谢谢参与')




        else:

            return render(request, "t0.html")

    else:
        page_id = 0
        return render(request, "index.html", {'page_id': page_id})




@csrf_exempt
def Lucky(request):

    if request.POST:
        page_id = request.POST['page_id']

        if page_id == '1':
            stu_name = request.POST.get('name')
            stu_num = request.POST.get('stu_id')
            stu_class = request.POST.get('stu_class')
            stu_sex = request.POST.get('stu_sex')
            # 检查学生学号
            check = models.stu_record.objects.all()
            check_flag = 0
            for stu in check:
                if stu.stu_num == stu_num:
                    check_flag = 1

            if check_flag == 0:

                rec = models.stu_record(stu_name=stu_name, stu_num=stu_num, stu_class=stu_class, stu_sex=stu_sex)
                rec.save()

                data = []
                row = []

                num = models.list_t1s.objects.all()

                for j in range(2):
                    for i in range(0, 3):
                        row.append(num[i + j].t1s)
                    data.append(row)
                    row = []

                return render(request, "t1s_luck.html", {'data': data, 'stu_num': stu_num})
            else:
                return HttpResponse('你的学号被人占用了，你需要请求老师的帮助')

        if page_id == '2':
            stu_num = request.POST.get('stu_id')
            data = []
            row = []

            num_lst = models.list_t1.objects.all()

            for j in range(31):
                for i in range(0, 6):
                    row.append(num_lst[i + j].t1)
                data.append(row)
                row = []

            # nu= request.POST.get('num')

            return render(request, "t1_luck.html", {'data': data, 'stu_num': stu_num})

        # if page_id == '2a':
        #     return render(request, "2a.html")
        # 第二题explain
        if page_id == '3':
            # 收集第一题的数据
            stu_num = request.POST.get('stu_id')
            game1 = request.POST.get('game1')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game1 = game1
            rec.save()

            #读取示例数据
            data = []
            row = []

            num = models.list_t3s.objects.all()

            for j in range(2):
                for i in range(0, 4):
                    row.append(num[i + j].t3s)
                data.append(row)
                row = []


            return render(request, "t3s_luck.html", {'stu_num': stu_num,'data': data})
        #

        if page_id == '4':
            stu_num = request.POST.get('stu_id')

            #显示t3的数据

            data = []
            row = []

            num_lst = models.list_t3.objects.all()

            for j in range(20):
                for i in range(0, 6):
                    row.append(num_lst[i + j].t3)
                data.append(row)
                row = []

            return render(request, "t3_luck.html", {'stu_num': stu_num,'data': data})

        #已省去
        if page_id == '4a':
            stu_num = request.POST.get('stu_id')


            return render(request, "6a.html", {'stu_num': stu_num})

        # 第三题：黑方块

        if page_id == '5':
            # 收集第二题的数据
            game2 = request.POST.get('game2')
            stu_num = request.POST.get('stu_id')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game2 = game2
            rec.save()

            return render(request, "t2s_luck.html", {'stu_num': stu_num})

        if page_id == '6':
            stu_num = request.POST.get('stu_id')
            return render(request, "t2_luck.html", {'stu_num': stu_num})

        if page_id == '6a':
            stu_num = request.POST.get('stu_id')
            return render(request, "4a_luck.html", {'stu_num': stu_num})
        # 第四题
        if page_id == '7':
            # 收集第三题的数据
            game3 = request.POST.get('game3')
            stu_num = request.POST.get('stu_id')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game3 = game3
            rec.save()

            return render(request, "t4_luck.html", {'stu_num': stu_num})

        if page_id == '7a':
            stu_num = request.POST.get('stu_id')
            return render(request, "7a_luck.html", {'stu_num': stu_num})
        # 第五题
        if page_id == '8':
            # 收集第四题的数据
            stu_num = request.POST.get('stu_id')
            game4 = request.POST.get('game4')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game4 = game4
            rec.save()

            return render(request, "t5_luck.html", {'stu_num': stu_num})
        if page_id == '8a':
            stu_num = request.POST.get('stu_id')
            return render(request, "8a_luck.html", {'stu_num': stu_num})
        # 第六题
        if page_id == '9':
            # 收集第五题的数据

            stu_num = request.POST.get('stu_id')
            game5 = request.POST.get('game5')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game5 = game5
            rec.save()

            return render(request, "t6_luck.html", {'stu_num': stu_num})
        if page_id == '9a':
            stu_num = request.POST.get('stu_id')
            return render(request, "9a_luck.html", {'stu_num': stu_num})

        if page_id == '10':
            # 收集第六题的数据
            stu_num = request.POST.get('stu_id')
            game6 = request.POST.get('game6')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game6 = game6
            rec.save()

            return render(request, "pass_luck.html", {'stu_num': stu_num})

        if page_id == '11':
            stu_num = request.POST.get('stu_id')

            return render(request, "directator_luck.html", {'stu_num': stu_num})

        if page_id == '12':

            #收集directator的数据

            stu_num = request.POST.get('stu_id')
            SH_self_m = request.POST.get('SH_self_m')
            SH_allot_stu_m = request.POST.get('SH_allot_stu_m')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]





            # #选择分配以班级为单位
            radom_stu=models.stu_record.objects.filter(stu_class=rec.stu_class)

            if len(radom_stu)>4:
                for i in range(0,len(radom_stu)-1):
                    #获取一个随机整数
                    random_num=random.randint(0,len(radom_stu)-1)
                    #判断是否为当前学生
                    if radom_stu[random_num].game6:
                        if stu_num != radom_stu[random_num].stu_num:

                            radom_stu_one = radom_stu[random_num]
                            SH_allot_stu_a = radom_stu_one.stu_num
                            rec.SH_self_m = SH_self_m
                            rec.SH_allot_stu_a_m = SH_allot_stu_m
                            rec.SH_allot_stu_a = SH_allot_stu_a
                            rec.save()
                            break
                return render(request, "lucky.html", {'stu_num': stu_num})
            else:
                return HttpResponse('做游戏的人数太少，无法做分配决定')




        if page_id == '13':

            #收集merit的数据

            stu_num = request.POST.get('stu_id')
            L_allot = request.POST.get('L_allot')
            ma=0
            mb=0
            if L_allot == '1':
                ma = 24
                mb = 0
            if L_allot == '2':
                ma = 20
                mb = 4
            if L_allot == '3':
                ma = 16
                mb = 8
            if L_allot == '4':
                ma = 12
                mb = 12
            if L_allot == '5':
                ma = 8
                mb = 16
            if L_allot == '6':
                ma = 4
                mb = 20
            if L_allot == '7':
                ma = 0
                mb = 24


            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            radom_stu = models.stu_record.objects.filter(stu_class=rec.stu_class)

            len_rad=len(radom_stu)
            #计算game1和game2的总成绩
            class_all = 0




            #是否分配大值和小值的标志
            flag_max=0
            flag_min=0
            #存放没有完成game2的记录

            cop=[]

            for j in range(len_rad):
                # 随机数存储
                cop.append(j)

            for i in range(0,len_rad):
                #获取一个随机整数
                if flag_max==1 and flag_min==1:
                    break
                else:
                    random_num=random.choice(cop)
                    #不重复抽取
                    cop.remove(random_num)

                        #判断是否完成第二个游戏
                    if radom_stu[random_num].game6:

                        # 判断是否为当前学生
                        if stu_num != radom_stu[random_num].stu_num:
                            # 计算学生游戏1和游戏2的值



                            if flag_max== 0:
                                # 分配大值
                                L_allot_stu_a = radom_stu[random_num].stu_num
                                rec.L_allot_stu_a = L_allot_stu_a
                                flag_max=1
                            else:

                                if flag_min == 0:

                                    L_allot_stu_b = radom_stu[random_num].stu_num
                                    rec.L_allot_stu_b = L_allot_stu_b
                                    flag_min=1







            rec.L_allot_stu_b_m = mb
            rec.L_allot_stu_a_m = ma


            rec.save()


            return HttpResponse('您已经做完游戏了，谢谢参与')




        else:

            return render(request, "t0_luck.html")

    else:
        page_id = 'luck'

        return render(request, "index.html", {'page_id': page_id})





@csrf_exempt
def Efficiency(request):
    if request.POST:
        page_id = request.POST['page_id']

        if page_id == '1':
            stu_name = request.POST.get('name')
            stu_num = request.POST.get('stu_id')
            stu_class = request.POST.get('stu_class')
            stu_sex = request.POST.get('stu_sex')

            #检查学生学号
            check= models.stu_record.objects.all()
            check_flag=0
            for stu in check:
                if stu.stu_num==stu_num:
                    check_flag=1

            if check_flag==0:

                rec = models.stu_record(stu_name=stu_name, stu_num=stu_num, stu_class=stu_class, stu_sex=stu_sex)
                rec.save()

                data = []
                row = []

                num = models.list_t1s.objects.all()

                for j in range(2):
                    for i in range(0, 3):
                        row.append(num[i + j].t1s)
                    data.append(row)
                    row = []

                return render(request, "temp_effic/t1s_eff.html", {'data': data, 'stu_num': stu_num})
            else:
                return HttpResponse('你的学号被人占用了，你需要请求老师的帮助')

        if page_id == '2':
            stu_num = request.POST.get('stu_id')
            data = []
            row = []

            num_lst = models.list_t1.objects.all()

            for j in range(31):
                for i in range(0, 6):
                    row.append(num_lst[i + j].t1)
                data.append(row)
                row = []

            # nu= request.POST.get('num')

            return render(request, "temp_effic/t1_eff.html", {'data': data, 'stu_num': stu_num})

        # if page_id == '2a':
        #     return render(request, "2a.html")
        # 第二题explain
        if page_id == '3':
            # 收集第一题的数据
            stu_num = request.POST.get('stu_id')
            game1 = request.POST.get('game1')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game1 = game1
            rec.save()

            # 读取示例数据
            data = []
            row = []

            num = models.list_t3s.objects.all()

            for j in range(2):
                for i in range(0, 4):
                    row.append(num[i + j].t3s)
                data.append(row)
                row = []

            return render(request, "temp_effic/t3s_eff.html", {'stu_num': stu_num, 'data': data})
        #

        if page_id == '4':
            stu_num = request.POST.get('stu_id')

            # 显示t3的数据

            data = []
            row = []

            num_lst = models.list_t3.objects.all()

            for j in range(20):
                for i in range(0, 6):
                    row.append(num_lst[i + j].t3)
                data.append(row)
                row = []

            return render(request, "temp_effic/t3_eff.html", {'stu_num': stu_num, 'data': data})

        # 已省去
        # if page_id == '4a':
        #     stu_num = request.POST.get('stu_id')
        #
        #     return render(request, "6a.html", {'stu_num': stu_num})

        # 第三题：黑方块

        if page_id == '5':
            # 收集第二题的数据
            game2 = request.POST.get('game2')
            stu_num = request.POST.get('stu_id')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game2 = game2
            rec.save()

            return render(request, "temp_effic/t2s_eff.html", {'stu_num': stu_num})

        if page_id == '6':
            stu_num = request.POST.get('stu_id')
            return render(request, "temp_effic/t2_eff.html", {'stu_num': stu_num})

        if page_id == '6a':
            stu_num = request.POST.get('stu_id')
            return render(request, "temp_effic/4a_eff.html", {'stu_num': stu_num})
        # 第四题
        if page_id == '7':
            # 收集第三题的数据
            game3 = request.POST.get('game3')
            stu_num = request.POST.get('stu_id')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game3 = game3
            rec.save()

            return render(request, "temp_effic/t4_eff.html", {'stu_num': stu_num})

        if page_id == '7a':
            stu_num = request.POST.get('stu_id')
            return render(request, "temp_effic/7a_eff.html", {'stu_num': stu_num})
        # 第五题
        if page_id == '8':
            # 收集第四题的数据
            stu_num = request.POST.get('stu_id')
            game4 = request.POST.get('game4')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game4 = game4
            rec.save()

            return render(request, "temp_effic/t5_eff.html", {'stu_num': stu_num})
        if page_id == '8a':
            stu_num = request.POST.get('stu_id')
            return render(request, "temp_effic/8a_eff.html", {'stu_num': stu_num})
        # 第六题
        if page_id == '9':
            # 收集第五题的数据

            stu_num = request.POST.get('stu_id')
            game5 = request.POST.get('game5')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game5 = game5
            rec.save()

            return render(request, "temp_effic/t6_eff.html", {'stu_num': stu_num})
        if page_id == '9a':
            stu_num = request.POST.get('stu_id')
            return render(request, "temp_effic/9a_eff.html", {'stu_num': stu_num})

        if page_id == '10':
            # 收集第六题的数据
            stu_num = request.POST.get('stu_id')
            game6 = request.POST.get('game6')
            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            rec.game6 = game6
            rec.save()

            return render(request, "temp_effic/pass_eff.html", {'stu_num': stu_num})

        if page_id == '11':
            stu_num = request.POST.get('stu_id')

            return render(request, "temp_effic/directator_eff.html", {'stu_num': stu_num})

        if page_id == '12':

            # 收集directator的数据

            stu_num = request.POST.get('stu_id')
            SH_self_m = request.POST.get('SH_self_m')
            SH_allot_stu_m = request.POST.get('SH_allot_stu_m')

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]

            # #选择分配以班级为单位
            radom_stu = models.stu_record.objects.filter(stu_class=rec.stu_class)

            if len(radom_stu) > 4:
                for i in range(0, len(radom_stu) - 1):
                    # 获取一个随机整数
                    random_num = random.randint(0, len(radom_stu) - 1)
                    # 判断是否为当前学生
                    if radom_stu[random_num].game6:
                        if stu_num != radom_stu[random_num].stu_num:
                            radom_stu_one = radom_stu[random_num]
                            SH_allot_stu_a = radom_stu_one.stu_num
                            rec.SH_self_m = SH_self_m
                            rec.SH_allot_stu_a_m = SH_allot_stu_m
                            rec.SH_allot_stu_a = SH_allot_stu_a
                            rec.save()
                            break
                return render(request, "temp_effic/efficiency.html", {'stu_num': stu_num})
            else:
                return HttpResponse('做游戏的人数太少，无法做分配决定')

        if page_id == '13':

            # 收集merit的数据

            stu_num = request.POST.get('stu_id')
            E_allot = request.POST.get('E_allot')
            ma = 0
            mb = 0
            if E_allot == '1':
                ma = 24
                mb = 0
            if E_allot == '2':
                ma = 20
                mb = 2
            if E_allot == '3':
                ma = 16
                mb = 4
            if E_allot == '4':
                ma = 12
                mb = 6
            if E_allot == '5':
                ma = 8
                mb = 8
            if E_allot == '6':
                ma = 4
                mb = 10
            if E_allot == '7':
                ma = 0
                mb = 12

            rec = models.stu_record.objects.filter(stu_num=stu_num)[0]
            radom_stu = models.stu_record.objects.filter(stu_class=rec.stu_class)

            len_rad = len(radom_stu)
            # 计算game1和game2的总成绩
            class_all = 0

            # 是否分配大值和小值的标志
            flag_max = 0
            flag_min = 0
            # 存放没有完成game2的记录

            cop = []

            for j in range(len_rad):
                # 随机数存储
                cop.append(j)

            for i in range(0, len_rad):
                # 获取一个随机整数
                if flag_max == 1 and flag_min == 1:
                    break
                else:
                    random_num = random.choice(cop)
                    # 不重复抽取
                    cop.remove(random_num)

                    # 判断是否完成第二个游戏
                    if radom_stu[random_num].game6:

                        # 判断是否为当前学生
                        if stu_num != radom_stu[random_num].stu_num:
                            # 计算学生游戏1和游戏2的值



                            if flag_max == 0:
                                # 分配大值
                                E_allot_stu_a = radom_stu[random_num].stu_num
                                rec.E_allot_stu_a = E_allot_stu_a
                                flag_max = 1
                            else:

                                if flag_min == 0:
                                    E_allot_stu_b = radom_stu[random_num].stu_num
                                    rec.E_allot_stu_b = E_allot_stu_b
                                    flag_min = 1

            rec.E_allot_stu_b_m = mb
            rec.E_allot_stu_a_m = ma

            rec.save()

            return HttpResponse('您已经做完游戏了，谢谢参与')




        else:

            return render(request, "temp_effic/t0_eff.html")

    else:
        page_id = 'efficiency'

        return render(request, "index.html", {'page_id': page_id})


def download(request):
    # 新建excel
    wb = xlwt.Workbook()
    # 添加工作薄

    sh = wb.add_sheet('Sheet1')

    #查找数据库
    rec = models.stu_record.objects.all()

    j=0
    sh.write(0, j, 'Name')
    sh.write(0, j+1, 'Student Number(S)')
    sh.write(0, j+2, 'Sex')
    sh.write(0, j+3, 'Class')
    sh.write(0, j+4, 'Game1')
    sh.write(0, j+5, 'Game2')
    sh.write(0, j+6, 'Game3')
    sh.write(0, j+7, 'Game4')
    sh.write(0, j+8, 'Game5')
    sh.write(0, j+9, 'Game6')
    sh.write(0, j+10, 'Money(S)')
    sh.write(0, j+11, 'SN(T)')
    sh.write(0, j+12, 'Money(T)')
    sh.write(0, j+13, 'SN(A1)')
    sh.write(0, j+14, 'Money(A1)')
    sh.write(0, j+15, 'SN(B1)')
    sh.write(0, j+16, 'Money (B1)')
    sh.write(0, j+17, 'SN(A2)')
    sh.write(0, j+18, 'Money (A2)')
    sh.write(0, j+19, 'SN(B2)')
    sh.write(0, j+20, 'Money(B2)')
    sh.write(0, j+21, 'SN(A3)')
    sh.write(0, j+22, 'Money(A3）')
    sh.write(0, j+23, 'SN(B3)')
    sh.write(0, j+24, 'Money (B3)')


    # 写入数据
    for i in range(len(rec)):
        sh.write(i+1, 0, rec[i].stu_name)
        sh.write(i + 1, 1, rec[i].stu_num)
        sh.write(i + 1, 2, rec[i].stu_sex)
        sh.write(i + 1, 3, rec[i].stu_class)
        sh.write(i + 1, 4, rec[i].game1)
        sh.write(i + 1, 5, rec[i].game2)
        sh.write(i + 1, 6, rec[i].game3)
        sh.write(i + 1, 7, rec[i].game4)
        sh.write(i + 1, 8, rec[i].game5)
        sh.write(i + 1, 9, rec[i].game6)
        sh.write(i + 1, 10, rec[i].SH_self_m)
        sh.write(i + 1, 11, rec[i].SH_allot_stu_a)
        sh.write(i + 1, 12, rec[i].SH_allot_stu_a_m)
        sh.write(i + 1, 13, rec[i].M_allot_stu_a)
        sh.write(i + 1, 14, rec[i].M_allot_stu_a_m)
        sh.write(i + 1, 15, rec[i].M_allot_stu_b)
        sh.write(i + 1, 16, rec[i].M_allot_stu_b_m)
        sh.write(i + 1, 17, rec[i].L_allot_stu_a)
        sh.write(i + 1, 18, rec[i].L_allot_stu_a_m)
        sh.write(i + 1, 19, rec[i].L_allot_stu_b)
        sh.write(i + 1, 20, rec[i].L_allot_stu_b_m)
        sh.write(i + 1, 21, rec[i].E_allot_stu_a)
        sh.write(i + 1, 22, rec[i].E_allot_stu_a_m)
        sh.write(i + 1, 23, rec[i].E_allot_stu_b)
        sh.write(i + 1, 24, rec[i].E_allot_stu_b_m)
        # print(rec)
    wb.save('record/student.xls')

    filename = 'record/student.xls'

    def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(filename))
    response['Content-Type'] = 'application/vnd.ms-excel'
    # 注意filename 这个是下载后的名字
    response['Content-Disposition'] = 'attachment;filename="student.xls"'
    return response

@csrf_exempt
def test(request):
    return render(request,'test.html')

def read_excel(request):
    # 打开excel文件
    ExcelFile = xlrd.open_workbook('wenjuan.xlsx')
    # 获取表单
    #存储四个例子：
    cop_t1s=[]
    cop_t1 = []
    cop_t3s = []
    cop_t3 = []

    for i in range(0,4):

        sheet = ExcelFile.sheet_by_index(i)
        # 读取数据,列的数据
        ncols = sheet.ncols

        # 读取数据,行的数据
        nrow=sheet.nrows

        if i==0:

            for row in range(0, nrow):
                for cols in range(0, ncols):
                    data = sheet.cell_value(row, cols)
                    # cop_t1s.append(data)
                    #写入数据库
                    twz = models.list_t1s(t1s=data)
                    twz.save()

        if i == 1:
            for row in range(0, nrow):
                for cols in range(0, ncols):
                    data = sheet.cell_value(row, cols)
                    #写入数据库
                    # cop_t1.append(data)
                    twz = models.list_t1(t1=data)
                    twz.save()


        if i == 2:
            for row in range(0, nrow):
                for cols in range(0, ncols):
                    data = sheet.cell_value(row, cols)
                    #写入数据库
                    # cop_t3s.append(data)
                    twz = models.list_t3s(t3s=data)
                    twz.save()


        if i == 3:
            for row in range(0, nrow):
                for cols in range(0, ncols):
                    data = sheet.cell_value(row, cols)
                    #写入数据库
                    # cop_t3.append(data)
                    twz = models.list_t3(t3=data)
                    twz.save()



    return  render(request,'test.html',{'t1s':cop_t1s,'t1':cop_t1,'t3s':cop_t3s,'t3':cop_t3})
