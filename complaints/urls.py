from django.urls import path

from .views import (
    complaints_home,
    create_complaint,
    complaint_list,
    complaint_detail,
    officer_dashboard,
    update_complaint_status,
    verify_complaint,
    resolve_complaint,
    complaint_feedback,
)


urlpatterns = [

    path(
        '',
        complaints_home,
        name='complaints_home'
    ),

    path(
        'create/',
        create_complaint,
        name='create_complaint'
    ),

    path(
        'my/',
        complaint_list,
        name='complaint_list'
    ),

    path(
        '<int:pk>/',
        complaint_detail,
        name='complaint_detail'
    ),

    path(
        'officer/',
        officer_dashboard,
        name='officer_dashboard'
    ),

    path(
        'officer/<int:pk>/status/',
        update_complaint_status,
        name='update_complaint_status'
    ),

    path(
        'verify/<int:pk>/',
        verify_complaint,
        name='verify_complaint'
    ),

    path(
        'officer/<int:pk>/resolve/',
        resolve_complaint,
        name='resolve_complaint'
    ),

    path(
        '<int:pk>/feedback/',
        complaint_feedback,
        name='complaint_feedback'
    ),

]