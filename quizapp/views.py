from django.shortcuts import redirect, render
from .models import * 

# xxxxxxxxxxxxxxxx saving to data base xxxxxxxxxxxxxxxxxxxxxxxxxx
 

def signup(request):
    if (request.method == 'POST'):
        name = request.POST['namex']
        place = request.POST['placex']
        email = request.POST['emailx']
        password = request.POST['passwordx']
        password_2 = request.POST['passwordxx']
        contact = int(request.POST['contactx'])
        sign_up = signup_form(Name=name, Place=place, Email=email,
                              Password=password, Re_password=password_2, Contact=contact)
        sign_up.save()
        return redirect('signuptable')

    return render(request, 'signupform.html')
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# xxxxxxxxxxxxxxx  TO DISPLAY IN TABLE XXXXXXXXXXXXXXXXXXXXX


def signuptable(request):
    sign_up = signup_form.objects.all()
    return render(request, 'signuptable.html', {'reg': sign_up})
# xxxxxxxxxxxxxxx DELETE xxxxxxxxxxxxxxxxxxxx


def deletetable(request, deletex):
    sign_up = signup_form.objects.get(id=deletex).delete()

    return redirect('signuptable')
# xxxxxxxxxxxxxxx UPDATE TABLE XXXXXXXXXXXXXXXXXXXXXXXX


def updatetable(request):
    userdata = signup_form.objects.get(id=deletex)
    return render(request, 'update.html', {'userdata': userdata})


# Create your views here.

# xxxxxxxxxxxxx inheritance sample xxxxxxxxxxxxxxxxxxxxxxxxx
def home1fun(request):
    return render(request, 'home1.html')


def home2fun(request):
    return render(request, 'home2.html')


def home3fun(request):
    return render(request, 'home3.html')

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def adminhomefun(request):
    return render(request, 'adminhome.html')


def loginfun(request):
    if(request.method == 'POST'):
        usernamex = request.POST['userxx']
        passwordx = request.POST['passwordxx']

        try:
            user_name = admin_reg.objects.get(username=usernamex)

            if(user_name.username == usernamex and user_name. password == passwordx):
                return render(request, 'adminhome.html')
            else:

                return render(request, 'login.html', {'message': 'login failed'})

        except admin_reg.DoesNotExist:
            return render(request, 'login.html', {'message': 'login failed'})

    return render(request, 'login.html')


def addquestion(request):
    if(request.method == 'POST'):
        question = request.POST['addquestionx']
        category = request.POST['categoryx']
        option_a = request.POST['option_ax']
        option_b = request.POST['option_bx']
        option_c = request.POST['option_cx']
        option_d = request.POST['option_dx']
        correct_ans = request.POST['correctansx']
        obj_qestion = Quiz_question(Questions=question, Category=category, Option_A=option_a,
                                    Option_B=option_b, Option_C=option_c, Option_D=option_d, Answer=correct_ans)
        obj_qestion.save()

    return render(request, 'addquestion.html')


def test2fun(request):
    return render(request, 'test2.html')


def test3fun(request):
    return render(request, 'test3.html')


def adminfirstpage(request):
    return render(request, 'adminfirstpage.html')


def homefun(request):
    return render(request, 'homepage.html')


def adminpage(request):
    return render(request,'admin_page.html')
