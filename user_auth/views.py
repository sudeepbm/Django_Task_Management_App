from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import re

# Password validation function
def validate_password(password):
    """
    Validate password based on the following criteria:
    - Length between 6 and 12 characters
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one number
    - At least one special character from [$#@]
    """
    if len(password) < 6 or len(password) > 12:
        return "Invalid Password. Length must be between 6 and 12 characters"

    lower_case_pattern = re.compile(r'[a-z]')
    upper_case_pattern = re.compile(r'[A-Z]')
    number_pattern = re.compile(r'\d')
    special_character_pattern = re.compile(r'[$#@]')

    if not lower_case_pattern.search(password):
        return "Invalid Password. Must contain at least one lowercase letter"

    if not upper_case_pattern.search(password):
        return "Invalid Password. Must contain at least one uppercase letter"

    if not number_pattern.search(password):
        return "Invalid Password. Must contain at least one number"

    if not special_character_pattern.search(password):
        return "Invalid Password. Must contain at least one special character from [$#@]"

    return None  # Password is valid

# Create your views here.
def login_(request):

    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        U=authenticate(username=username_data, password=password_data)
        if U:
            login(request, U)
            return redirect('home')  # Redirect to a home page or dashboard after login
    return render(request, 'login.html')

def register_(request):

    if request.method == 'POST':
        first_name_data = request.POST['firstname']
        last_name_data = request.POST['lastname']
        email_data = request.POST['email']
        username_data = request.POST['username']
        password_data = request.POST['password']

        # Validate password
        password_error = validate_password(password_data)
        if password_error:
            return render(request, 'register.html', {
                'error': password_error,
                'firstname': first_name_data,
                'lastname': last_name_data,
                'email': email_data,
                'username': username_data
            })
        
        # Check if username already exists
        if User.objects.filter(username=username_data).exists():
            return render(request, 'register.html', {'error': f"The username '{username_data}' is already taken. Please choose a different one.", 'firstname': first_name_data, 'lastname': last_name_data, 'email': email_data, 'username': username_data})

        # Check if email already exists
        if User.objects.filter(email=email_data).exists():
            return render(request, 'register.html', {'error': f"The email '{email_data}' is already taken. Please choose a different one.", 'firstname': first_name_data, 'lastname': last_name_data, 'email': email_data, 'username': username_data})
        
        try:
            user = User.objects.create(
                first_name=first_name_data,
                last_name=last_name_data,
                email=email_data,
                username=username_data,
            )
            user.set_password(password_data)
            user.save()
            return redirect('login_')
        
        except IntegrityError:
            return render(request, 'register.html', {'error': 'An error occurred while registering. Please try again.', 'firstname': first_name_data, 'lastname': last_name_data, 'email': email_data, 'username': username_data})

    return render(request, 'register.html')

def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login_')
def update_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        # Check if username already exists (excluding current user)
        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            return render(request, 'update_profile.html', {'error': f"The username '{username}' is already taken. Please choose a different one.", 'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email})

        if User.objects.filter(email=email).exclude(id=request.user.id).exists():
            return render(request, 'update_profile.html', {'error': f"The email '{email}' is already taken. Please choose a different one.", 'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email})

        try:
            request.user.username = username
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.email = email
            request.user.save()
            return redirect('profile')
        except IntegrityError:
            return render(request, 'update_profile.html', {'error': 'An error occurred while updating your profile. Please try again.', 'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email})
    return render(request, 'update_profile.html')

@login_required(login_url='login_')
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        # Validate new password
        password_error = validate_password(new_password)
        if password_error:
            return render(request, 'change_password.html', {'error': password_error})

        if not request.user.check_password(old_password):
            return render(request, 'change_password.html', {'error': 'Old password is incorrect'})
        if new_password != confirm_password:
            return render(request, 'change_password.html', {'error': 'New passwords do not match'})
        request.user.set_password(new_password)
        request.user.save()
        return redirect('login_')  # Redirect to login after password change
    return render(request, 'change_password.html')
