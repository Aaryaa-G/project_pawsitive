from django.shortcuts import render, redirect
from .models import Donation, Adoption, Volunteer
from .form import DonationForm, AdoptionForm, VolunteerForm,PreAdoptionForm
from django.contrib import messages


def donate_form_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your donation!')
            return redirect('donate_form')
    else:
        form = DonationForm()
    return render(request, 'adoptions/donation_form.html', {'form': form})

def postadoption_form_view(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your adoption!')
            return redirect('adopt_form')
    else:
        form = AdoptionForm()
    return render(request, 'adoptions/adopt_form.html', {'form': form})

def volunteer_form_view(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for thinking to be a volunteer!See you soon....')
            return redirect('volunteer_form')
    else:
        form = VolunteerForm()
    return render(request, 'adoptions/volunteer_form.html', {'form': form})

def preadoption_form_view(request):
    if request.method == 'POST':
        form = PreAdoptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your pre-adoption form has been submitted.Our team will contact you as soon as possible!!")
            return redirect('preadoption_form')  
    else:
        form = PreAdoptionForm()
    return render(request, 'adoptions/PreAdoption_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def home_view(request):
    return render(request, 'adoptions/home.html')

def about_view(request):
    return render(request, 'adoptions/about-us.html')

def donate_view(request):
    return render(request, 'adoptions/donate.html')

def volunteer_view(request):
    return render(request, 'adoptions/volunteer.html')

def adopt_view(request):
    return render(request, 'adoptions/adopt.html')
