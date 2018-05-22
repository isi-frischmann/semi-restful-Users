from django.shortcuts import render, HttpResponse, redirect
from .models import User
# import the User class
from django.contrib import messages
# import the flash messages

# never render on a POST method 

def index(request):
    context = {
        'user': User.objects.all()
    }
    return render(request, 'first_app/index.html', context)

# HTML file for adding a User:
def new(request):
    return render(request, 'first_app/add_User.html')

# Creating a new User when the Create button is clicked
def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
        if len(errors):
            # iterate through error messages if there is
            for key, error in errors.items():
                # Don't forget the items after errors that's the function who is going through
                # if the errors object contains anything loop through each key-value pair and make a flash message
                messages.error(request, error)
            return redirect('/users/new')
        else:
            # if errors object is empty
            User.objects.create(fname = request.POST['fname'], email = request.POST['email'])
            messages.success(request, 'Added new user')
            return redirect('/')
    return redirect('/')

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    # check if the input has any error
    if len(errors):
        # if there is go through the error messages
        for key, error in errors.items():
            messages.error(request, error)
        return redirect('/users/edit/' + id)
        # if there are error messages add the / and the id to the redirect
    # if there are no errors:
    else:
        u = User.objects.get(id = id)
        u.fname = request.POST['fname']
        u.email = request.POST['email']
        u.save()
    return redirect('/')

# add a input after request in the edit method when you need to get informations
def edit(request, id):
    # crating a dictionary when you need to pull out informations
    context = {
        'user': User.objects.get(id = id)
    }
    return render(request, 'first_app/edit_User.html', context)

def show(request, id):
    print(id)
    context = {
        'user' : User.objects.get(id = id)
    }
    return render(request, 'first_app/show_user.html', context)
    # If you want to get something returned add it to return. Like here context.

def destroy(request, id):
    u = User.objects.get(id = id)
    u.delete()
    return redirect('/')


