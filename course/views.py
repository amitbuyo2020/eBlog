from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def eNepal(request):
    context = {
        'title': "eNepal",
    }
    return render(request, 'course/eNepal.html', context)

@login_required(login_url='login')
def home(request):
    context = {
        'title': "Home",
    }
    return render(request, 'course/home.html', context)

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'course/about.html', context)



def lowerSecondary(request):
    return render(request, 'course/lower_secondary.html', {'title': "Lower Secondary"})

# Secondary Section

def secondary(request):
    context = {
        'title': "Secondary",
    }
    return render(request, 'course/secondary.html', context)

def secScience(request):
    return render(request, 'course/sec_science.html', {'title':"Science"})

def secMath(request):
    return render(request, 'course/sec_math.html', {'title':"Math"})

def secComputer(request):
    return render(request, 'course/sec_cs.html', {'title':"Computer Science"})

# Primary Section
def primary(request):
    return render(request, 'course/primary.html', {'title': 'Primary'})


def priScience(request):
    return render(request, 'course/pri_science.html', {'title':"Science"})


def contact(request):
    return render(request, 'course/contact.html', {'title': "Contact"})
