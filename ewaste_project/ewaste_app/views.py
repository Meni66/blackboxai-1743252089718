from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm
from .models import Report

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def dashboard(request):
    user_reports = Report.objects.filter(user=request.user)
    stats = {
        'total_reports': user_reports.count(),
        'pending': user_reports.filter(status='PENDING').count(),
        'scheduled': user_reports.filter(status='SCHEDULED').count(),
        'collected': user_reports.filter(status='COLLECTED').count()
    }
    return render(request, 'dashboard/index.html', {'stats': stats})

@login_required
def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.status = 'PENDING'
            report.save()
            messages.success(request, 'Report submitted successfully!')
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'reports/create.html', {'form': form})

@login_required
def report_list(request):
    reports = Report.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'reports/list.html', {'reports': reports})
