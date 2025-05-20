from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.contrib.auth import get_user_model, authenticate, login


def redirect_to_index(request):
    return redirect("/")

def registration_page(request):
    return TemplateResponse(request, "registration.html")

def login_page(request):
    return TemplateResponse(request, "login.html")

def registr_user(request):
    if request.method == "POST":
        uname = request.POST.get("user-name")
        uemail = request.POST.get("user-email")
        upass1 = request.POST.get("user-pass")
        upass2 = request.POST.get("user-pass-repeat")

        print(f"\n{uname}\n")
        if (
            uname == "" or uemail == "" or
            upass1 == "" or upass2 == ""
        ):
            return TemplateResponse(request, "registration.html",
                                    {"message": "ERROR: some field were unfilled"})
        
        if upass1 != upass2:
            return TemplateResponse(request, "registration.html",
                                    {"message": "ERROR: passwords are not the same"})

        user = get_user_model()
        profile = user.objects.create_user(username=uname, email=uemail, password=upass1)
        profile.save()
        return TemplateResponse(request, "registration.html",
                                {"message": "SUCCESS: your account was added to the system"})
    
    return TemplateResponse(request, "registration.html",
                            {"message": "ERROR: invalid method was used"})

def login_user(request):
    if request.method == "POST":
        uemail = request.POST.get("user-email")
        upass = request.POST.get("user-pass")

        if uemail == "" or upass == "":
            return TemplateResponse(request, "login.html",
                                    {"message": "ERROR: some field were unfilled"})

        user = authenticate(request, username=uemail, password=upass)
        if user is not None:
            login(request, user)
            return redirect("/profile")
        else:
            return TemplateResponse(request, "login.html", {
                "message": "ERROR: invalid email or password"
            })

    return TemplateResponse(request, "login.html",
                            {"message": "ERROR: invalid method was used"})

def restore_passwd(request):
    if request.method == "POST":
        uemail = request.POST.get("user-email")

        if uemail == "":
            return TemplateResponse(request, "restore_password.html",
                                    {"message": "ERROR: some field were unfilled"})

        user = authenticate(request, username=uemail, password=upass)
        if user is not None:
            login(request, user)
            return redirect("/profile")
        else:
            return TemplateResponse(request, "login.html", {
                "message": "ERROR: invalid email or password"
            })

    return TemplateResponse(request, "login.html",
                            {"message": "ERROR: invalid method was used"})
