from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def index(req):
    return render(req,'index.html')

def add(req):
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    # p1 = Product(name='orange',price=140)
    # p2 = Product(name='apple', price=150)
    # p3 = Product(name='tomat', price=155)
    # c1 = Company.objects.get(title='J7')
    # c2 = Company.objects.get(title='DOBRY')
    # c2.product_set.add(p1, bulk=False)
    # c2.product_set.add(p2, bulk=False)
    # c2.product_set.add(p3, bulk=False)
    # print(c2.product_set.count())
    # print(c2.product_set.values_list())
    # s1 = Student.objects.create(name='Viktor',group='G001')
    # s2 = Student.objects.create(name='Boris', group='G001')
    # s3 = Student.objects.create(name='Max', group='G001')
    # s4 = Student.objects.create(name='Igor', group='G002')
    # s5 = Student.objects.create(name='Zahar', group='G002')
    # k1 = Course.objects.create(title='Math')
    # k2 = Course.objects.create(title='Geo')
    # k1.student_set.add(s1,s3,s5)
    # k1.student_set.add(s3)
    # k1.student_set.add(s5)
    # k2.student_set.add(s1,s2,s3)
    # k2.student_set.add(s2)
    # k2.student_set.add(s3)
    # u1 = User.objects.create(name='Sasha')
    # ac1 = Account.objects.create(login='asd', password='12345', user=u1)
    return redirect('home')

def table1(req):
    #заходим на страницу
    baza = Product.objects.all()
    anketa = FormaSok()
    bd=[]
    if req.POST:#нажали на кнопку submit
        #bd = []
        anketa = FormaSok(req.POST)#форма с прошлым запросом
        a = req.POST['firma']#собираем данные
        b = req.POST['sok']
        print(a,b,'####################')
        #выбираем таблицу для вывода
        if a and not b:
            baza = Product.objects.filter(firma_id=a)
        elif b and not a:
            c = Product.objects.get(id=b).name
            baza = Product.objects.filter(name=c)
        elif a and b:
            c = Product.objects.get(id=b).name
            baza = Product.objects.filter(firma_id=a, name=c)
        else:
            baza = Product.objects.all()
    #заполняется таблица
    for i in baza:
        bd.append([i.name,i.price,i.firma.title])
        # bd.append(i.price)
        # bd.append(i.firma.title)
    print(bd)
    title = ['Название','Цена','Фирма']#строка с заголовком

    data={'table':bd,'title':title,'forma':anketa}#данные для вывода
    return render(req,'totable.html',context=data)


def table2(req):
    # заходим на страницу
    baza = Student.objects.all()
    anketa = ''
    bd=[]
    for i in baza:
        temp=i.course.all()
        kursi=''
        for t in temp:
            kursi+=t.title + ' '
        bd.append([i.name,i.group,kursi])
    title = ['Имя', 'Группа', 'Курсы']  # строка с заголовком
    data = {'table': bd, 'title': title, 'forma': anketa}  # данные для вывода
    return render(req, 'totable.html', context=data)

def table3(req):
    #заходим на страницу
    baza = User.objects.all()
    anketa = FormaUser()
    bd=[]
    if req.POST:#нажали на кнопку submit
        #bd = []
        anketa = FormaUser(req.POST)#форма с прошлым запросом
        a = req.POST['user']#собираем данные
        #print(a,b,'####################')

        baza = User.objects.filter(id=a)

    for i in baza:
        bd.append([i.name,i.account.login,i.account.password])

    print(bd)
    title = ['Имя','Логин','Пароль']#строка с заголовком

    data={'table':bd,'title':title,'forma':anketa}#данные для вывода
    return render(req,'totable.html',context=data)
