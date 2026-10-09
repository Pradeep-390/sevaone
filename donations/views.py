from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import FoodDonationForm, ItemDonationForm
from .models import FoodDonation, ItemDonation


# =========================================================
# DONATIONS HOME
# =========================================================

@login_required
def donations_home(request):

    return render(
        request,
        'donations/donations_home.html'
    )


# =========================================================
# FOOD DONATIONS
# =========================================================

@login_required
def create_food_donation(request):

    if request.method == 'POST':

        form = FoodDonationForm(request.POST)

        if form.is_valid():

            food_donation = form.save(commit=False)

            food_donation.donor = request.user
            food_donation.status = 'PENDING'

            food_donation.save()

            return redirect('food_donation_success')

    else:
        form = FoodDonationForm()

    return render(
        request,
        'donations/create_food_donation.html',
        {'form': form}
    )


@login_required
def food_donation_success(request):

    return render(
        request,
        'donations/food_donation_success.html'
    )


@login_required
def my_food_donations(request):

    donations = FoodDonation.objects.filter(
        donor=request.user
    ).order_by('-created_at')

    return render(
        request,
        'donations/my_food_donations.html',
        {'donations': donations}
    )


@login_required
def available_food_donations(request):

    donations = FoodDonation.objects.filter(
        status='PENDING'
    ).exclude(
        donor=request.user
    ).order_by('-created_at')

    return render(
        request,
        'donations/available_food_donations.html',
        {'donations': donations}
    )


@login_required
@require_POST
def accept_food_donation(request, donation_id):

    food_donation = get_object_or_404(
        FoodDonation,
        id=donation_id,
        status='PENDING'
    )

    if food_donation.donor == request.user:
        return redirect('available_food_donations')

    food_donation.accepted_by = request.user
    food_donation.status = 'ACCEPTED'

    food_donation.save()

    return redirect('available_food_donations')


@login_required
@require_POST
def collect_food_donation(request, donation_id):

    food_donation = get_object_or_404(
        FoodDonation,
        id=donation_id,
        accepted_by=request.user,
        status='ACCEPTED'
    )

    food_donation.status = 'COLLECTED'

    food_donation.save()

    return redirect('my_accepted_food')


@login_required
def my_accepted_food(request):

    donations = FoodDonation.objects.filter(
        accepted_by=request.user
    ).order_by('-updated_at')

    return render(
        request,
        'donations/my_accepted_food.html',
        {'donations': donations}
    )


@login_required
@require_POST
def complete_food_donation(request, donation_id):

    food_donation = get_object_or_404(
        FoodDonation,
        id=donation_id,
        donor=request.user,
        status='COLLECTED'
    )

    food_donation.status = 'COMPLETED'

    food_donation.save()

    return redirect('my_food_donations')


# =========================================================
# ITEM DONATIONS
# =========================================================

@login_required
def create_item_donation(request):

    if request.method == 'POST':

        form = ItemDonationForm(request.POST)

        if form.is_valid():

            item_donation = form.save(commit=False)

            item_donation.donor = request.user
            item_donation.status = 'PENDING'

            item_donation.save()

            return redirect('my_item_donations')

    else:
        form = ItemDonationForm()

    return render(
        request,
        'donations/create_item_donation.html',
        {'form': form}
    )


@login_required
def my_item_donations(request):

    donations = ItemDonation.objects.filter(
        donor=request.user
    ).order_by('-created_at')

    return render(
        request,
        'donations/my_item_donations.html',
        {'donations': donations}
    )


@login_required
def available_item_donations(request):

    donations = ItemDonation.objects.filter(
        status='PENDING'
    ).exclude(
        donor=request.user
    ).order_by('-created_at')

    return render(
        request,
        'donations/available_item_donations.html',
        {'donations': donations}
    )


@login_required
@require_POST
def accept_item_donation(request, donation_id):

    item_donation = get_object_or_404(
        ItemDonation,
        id=donation_id,
        status='PENDING'
    )

    if item_donation.donor == request.user:
        return redirect('available_item_donations')

    item_donation.accepted_by = request.user
    item_donation.status = 'ACCEPTED'

    item_donation.save()

    return redirect('available_item_donations')


@login_required
def my_accepted_item_donations(request):

    donations = ItemDonation.objects.filter(
        accepted_by=request.user
    ).order_by('-updated_at')

    return render(
        request,
        'donations/my_accepted_item_donations.html',
        {'donations': donations}
    )


@login_required
@require_POST
def collect_item_donation(request, donation_id):

    item_donation = get_object_or_404(
        ItemDonation,
        id=donation_id,
        accepted_by=request.user,
        status='ACCEPTED'
    )

    item_donation.status = 'COLLECTED'

    item_donation.save()

    return redirect('my_accepted_item_donations')


# =========================================================
# COMPLETE ITEM DONATION
# =========================================================

@login_required
@require_POST
def complete_item_donation(request, donation_id):

    item_donation = get_object_or_404(
        ItemDonation,
        id=donation_id,
        donor=request.user,
        status='COLLECTED'
    )

    item_donation.status = 'COMPLETED'

    item_donation.save()

    return redirect('my_item_donations')