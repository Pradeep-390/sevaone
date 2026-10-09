from django.urls import path

from .views import (
    blood_home,
    create_blood_request,
    blood_request_success,
    my_blood_requests,
    become_blood_volunteer,
    volunteer_success,
    volunteer_requests,
    accept_blood_request,
    complete_blood_request,
    edit_blood_volunteer,
    volunteer_profile_updated,
    volunteer_dashboard,
    cancel_blood_request,
)


urlpatterns = [

    # =====================================================
    # BLOOD HELP HOME
    # =====================================================

    path(
        '',
        blood_home,
        name='blood'
    ),


    # =====================================================
    # BLOOD REQUEST
    # =====================================================

    path(
        'request/',
        create_blood_request,
        name='create_blood_request'
    ),

    path(
        'request/success/',
        blood_request_success,
        name='blood_request_success'
    ),

    path(
        'my/',
        my_blood_requests,
        name='my_blood_requests'
    ),


    # =====================================================
    # BLOOD VOLUNTEER
    # =====================================================

    path(
        'volunteer/',
        become_blood_volunteer,
        name='become_blood_volunteer'
    ),

    path(
        'volunteer/success/',
        volunteer_success,
        name='volunteer_success'
    ),

    path(
        'volunteer/requests/',
        volunteer_requests,
        name='volunteer_requests'
    ),

    path(
        'volunteer/requests/<int:request_id>/accept/',
        accept_blood_request,
        name='accept_blood_request'
    ),

    path(
        'volunteer/profile/edit/',
        edit_blood_volunteer,
        name='edit_blood_volunteer'
    ),

    path(
        'volunteer/profile/updated/',
        volunteer_profile_updated,
        name='volunteer_profile_updated'
    ),

    path(
        'volunteer/dashboard/',
        volunteer_dashboard,
        name='volunteer_dashboard'
    ),


    # =====================================================
    # COMPLETE / CANCEL REQUEST
    # =====================================================

    path(
        'my/<int:request_id>/complete/',
        complete_blood_request,
        name='complete_blood_request'
    ),

    path(
        'my/<int:request_id>/cancel/',
        cancel_blood_request,
        name='cancel_blood_request'
    ),

]