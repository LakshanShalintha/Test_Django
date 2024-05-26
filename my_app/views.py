from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def members(request, template):
    members_list = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown']
    context = {
        'members': members_list,
    }
    template = loader.get_template('my_app/login.html')
    return HttpResponse(template.render(context, request))


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']  # Adjusted to 'username' to match the HTML input name
        email = request.POST['email']
        phone_number = request.POST.get('phone_number', '')  # New field from Flutter (optional)
        password = request.POST['password']
        remember_me = 'rememberMe' in request.POST

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "User with this username already exists.")
            return render(request, 'my_app/signup.html', status=400)
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return render(request, 'my_app/signup.html', status=400)

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Additional user fields like phone_number should be saved in a profile model if needed
        # Example:
        # profile = UserProfile(user=user, phone_number=phone_number)
        # profile.save()

        # Log the user in if remember_me is checked
        if remember_me:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)

        # Handle post-signup actions (e.g., send a verification email)
        return redirect('verify_email')  # Redirect to verification page after successful signup

    return render(request, 'my_app/signup.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = 'rememberMe' in request.POST

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'my_app/login.html', status=400)

    return render(request, 'my_app/login.html')


def verify_email(request):
    return HttpResponse("Verify your email.")


def home(request):
    return HttpResponse("Home page.")  # Placeholder for the home page
