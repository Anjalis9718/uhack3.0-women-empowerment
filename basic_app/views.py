from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm,SkillsForm,RateForm
from .models import User,Counsellor,n_g_o



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def skills_page(request):
    skill=None
    submitted = False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        skills_form=SkillsForm(data=request.POST)

        if user_form.is_valid() and skills_form.is_valid():
            user = User.objects.get(pk=username)




            user.userprofileinfo.Area_of_Interests = "NNGO"
            user.save()

        else:
            print("Error")
    else:
        return render(request,'basic_app/index.html')

    return render(request,'basic_app/index.html',{'skills_form':skills_form,'user_form':user_form,'skill':skill,'submitted':submitted})

def counsellors(request):
    list=Counsellor.objects.all()
    return render(request,'basic_app/counsellor.html',{'list':list})

def ngos(request):
    ngo = n_g_o.objects.all()
    return render(request,'basic_app/ngo.html',{'ngo':ngo})

def rateorg(request):
    if request.method == 'POST':
            rate_form = RateForm(data=request.POST)
            if rate_form.is_valid() :
                rate_organisation=rate_form.save()
                rate_organisation.save()
            else:
                print("error")
    else:
        rate_form = RateForm()

    return render(request,'basic_app/rate_organisation.html',{'rate_form':rate_form})


    return render(request,'basic_app/rate_organisation.html')

def index(request):
    ##submitted = False
    #if request.method=="POST":

        #skills_form=SkillsForm(data=request.POST)

        #if  skills_form.is_valid():
            #user = User.objects.get(pk=user_id)

            #user.save()

            #skill = skills_form.save()
            #skill.user = user
            #skill.save()
            #submitted = True
        #else:
            #print("Error")
    #else:
        #return render(request,'basic_app/index.html')
        #'skills_form':skills_form,'user_form':user_form,'skill':skill,'submitted':submitted
    return render(request,'basic_app/index.html',{})

def who_we_are(request):
    return render(request,'basic_app/who_we_are.html')



@login_required
def LoggedIn(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'

    return render(request,'basic_app/LoggedIn.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))


            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})
