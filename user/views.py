from django.shortcuts import render,redirect
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    UserAccountForm
)
from django.contrib.auth import( 
    authenticate,
    login,
    logout
)
from .Validation import User
from django.contrib.auth.models import User
from django.contrib import messages 
from .Utils import UserInitialiser


# Create your views here.
def register_view(request):
    
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            messages.success(request,f'User registration successful {form.cleaned_data.get("username")}')
            form.save()
            UserInitialiser(User.objects.get(username=form.cleaned_data.get("username")))
            login(request, User.objects.get(username=form.cleaned_data.get("username")))
            return redirect('blog-home')

        else:

            return render(
                request=request,
                template_name='register.html',
                context={
                    'form':form,
                    'name':'Sign Up',
                }
            )
            
    form = UserRegistrationForm()
    return render(
        request=request,
        template_name='register.html',
        context={
            'form':form,
            'name':'Sign Up',
        }
    )
    
def login_view(request):
    
    if(request.method == 'GET'):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form, 'name':'Login', 'err':''})
    
    elif(request.method == 'POST'):
        form = UserLoginForm(request.POST)
        
        if(form.is_valid()):
            #authenticating user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('username')
            try:
                user_e= User.objects.get(email = email)
            except Exception as e:
                pass
            user = authenticate(username = username,password = raw_password)
            if(user is not None and user.is_authenticated):
                login(request=request, user=user)
                messages.success(request, f'{username} has logged in successfully')
                return redirect('blog-home')
            elif(user_e is not None and user_e.check_password(raw_password)):
                #checks the password of the user
                login(request=request, user=user_e)
                messages.success(request, f'{user_e} has logged in successfully')
                return redirect('blog-home')
          
            
        return render(
        request=request,
        template_name='login.html',
            context={
                'form':form,
                'name':'Log In | Error',
                'err':'Username or Password is incorrect.'
            }
        )
    
def account_reset_view(request):
    return redirect('user-login')

def user_account_view(request):
    form = UserAccountForm()
    if(request.method == 'GET'):
        
        form.fields["username"].initial = request.user.username
        form.fields["email"].initial = request.user.email
        form.fields["first_name"].initial = request.user.first_name
        form.fields["last_name"].initial = request.user.last_name
        
        return render(
            request=request,
            template_name='user_account.html',
            context={
                'name':'My Accout',
                'user':request.user,
                'form':form
            }
        )
            
            
def logout_user(request):
    if(request.user.is_authenticated):
        logout(request=request)
        return redirect('user-login')