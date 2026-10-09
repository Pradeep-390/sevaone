from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ComplaintForm,ComplaintStatusForm,ComplaintVerificationForm,ResolutionForm,FeedbackForm

from .models import Complaint
@login_required
def complaints_home(request):
    return render(
        request,
        'complaints/complaints_home.html'
    )

@login_required
def create_complaint(request):

    if request.method == 'POST':

        form = ComplaintForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            complaint = form.save(commit=False)

            complaint.user = request.user

            complaint.save()

            return redirect('complaint_list')

    else:

        form = ComplaintForm()

    return render(
        request,
        'complaints/create_complaint.html',
        {
            'form': form
        }
    )


@login_required
def complaint_list(request):

    complaints = Complaint.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'complaints/complaint_list.html',
        {
            'complaints': complaints
        }
    )


@login_required
def complaint_detail(request, pk):

    complaint = get_object_or_404(
        Complaint,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        'complaints/complaint_detail.html',
        {
            'complaint': complaint
        }
    )


@login_required
def officer_dashboard(request):

    complaints = Complaint.objects.filter(
        assigned_officer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'complaints/officer_dashboard.html',
        {
            'complaints': complaints
        }
    )

@login_required
def update_complaint_status(request, pk):

    complaint = get_object_or_404(
        Complaint,
        pk=pk,
        assigned_officer=request.user
    )

    if request.method == 'POST':

        form = ComplaintStatusForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():

            form.save()

            return redirect(
                'officer_dashboard'
            )

    else:

        form = ComplaintStatusForm(
            instance=complaint
        )

    return render(
        request,
        'complaints/update_status.html',
        {
            'form': form,
            'complaint': complaint
        }
    )

@login_required
def verify_complaint(request, pk):

    complaint = get_object_or_404(
        Complaint,
        pk=pk
    )

    if request.method == 'POST':

        form = ComplaintVerificationForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():

            complaint = form.save(
                commit=False
            )

            if complaint.status == 'APPROVED':

                complaint.is_verified = True

                complaint.rejection_reason = ''

            elif complaint.status == 'REJECTED':

                complaint.is_verified = False

            complaint.save()

            return redirect(
                'admin_complaints'
            )

    else:

        form = ComplaintVerificationForm(
            instance=complaint
        )

    return render(
        request,
        'complaints/verify_complaint.html',
        {
            'form': form,
            'complaint': complaint
        }
    )
    
from django.utils import timezone 
@login_required
def resolve_complaint(request, pk):

    complaint = get_object_or_404(
        Complaint,
        pk=pk,
        assigned_officer=request.user
    )

    if request.method == 'POST':

        form = ResolutionForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():

            complaint = form.save(
                commit=False
            )

            if complaint.status == 'RESOLVED':

                complaint.resolved_at = timezone.now()

            complaint.save()

            return redirect(
                'officer_dashboard'
            )

    else:

        form = ResolutionForm(
            instance=complaint
        )

    return render(
        request,
        'complaints/resolve_complaint.html',
        {
            'form': form,
            'complaint': complaint
        }
    )  

@login_required
def complaint_feedback(request, pk):

    complaint = get_object_or_404(
        Complaint,
        pk=pk,
        user=request.user,
        status='RESOLVED'
    )

    if request.method == 'POST':

        form = FeedbackForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():

            form.save()

            return redirect(
                'complaint_detail',
                pk=complaint.pk
            )

    else:

        form = FeedbackForm(
            instance=complaint
        )

    return render(
        request,
        'complaints/feedback.html',
        {
            'form': form,
            'complaint': complaint
        }
    )         