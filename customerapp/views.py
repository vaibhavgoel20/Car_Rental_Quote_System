from django.shortcuts import render 
from django.shortcuts import HttpResponse
from .models import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password
import json
# Create your views here.

def register_view(request):
    if request.POST.get('btn') != None:
        custname = request.POST.get('custname')
        phoneno = request.POST.get('phoneno')
        custcode = request.POST.get('custcode')
        rentdays = request.POST.get('rentdays')
        firstodo = request.POST.get('firstodo')
        custstate = request.POST.get('custstate')
        obj = CustomerDetails()
        obj.cust_name = custname
        obj.phone_no =  phoneno
        obj.cust_code =  custcode 
        obj.days =  rentdays
        obj.first_odo =  firstodo
        obj.cust_state =  custstate
        obj.save()
        context ={
        'Register': "YOUR BOOKING HAS BEEN DONE SUCCESSFULLY !"
        }
        return render(request, "customer/home.html", context)

    return render(request, "customer/home.html")


def viewcustomer_view(request):

    if request.POST.get('btn1') != None:
        custname = request.POST.get('custname')
        phoneno = request.POST.get('phoneno')
        record = CustomerDetails.objects.filter(cust_name = custname , phone_no = phoneno ).first()
        if record:

            context ={
                'Customer_Data': record
            }
            return render(request, "customer/viewcustomer.html", context)
        else:
            context = {
                'Error': " Record Not Found"
            }
        
            return render(request, "customer/viewcustomer.html", context)

    
            


    if request.POST.get('btn2') != None:
        records = CustomerDetails.objects.all()
        context ={
        'Customer_Datab': records
        }
        return render(request, "customer/viewcustomer.html", context)

    return render(request, "customer/viewcustomer.html")




def update_view(request):

    if request.POST.get('btn') != None:
        custname = request.POST.get('custname')
        phoneno = request.POST.get('phoneno')
        rentdays = request.POST.get('rentdays')
        firstodo = request.POST.get('firstodo')
        record = CustomerDetails.objects.filter(cust_name = custname , phone_no = phoneno ).first()
        record.days =  rentdays
        record.first_odo = firstodo
        record.save()
        context ={
            'Result' : "RECORD UPDATED SUCCESSFULLY !"
        }
        return render(request, "customer/update.html",context)
    
    return render(request, "customer/update.html")




def delete_view(request):

    if request.POST.get('btn') != None:
        custname = request.POST.get('custname')
        phoneno = request.POST.get('phoneno')
        record = CustomerDetails.objects.filter(cust_name = custname , phone_no = phoneno )
        record.delete()
        context ={
            'Result' : "RECORD DELETED SUCCESSFULLY !"
        }
        return render(request, "customer/delete.html",context)
    
    return render(request, "customer/delete.html")



def login_view(request):

    if request.POST.get('btn') != None:
        user_name = request.POST.get('uname')
        user_psw = request.POST.get('psw')
        user = authenticate(request, username=user_name, password=user_psw)
        if user is not None:
            login(request,user)
            return render(request, "customer/addcustomer.html")
        else:
            context = {
                "error": "Invalid Username Or Password"
            }
            return render(request,"customer/login.html", context)

    
    if request.POST.get('btn2') != None:
        
        return render(request, "customer/signup.html")

   
    return render(request, "customer/login.html")






def signup_view(request):
    
    if request.POST.get('btn') != None:
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        user_name = request.POST.get('uname')
        user_psw = request.POST.get('psw')
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = user_name
        encrypted_pwd = make_password(user_psw)
        user.password = encrypted_pwd
        user.save()
        login(request, user)
        return render(request, "customer/login.html")


    return render(request, "customer/signup.html")





def logout_view(request):
    logout(request)
    return render(request, "customer/logout.html")





def addcustomer_view(request):
    if request.POST.get('btn') != None:
        custname = request.POST.get('custname')
        phoneno = request.POST.get('phoneno')
        custcode = request.POST.get('custcode')
        rentdays = request.POST.get('rentdays')
        firstodo = request.POST.get('firstodo')
        custstate = request.POST.get('custstate')
        obj = CustomerDetails()
        obj.cust_name = custname
        obj.phone_no =  phoneno
        obj.cust_code =  custcode 
        obj.days =  rentdays
        obj.first_odo =  firstodo
        obj.cust_state =  custstate
        obj.save()
        context ={
        'Register': "YOUR BOOKING HAS BEEN DONE SUCCESSFULLY !"
        }
        return render(request, "customer/addcustomer.html", context)

    return render(request, "customer/addcustomer.html")



def viewbooking_view(request):

    if request.POST.get('btn') != None:
        custname = request.POST.get('custname')
        phoneno = request.POST.get('phoneno')
        finalodo = request.POST.get('finalodo')
        record = CustomerDetails.objects.filter(cust_name = custname , phone_no = phoneno ).first()
        if record:

            mile = float(finalodo) - record.first_odo

            if record.cust_code == 'B':
                price = round(40.00 * record.days + round((mile / 10), 1) * 0.25, 2)

            elif record.cust_code == 'D':
                mile = (mile / 10) / record.days
                if mile <= 100:
                    price = 60.00 * record.days
                else:
                    price = round(60.00 * record.days + round((mile / 10), 1) * 0.25, 2)
            elif record.cust_code == 'W':
                mile = (mile / 10) / record.days
                if mile <= 900:
                    price = 190.00 * record.days
            elif 900 < mile <= 1500:
                price = round(190.00 * record.days + 100.00 * record.days, 2)
            else:
                price = round(190.00 * record.days + round((mile / 10), 1) * 0.25 + 200.00 * record.days, 2)
            #price = "$"+str(price)
            tax = 18/100*(price)
            price = tax + price 

            
        
            obj = BillDetails()
            obj.c_name = custname
            obj.phn_no = phoneno
            obj.c_code = record.cust_code
            obj.c_state = record.cust_state
            obj.no_days =  record.days
            obj.odo_first = record.first_odo
            obj.odo_final = finalodo
            obj.no_miles = mile 
            obj.tax_rate = "18 %"
            obj.amount_tax = tax
            obj.amount_due = price
            obj.save()





            context = {

                'Final_Read': finalodo,
                'Customer_Data': record,
                'Tax_Amount': tax,
                'Miles' : mile,
                'Bill_Amount': price
            }
            return render(request, "customer/viewbooking.html", context)
            
            

    
    
        else:
            context = {
                'Error': " Record Not Found"
            }
        
            return render(request, "customer/viewbooking.html", context)




    







    
    elif request.POST.get('btn2') != None:
        custname = request.POST.get('custname')
        phoneno = request.POST.get('phoneno')
        finalodo = request.POST.get('finalodo')
        record = CustomerDetails.objects.filter(cust_name = custname , phone_no = phoneno ).first()
        if record:

            mile = int(finalodo) - int(record.first_odo)
            

            if record.cust_code == 'B':
                price = round(40.00 * record.days + round((mile / 10), 1) * 0.25, 2)

            elif record.cust_code == 'D':
                mile = (mile / 10) / record.days
                if mile <= 100:
                    price = 60.00 * record.days
                else:
                    price = round(60.00 * record.days + round((mile / 10), 1) * 0.25, 2)
            elif record.cust_code == 'W':
                mile = (mile / 10) / record.days
                if mile <= 900:
                    price = 190.00 * record.days
            elif 900 < mile <= 1500:
                price = round(190.00 * record.days + 100.00 * record.days, 2)
            else:
                price = round(190.00 * record.days + round((mile / 10), 1) * 0.25 + 200.00 * record.days, 2)
            #price = "$"+str(price)
            tax = 18/100*(price)
            price = tax + price 

            
        
            obj = BillDetails()
            obj.c_name = custname
            obj.phn_no = phoneno
            obj.c_code = record.cust_code
            obj.c_state = record.cust_state
            obj.no_days =  record.days
            obj.odo_first = record.first_odo
            obj.odo_final = finalodo
            obj.no_miles = mile 
            obj.tax_rate = "18 %"
            obj.amount_tax = tax
            obj.amount_due = price
            obj.save()





            context = {

                'Final_Read': finalodo,
                'Customer_Data': record,
                'Tax_Amount': tax,
                'Miles' : mile,
                'Bill_Amount': price
            }
            return render(request, "customer/printbill.html", context)
            
            

    
    
        else:
            context = {
                'Error': " Record Not Found"
            }
        
            return render(request, "customer/viewbooking.html", context)





    return render(request, "customer/viewbooking.html")






def ajax_view(request):
    country_name = Country.objects.all()
    state_name = States.objects.all()
    context = {
        'country': country_name,
        'state': state_name
    }


    
    return render(request, "customer/ajax.html" , context)


def state_view(request):
    c_name = request.GET.get('cname')
    print(c_name)
    state_name = States.objects.filter(country__country_name = c_name)
    print(state_name)
    state_names = list()
    for s in state_name:
        state_names.append(s.state_name)
    
    data = json.dumps(state_names)
    return HttpResponse(data, content_type = 'application/json')


def name_search_view(request):
    if(request.method=="GET"):
        init_name = request.GET.get("name_intial")
        names = list()
        if init_name:
            result = CustomerDetails.objects.filter(cust_name__contains = init_name)
            for r in result:
                names.append(r.cust_name)

    data = json.dumps(names)
    return HttpResponse(data, content_type = 'application/json')

    

    

def viewbills_view(request):
    
    
    if request.POST.get('btn') != None:
        fromdate = request.POST.get('billdate')
        todate = request.POST.get('billdate2')
        print("from date..",fromdate)
        print("To date..",todate)
        billrecord = BillDetails.objects.filter(created_at__gte = fromdate  , created_at__lte = todate )
        if billrecord:

            context ={
                'Customer_Bill': billrecord
            }
            return render(request, "customer/viewbills.html", context)
        else:
            context = {
                'Error': " Record Not Found"
            }
        
            return render(request, "customer/viewbills.html", context)

    
        

    return render(request, "customer/viewbills.html")






def printbill_view(request):
    
   

    return render(request, "customer/printbill.html")
