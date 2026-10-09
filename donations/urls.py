from django.urls import path

from .views import (  donations_home,create_food_donation,
food_donation_success,my_food_donations,available_food_donations, accept_food_donation,
collect_food_donation,my_accepted_food,
complete_food_donation,create_item_donation,
my_item_donations,available_item_donations,
accept_item_donation, my_accepted_item_donations,
    collect_item_donation,complete_item_donation,)


urlpatterns = [

    path('',donations_home,name='donations_home'),

    path('food/create/',create_food_donation,name='create_food_donation'),
    path('food/success/',food_donation_success,name='food_donation_success'),
    path('food/my/',my_food_donations,name='my_food_donations'),
    path('food/available/',available_food_donations,name='available_food_donations'),
    path('food/<int:donation_id>/accept/',accept_food_donation,name='accept_food_donation'),
    path('food/<int:donation_id>/collect/',collect_food_donation,name='collect_food_donation'),
    path('food/accepted/',my_accepted_food,name='my_accepted_food'),
    path('food/<int:donation_id>/complete/',complete_food_donation,name='complete_food_donation' ),
    path('items/create/',create_item_donation,name='create_item_donation' ),
    path('items/my/',my_item_donations,name='my_item_donations'),
    path('items/available/',available_item_donations,name='available_item_donations'),
    path('items/<int:donation_id>/accept/',accept_item_donation, name='accept_item_donation'),
        path(
        'items/accepted/',
        my_accepted_item_donations,
        name='my_accepted_item_donations'
    ),

    path(
        'items/<int:donation_id>/collect/',
        collect_item_donation,
        name='collect_item_donation'
    ),

    path(
        'items/<int:donation_id>/complete/',
        complete_item_donation,
        name='complete_item_donation'
    ),


]