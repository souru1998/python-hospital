from django.shortcuts import render,redirect
from .models import appointmenttable,contacttable,registrationtable,adminregistertable
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def index(request):
    return render(request,'index.html')

def inpage(request):
    return render(request,'innerpage.html')

def login(request):
    return render(request,'login.html')

def demo(request):
    return render(request,'demo.html')

def contview(request):
    return render(request,'cont view.html')

def table(request):
    return render(request,'table.html')

def appointtable(request):
    return render(request,'appointtable.html')

def upappointment(request):
    return render(request,'upappointment.html')

def register(request):
    return render(request,'registrationform.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def department(request):
    return render(request,'department.html')

def doctors(request):
    return render(request,'doctors.html')

def appointment(request):
    return render(request,'appointment.html')

def contact(request):
    return render(request,'contact.html')



# def adminlogin(request):
#     return render(request,'admin/adminlogin.html')

def adminreg(request):
    return render(request,'admin/adminregister.html')

def admindash(request):
    if request.session.has_key('aid'):
        apponitmentdata=appointmenttable.objects.all()
        return render(request,"admin/admindash.html",{'appo':apponitmentdata})
    else:
        return render(request,'admin/adminlogin.html')
    

def allmembers(request):
        registrationform=registrationtable.objects.all()
        return render(request,'admin/allmembers.html',{'member':registrationform})
  



def appointmentform(request):
    dict1={}
    try:
        a_name=request.POST['name']
        a_email=request.POST['email']
        a_phone=request.POST['phone']
        a_date=request.POST['date']
        a_depart=request.POST['department']
        a_doc=request.POST['doctor']
        a_message=request.POST['message']
         ####
        
        subject = 'Message from Medilab Users'
        message = 'appointment schedule'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message,email_from, recipient_list)
        ####
        subject = 'Thank you'
        message = f'hello {a_name},your appointment scheduled at{a_date} to {a_doc} for {a_depart}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [a_email, ]
        send_mail(subject,message,email_from,recipient_list)
        add=appointmenttable(name=a_name,email=a_email,phone=a_phone,date=a_date,depart=a_depart,doc=a_doc,message=a_message)
        add.save()
        dict1['msg']='We registerd your appointment'
        return render(request,'demo.html',dict1)
    except Exception as e:
        print(e)
        dict1['msg']='Sorry ,try again'
        return render(request,'index.html',dict1)
    
def contactform(request):
    dict2={}
    try:
        c_name=request.POST['name']
        c_email=request.POST['email']
        c_subject=request.POST['subject']
        c_message=request.POST['message']
         ####
        subject = 'Message from Medilab Users'
        message = f'name:{c_name} ,email:{c_email}, message:{c_message}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message,email_from, recipient_list)
        ####
        subject = 'Thank you for contacting us'
        message = f'hello:{c_name}, Thanks for choosing us, Have a nice day'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [c_email, ]
        send_mail(subject,message,email_from,recipient_list)

        add=contacttable(name=c_name,email=c_email,subject=c_subject,message=c_message)
        add.save()
        dict2['msg3']='Thank you'
        return render(request,'demo.html',dict2)
    except Exception as e:
        print(e)
        dict2['msg3']='sorry!,try again'
        return render(request,'index.html',dict2) 
    

#contact view

def contactview(request):
    cont=contacttable.objects.all()
    return render(request,'table.html',{'con':cont})
     

#appointment view

def appointmentview(request):
    appoint=appointmenttable.objects.all()
    return render(request,'appointtable.html',{'appo':appoint})



#updating contact section

def contactupdate(request):
    if request.method=='POST':
        c_name=request.POST['name']
        c_email=request.POST['email']
        c_subject=request.POST['subject']
        c_message=request.POST['message']
        registerid=request.GET['iid']
        contactdata=contacttable.objects.filter(id=registerid).update(name=c_name,email=c_email,subject=c_subject,message=c_message)
        return redirect('/conview/')
    else:
        registerid=request.GET['iid']
        contactdata=contacttable.objects.filter(id=registerid)
        return render(request,'updatedcontact.html',{'con':contactdata})

#deleting contact section
def contactdelete(request):
    registerid=request.GET['iid']
    contactdata=contacttable.objects.filter(id=registerid).delete()
    return redirect('/conview/')


#updating appointment section
def appointmentupdate(request):
    if request.method=='POST':
        a_name=request.POST['name']
        a_email=request.POST['email']
        a_phone=request.POST['phone']
        a_date=request.POST['date']
        a_depart=request.POST['department']
        a_doc=request.POST['doctor']
        a_message=request.POST['message']
        registerid=request.GET['iid']
        apponitmentdata=appointmenttable.objects.filter(id=registerid).update(name=a_name,email=a_email,phone=a_phone,date=a_date,depart=a_depart,doc=a_doc,message=a_message)
        return redirect('/appointview/')
    else:
        registerid=request.GET['iid']
        apponitmentdata=appointmenttable.objects.filter(id=registerid)
        return render(request,'upappointment.html',{'appo':apponitmentdata})
    
#deleting appointment section
def appointmentdelet(request):
    registerid=request.GET['iid']
    apponitmentdata=appointmenttable.objects.filter(id=registerid).delete()
    return redirect('/appointview/')


#registraion form
def registrationform(request):
    dict3={}
    try:
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        eemail = request.POST['email']
        passwo = request.POST['password']
        r_passwo = request.POST['re_password']
        if passwo == r_passwo:
            add=registrationtable(finame=firstname,laname=lastname,emaill=eemail,passwords=passwo,re_passwords=r_passwo)
            add.save()
            dict3['msg3']='Registered Successfull'
            return render(request,'login.html',dict3)
        else:
            dict3['msg3']='Oops,something went wrong'
            return render(request,'registrationform.html',dict3)

    except Exception as e:
        print(e)
        dict3['msg3']='Oops, Try again!'
        return render(request,'registrationform.html',dict3)

#login section
def loginform(request):
    if request.method =='POST':
        l_email=request.POST['email']
        l_password=request.POST['password']
        check=registrationtable.objects.filter(emaill=l_email,passwords=l_password)
        if check:
            for i in check:
                request.session['id']=i.id
                request.session['fname']=i.finame
                
            return render(request, 'index.html',{"success":"Welcome to medilab"})
        else:
            return render(request,'login.html',{"error":"Something went wrong,Please try again"})
    else:
        return render(request,'index.html')
    
# #logout section
def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        del request.session['fname']
    return redirect('/')



#admin registration form
def adminregistrationform(request):
    dict4={}
    try:
        a_name = request.POST['name']
        a_email = request.POST['email']
        a_password = request.POST['password']
        a_repassword = request.POST['re_password']
        if a_password == a_repassword:
            add=adminregistertable(name=a_name,email=a_email,password=a_password,ree_password=a_repassword)
            add.save()
            dict4['msg4']='success'
            return render(request,'admin/adminlogin.html',dict4)
        else:
            dict4['msg4']='somthing wrong'
            return render(request,'admin/adminregister.html',dict4)
    except Exception as e:
        print(e)
        dict4['msg4']='somthing wrong'
        return render(request,'admin/adiminregister.html',dict4)

    

def adminloginform(request):
    if request.method == 'POST':
        al_email= request.POST['email']
        al_password = request.POST['password']
        check = adminregistertable.objects.filter(email=al_email,password=al_password)
        if check:
            for i in check:
                request.session['aid']=i.id
                request.session['aname']=i.name
                apponitmentdata=appointmenttable.objects.all()

                return render(request,'admin/admindash.html',{'appo':apponitmentdata})
            # else:
            #     return render(request,'admin/adminlogin.html')
        else:
            return render(request,'admin/adminlogin.html',{'error':'somthing wrong'})
    else:
        return render(request,'admin/adminlogin.html')


def adminlogout(request):
    if request.session.has_key('aid'):
        del request.session['aid']
        del request.session['aname']
    return redirect('/adminlogin/')
