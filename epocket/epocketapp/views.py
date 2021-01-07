from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from collections import defaultdict 
import pymysql
import json
db=pymysql.connect("localhost","root","","epocket")
c=db.cursor()
cursor = db.cursor(pymysql.cursors.DictCursor)

# Create your views here.

def index(request):
    return render(request,"index.html")
def login(request):
    data={}
    if(request.POST):
        uname=request.POST['uname']
        pword=request.POST['pword']
        q="select count(uname) from login where uname='"+uname+"' and pword='"+pword+"'"
        c.execute(q)
        cn=c.fetchone()
        if(cn[0]>0):
           q1="select * from login where uname='"+uname+"' and pword='"+pword+"'"
           c.execute(q1)
           data=c.fetchone()
           request.session['rid']=data[1]
           return HttpResponseRedirect("/userhome")
        else:
            msg="invalid"
            return render(request,"login.html",{"msg":msg})        
    return render(request,"login.html")
def userhome(request):
    return render(request,"userhome.html")
def reg(request):
    if(request.POST):
        name=request.POST['sname']
        age=request.POST['age']
        addr=request.POST['addr']
        place=request.POST['place']
        dob=request.POST['dob']
        email=request.POST['email']
        pword=request.POST['pword']
        q="insert into reg(name,age,addr,place,dob,email)values('"+name+"','"+age+"','"+addr+"','"+place+"','"+dob+"','"+email+"')"
        c.execute(q)
        
        q1="insert into login(rid,uname,pword,utype)values((select max(rid) from reg),'"+email+"','"+pword+"','user')"
        c.execute(q1)
        
        q1="insert into incometype(rid,incometype)values((select max(rid) from reg),'Salary')"
        c.execute(q1)
        
        q1="insert into incometype(rid,incometype)values((select max(rid) from reg),'Household income')"
        c.execute(q1)
        
        q1="insert into expensetype(rid,expensetype)values((select max(rid) from reg),'Food')"
        c.execute(q1)
        
        q1="insert into expensetype(rid,expensetype)values((select max(rid) from reg),'Travel')"
        c.execute(q1)
        db.commit()
        return render(request,"reg.html")
    return render(request,"reg.html")

def expensetype(request):
    if(request.POST):
        rid=str(request.session['rid'])
        etype=request.POST['etype']
        q="insert into expensetype(rid,expensetype)values('"+rid+"','"+etype+"')"
        c.execute(q)
        db.commit()
    return render(request,"expensetype.html")

def expense(request):
    rid=str(request.session['rid'])
    if(request.POST):
        
        etype=request.POST['etype']
        expense=request.POST['expense']
        amt=request.POST['amt']
        dt=request.POST['dt']
        q="insert into expense(rid,etype,amt,dt,etypeid)values('"+rid+"','"+expense+"','"+amt+"','"+dt+"','"+etype+"')"
        c.execute(q)
        db.commit()
    q="select * from expensetype where rid='"+rid+"'"
    c.execute(q)
    expensetype=c.fetchall()
    q="select expense.*,expensetype.expensetype from expensetype,expense where expense.rid='"+rid+"' and expense.etypeid=expensetype.etypeid"
    c.execute(q)
    expense=c.fetchall()
    return render(request,"expense.html",{"etype":expensetype,"expense":expense})

def incometype(request):
    if(request.POST):
        rid=str(request.session['rid'])
        itype=request.POST['itype']
        q="insert into incometype(rid,incometype)values('"+rid+"','"+itype+"')"
        c.execute(q)
        db.commit()
    return render(request,"incometype.html")

def income(request):
    rid=str(request.session['rid'])
    if(request.POST):
        income=request.POST['income']
        itype=request.POST['itype']
        amt=request.POST['amt']
        dt=request.POST['dt']
        q="insert into income(rid,itype,amt,dt,itypeid)values('"+rid+"','"+income+"','"+amt+"','"+dt+"','"+itype+"')"
        c.execute(q)
        db.commit()
    q="select * from incometype where rid='"+rid+"'"
    c.execute(q)
    incometype=c.fetchall()
    q="select income.*,incometype.incometype from incometype,income where income.rid='"+rid+"' and income.itypeid=incometype.itypeid"
    c.execute(q)
    income=c.fetchall()
    return render(request,"income.html",{"itype":incometype,"income":income})

def budget(request):
    rid=str(request.session['rid'])
    if(request.POST):
        
        budget=request.POST['budget']
        bfrom=request.POST['bfrom']
        bto=request.POST['bto']
        q="insert into budget(rid,budgetname,bfrom,bto)values('"+rid+"','"+budget+"','"+bfrom+"','"+bto+"')"
        c.execute(q)
        db.commit()
    q="select count(*) from budget where rid='"+str(rid)+"'"
    c.execute(q)
    b=c.fetchone()
    budget="BUDGET"+str(b[0]+1)
    q="select * from budget where rid='"+str(rid)+"'"
    c.execute(q)
    budgets=c.fetchall()
    return render(request,"budget.html",{"budget":budget,"budgets":budgets})

def budgetlist(request):
    bid=request.GET.get("id")
    rid=str(request.session['rid'])
    if(request.POST):
        
        etype=request.POST['etype']
        amt=request.POST['amt']
        q="insert into budgetlist(bid,etype,amt)values('"+bid+"','"+etype+"','"+amt+"')"
        c.execute(q)
        db.commit()
        return HttpResponseRedirect("/budget")
    q="select * from expensetype where rid='"+str(rid)+"'"
    c.execute(q)
    etype=c.fetchall()
    q="select expensetype.expensetype,budgetlist.amt from budgetlist,expensetype where budgetlist.bid='"+str(bid)+"' and budgetlist.etype=expensetype.etypeid"
    c.execute(q)
    budget=c.fetchall()
    q="select sum(amt) from budgetlist where bid='"+str(bid)+"'"
    c.execute(q)
    tot=c.fetchone()
    total=tot[0]
    return render(request,"budgetlist.html",{"etype":etype,"budget":budget,"total":total})

def allbudget(request):
    rid=str(request.session['rid'])
    q="select * from budget where rid='"+str(rid)+"'"
    c.execute(q)
    budget=c.fetchall()
    return render(request,"allbudget.html",{"budget":budget})

def budgetview(request):
    rid=str(request.session['rid'])
    bid=request.GET.get("id")
    q="select * from budget where bugetid='"+str(bid)+"'"
    c.execute(q)
    data=c.fetchone()
    d1=data[3]
    d2=data[4]
    q="select expensetype.expensetype,budgetlist.amt from budgetlist,expensetype where budgetlist.bid='"+str(bid)+"' and budgetlist.etype=expensetype.etypeid"
    c.execute(q)
    budget=c.fetchall()
    q="select sum(amt) from budgetlist where bid='"+str(bid)+"'"
    c.execute(q)
    tot=c.fetchone()
    total=tot[0]
    q="select income.*,incometype.incometype from incometype,income where income.rid='"+rid+"' and income.itypeid=incometype.itypeid and (income.dt between '"+str(d1)+"' and '"+str(d2)+"')"
    print(q)
    c.execute(q)
    income=c.fetchall()
    print(income)
    inctotal=0
    q="select sum(amt) from income where rid='"+str(rid)+"' and (dt between '"+str(d1)+"' and '"+str(d2)+"')"
    c.execute(q)
    inctot=c.fetchone()
    if(inctot[0]!="None"):
        inctotal=inctot[0]
    exptotal=0
    q="select sum(amt) from expense where rid='"+str(rid)+"' and (dt between '"+str(d1)+"' and '"+str(d2)+"')"
    c.execute(q)
    exptot=c.fetchone()
    if(exptot[0]!="None"):
        exptotal=exptot[0]
    q="select expense.*,expensetype.expensetype from expensetype,expense where expense.rid='"+str(rid)+"' and expense.etypeid=expensetype.etypeid and (expense.dt between '"+str(d1)+"' and '"+str(d2)+"')"
    c.execute(q)
    expense=c.fetchall()

    savings=0
    import datetime
    now = datetime.date.today()
    if(now>d2):
        if(inctotal==None):
            inctotal=0
        if(exptotal==None):
            exptotal=0
        savings=inctotal-exptotal
        # if(savings>0):
        #     q="select count(*) from savings where budgetid='"+str(bid)+"'"
        #     c.execute(q)
        #     count=c.fetchone()
        #     if(count[0]==0):
        #         q="insert into savings(budgetid,savings) values('"+str(bid)+"','"+str(savings)+"')"
        #         c.execute(q)
        #         db.commit()
    return render(request,"budgetview.html",{"budget":budget,"total":total,"income":income,"expense":expense,"inctotal":inctotal,"exptotal":exptotal,"savings":savings})

def dates(request):
    rid=str(request.session['rid'])
    if(request.POST):
        
        brom=request.POST['bfrom']
        bto=request.POST['bto']
        gtype=request.POST['type']
        request.session['bfrom']=brom
        request.session['bto']=bto
        request.session['gtype']=gtype
        q="select count(*) from income where dt between '"+brom+"' and '"+bto+"' and rid='"+rid+"'"
        print(q)
        c.execute(q)
        income=c.fetchone()
        print(income)
        q="select count(*) from expense where dt between '"+brom+"' and '"+bto+"' and rid='"+rid+"'"
        c.execute(q)
        expense=c.fetchone()
        if(income[0]>0 or expense[0]>0):
            q="select cast(dt as char),amt from expense where (dt between '"+brom+"' and '"+bto+"') and rid='"+rid+"'"
            print(q)
            c.execute(q)
            expense=c.fetchall()
            q="select cast(dt as char),amt from income where (dt between '"+brom+"' and '"+bto+"') and rid='"+rid+"'"
            c.execute(q)
            income=c.fetchall()
            import pandas as pd
            import pandas as pd1
            import matplotlib.pyplot as plt1
            import matplotlib.pyplot as plt2
            if(gtype=="Income"):
                data=income
                df1 = pd.DataFrame(data,columns=['Date','Income in Rupees'])
                df1.plot(x ='Date', y='Income in Rupees', kind = 'bar')
                plt1.show()
            else:
                data1=expense
                df2 = pd1.DataFrame(data1,columns=['Date','Expense in Rupees'])
                df2.plot(x ='Date', y='Expense in Rupees', kind = 'bar')
                plt2.show()
            # return HttpResponseRedirect("/graph")
    return render(request,"dates.html")

def graph(request):
    rid=str(request.session['rid'])
    bfrom=request.session['bfrom']
    bto=request.session['bto']
    gtype=request.session['gtype']
    # q="select cast(dt as char) from income where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    # c.execute(q)
    # idate=c.fetchall()
    # q="select amt from income where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    # c.execute(q)
    # iamt=c.fetchall()
    # # income=dict(zip(idate,iamt))
    # # print(idate[0][0])
    # # print(iamt)
    # # print(income)
    # for i in idate:
    #     income
    # q="select cast(dt as char) from expense where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    # print(q)
    # c.execute(q)
    # date=c.fetchall()
    # jsonEdate= json.dumps(date)
    q="select cast(dt as char),amt from expense where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    print(q)
    c.execute(q)
    expense=c.fetchall()
    # jsonExpense = json.dumps(expense)
    # print(expense)
    q="select cast(dt as char),amt from income where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    c.execute(q)
    income=c.fetchall()
    print(income)
    # jsonIdate = json.dumps(edate)
    # q="select amt from income where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    # c.execute(q)
    # income=c.fetchall()
    # jsonIncome = json.dumps(income)
    import pandas as pd
    import pandas as pd1
    import matplotlib.pyplot as plt1
    import matplotlib.pyplot as plt2
    if(gtype=="Income"):
        data=income
        df1 = pd.DataFrame(data,columns=['Date','Income in Rupees'])
        df1.plot(x ='Date', y='Income in Rupees', kind = 'bar')
        plt1.show()
    else:
        data1=expense
        df2 = pd1.DataFrame(data1,columns=['Date','Expense in Rupees'])
        df2.plot(x ='Date', y='Expense in Rupees', kind = 'bar')
        plt2.show()
    # return render(request,"graph.html",{"idate":jsonIdate,"income":jsonIncome,"edate":jsonEdate,"expense":jsonExpense})
    return render(request,"graph.html")
def idate(request):
    rid=str(request.session['rid'])
    bfrom=request.session['bfrom']
    bto=request.session['bto']
    q="select cast(dt as char) from income where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    c.execute(q)
    edate=c.fetchall()
    jsonIdate = json.dumps(edate)
    return HttpResponse(jsonIdate)
def jsonIncome(request):
    rid=str(request.session['rid'])
    bfrom=request.session['bfrom']
    bto=request.session['bto']
    q="select amt from income where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    c.execute(q)
    income=c.fetchall()
    jsonIncome = json.dumps(income)
    return HttpResponse(jsonIncome)
def edate(request):
    rid=str(request.session['rid'])
    bfrom=request.session['bfrom']
    bto=request.session['bto']
    q="select cast(dt as char) from expense where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    c.execute(q)
    edate=c.fetchall()
    jsonEdate = json.dumps(edate)
    return HttpResponse(jsonEdate)
def jsonExpense(request):
    rid=str(request.session['rid'])
    bfrom=request.session['bfrom']
    bto=request.session['bto']
    q="select amt from expense where (dt between '"+bfrom+"' and '"+bto+"') and rid='"+rid+"'"
    c.execute(q)
    expense=c.fetchall()
    jsonExpense = json.dumps(expense)
    return HttpResponse(jsonExpense)
def loan(request):
    rid=str(request.session['rid'])
    if(request.POST):
        
        loan=request.POST['loan']
        lender=request.POST['lender']
        amount=request.POST['amt']
        sdate=request.POST['sdate']
        endate=request.POST['endate']
        interest=request.POST['interest']
        
        q="insert into loan(rid,loanname,lender,amount,sdate,endate,interest,loanstatus)values('"+rid+"','"+loan+"','"+lender+"','"+amount+"','"+sdate+"','"+endate+"','"+interest+"','active')"
        c.execute(q)
        db.commit() 
    q="select * from loan where rid='"+rid+"'"
    c.execute(q)
    data=c.fetchall()
    return render(request,"loan.html",{"data":data})
def savings(request):
    rid=str(request.session['rid'])
    if(request.POST):
        
        savings=request.POST['savings']
        date=request.POST['date']
        
        amount=request.POST['amt']
        src=request.POST['src']
         
        q="insert into savings(rid,savings,source,amount,sdate)values('"+rid+"','"+savings+"','"+src+"','"+amount+"','"+date+"')"
        c.execute(q)
        db.commit() 
    q="select * from savings where rid='"+rid+"'"
    c.execute(q)
    data=c.fetchall()
    return render(request,"savings.html",{"data":data})