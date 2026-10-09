from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from django.views.decorators.http import require_POST

from .forms import BloodRequestForm, BloodVolunteerForm
from .models import BloodRequest, BloodVolunteer


# =====================================================
# BLOOD HELP HOME
# =====================================================

def blood_home(request):

    return render(
        request,
        'blood.html'
    )


# =====================================================
# CREATE BLOOD REQUEST
# =====================================================

@login_required
def create_blood_request(request):

    if request.method == 'POST':

        form = BloodRequestForm(request.POST)

        if form.is_valid():

            blood_request = form.save(commit=False)

            blood_request.requester = request.user

            blood_request.save()

            return redirect('blood_request_success')

    else:

        form = BloodRequestForm()

    return render(
        request,
        'blood/create_blood_request.html',
        {
            'form': form
        }
    )


# =====================================================
# BLOOD REQUEST SUCCESS
# =====================================================

@login_required
def blood_request_success(request):

    return render(
        request,
        'blood/blood_request_success.html'
    )


# =====================================================
# MY BLOOD REQUESTS
# =====================================================

@login_required
def my_blood_requests(request):

    blood_requests = BloodRequest.objects.filter(
        requester=request.user
    ).order_by('-created_at')

    return render(
        request,
        'blood/my_blood_requests.html',
        {
            'blood_requests': blood_requests
        }
    )


# =====================================================
# BECOME BLOOD VOLUNTEER
# =====================================================

@login_required
def become_blood_volunteer(request):

    # Check whether the user is already a volunteer

    existing_volunteer = BloodVolunteer.objects.filter(
        user=request.user
    ).first()

    # If already registered, show existing profile

    if existing_volunteer:

        return render(
            request,
            'blood/volunteer_already_registered.html',
            {
                'volunteer': existing_volunteer
            }
        )

    # New volunteer registration

    if request.method == 'POST':

        form = BloodVolunteerForm(request.POST)

        if form.is_valid():

            volunteer = form.save(commit=False)

            volunteer.user = request.user

            volunteer.save()

            return redirect('volunteer_success')

    else:

        form = BloodVolunteerForm()

    return render(
        request,
        'blood/become_volunteer.html',
        {
            'form': form
        }
    )


# =====================================================
# EDIT BLOOD VOLUNTEER
# =====================================================

@login_required
def edit_blood_volunteer(request):

    volunteer = get_object_or_404(
        BloodVolunteer,
        user=request.user
    )

    if request.method == 'POST':

        form = BloodVolunteerForm(
            request.POST,
            instance=volunteer
        )

        if form.is_valid():

            form.save()

            return redirect('volunteer_profile_updated')

    else:

        form = BloodVolunteerForm(
            instance=volunteer
        )

    return render(
        request,
        'blood/edit_volunteer.html',
        {
            'form': form,
            'volunteer': volunteer
        }
    )


# =====================================================
# VOLUNTEER PROFILE UPDATED
# =====================================================

@login_required
def volunteer_profile_updated(request):

    return render(
        request,
        'blood/volunteer_profile_updated.html'
    )


# =====================================================
# VOLUNTEER DASHBOARD
# =====================================================

@login_required
def volunteer_dashboard(request):

    volunteer = get_object_or_404(
        BloodVolunteer,
        user=request.user
    )

    pending_count = BloodRequest.objects.filter(
        blood_group=volunteer.blood_group,
        status='PENDING'
    ).count()

    accepted_count = BloodRequest.objects.filter(
        accepted_by=volunteer,
        status='ACCEPTED'
    ).count()

    completed_count = BloodRequest.objects.filter(
        accepted_by=volunteer,
        status='COMPLETED'
    ).count()

    return render(
        request,
        'blood/volunteer_dashboard.html',
        {
            'volunteer': volunteer,
            'pending_count': pending_count,
            'accepted_count': accepted_count,
            'completed_count': completed_count,
        }
    )


# =====================================================
# VOLUNTEER SUCCESS
# =====================================================

@login_required
def volunteer_success(request):

    return render(
        request,
        'blood/volunteer_success.html'
    )


# =====================================================
# VOLUNTEER REQUESTS
# =====================================================

@login_required
def volunteer_requests(request):

    volunteer = get_object_or_404(
        BloodVolunteer,
        user=request.user
    )

    # Get urgency filter from URL

    selected_urgency = request.GET.get(
        'urgency',
        'ALL'
    )

    # Base queryset

    blood_requests = BloodRequest.objects.filter(
        blood_group=volunteer.blood_group
    ).filter(

        models.Q(
            status='PENDING'
        )

        |

        models.Q(
            status='ACCEPTED',
            accepted_by=volunteer
        )

        |

        models.Q(
            status='COMPLETED',
            accepted_by=volunteer
        )

    )

    # Apply urgency filter

    if selected_urgency in [
        'EMERGENCY',
        'URGENT',
        'NORMAL'
    ]:

        blood_requests = blood_requests.filter(
            urgency=selected_urgency
        )

    # Emergency → Urgent → Normal
    # Newest first within each urgency

    blood_requests = blood_requests.order_by(

        models.Case(

            models.When(
                urgency='EMERGENCY',
                then=0
            ),

            models.When(
                urgency='URGENT',
                then=1
            ),

            models.When(
                urgency='NORMAL',
                then=2
            ),

            default=3,

            output_field=models.IntegerField()
        ),

        '-created_at'
    )

    return render(
        request,
        'blood/volunteer_requests.html',
        {
            'volunteer': volunteer,
            'blood_requests': blood_requests,
            'selected_urgency': selected_urgency,
        }
    )


# =====================================================
# ACCEPT BLOOD REQUEST
# =====================================================

@login_required
def accept_blood_request(request, request_id):

    volunteer = get_object_or_404(
        BloodVolunteer,
        user=request.user
    )

    # Volunteer must be available

    if not volunteer.is_available:

        return render(
            request,
            'blood/volunteer_unavailable.html',
            {
                'volunteer': volunteer
            }
        )

    # Request must still be pending

    blood_request = get_object_or_404(
        BloodRequest,
        id=request_id,
        status='PENDING'
    )

    # Blood group must match

    if blood_request.blood_group != volunteer.blood_group:

        return render(
            request,
            'blood/blood_group_mismatch.html',
            {
                'volunteer': volunteer,
                'blood_request': blood_request
            }
        )

    # Accept request

    blood_request.accepted_by = volunteer

    blood_request.status = 'ACCEPTED'

    blood_request.save()

    return redirect(
        'volunteer_requests'
    )


# =====================================================
# COMPLETE BLOOD REQUEST
# =====================================================

@login_required
def complete_blood_request(request, request_id):

    blood_request = get_object_or_404(
        BloodRequest,
        id=request_id,
        requester=request.user,
        status='ACCEPTED'
    )

    blood_request.status = 'COMPLETED'

    blood_request.save()

    return redirect(
        'my_blood_requests'
    )


# =====================================================
# CANCEL BLOOD REQUEST
# =====================================================

@login_required
@require_POST
def cancel_blood_request(request, request_id):

    blood_request = get_object_or_404(
        BloodRequest,
        id=request_id,
        requester=request.user,
        status='PENDING'
    )

    blood_request.status = 'CANCELLED'

    blood_request.save()

    return redirect(
        'my_blood_requests'
    )