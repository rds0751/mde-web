"""Epatient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views

app_name = 'native'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-member', views.add_member, name='add-member'),
    path('bp-and-sugar-control', views.bp_and_sugar_control, name='bp-and-sugar-control'),
    path('contact-medose', views.contact_medose, name='contact-medose'),
    path('daily-dairy-icon', views.daily_dairy_icon, name='daily-dairy-icon'),
    path('find-your-specialist-doctors', views.find_your_specialist_doctors, name='find-your-specialist-doctors'),
    path('health-tips-icon', views.health_tips_icon, name='health-tips-icon'),
    path('hospital-reports', views.hospital_reports, name='hospital-reports'),
    path('iphone-xr-xs-max-11-1', views.iphone_xr_xs_max_11_1, name='iphone-xr-xs-max-11-1'),
    path('lab-test', views.lab_test, name='lab-test'),
    path('link-at-dairy-doctor', views.link_at_dairy_doctor, name='link-at-dairy-doctor'),
    path('login', views.login, name='login'),
    path('medicine-reminder', views.medicine_reminder, name='medicine-reminder'),
    path('medose-join-now-menu-page', views.medose_join_now_menu_page, name='medose-join-now-menu-page'),
    path('menu-icon-1', views.menu_icon_1, name='menu-icon-1'),
    path('my-activity-page-2', views.my_activity_page_2, name='my-activity-page-2'),
    path('my-activity', views.my_activity, name='my-activity'),
    path('my-cart', views.my_cart, name='my-cart'),
    path('my-consulation', views.my_consulation, name='my-consulation'),
    path('my-device', views.my_device, name='my-device'),
    path('my-doctors-1', views.my_doctors_1, name='my-doctors-1'),
    path('my-doctors', views.my_doctors, name='my-doctors'),
    path('my-health', views.my_health, name='my-health'),
    path('my-orders', views.my_orders, name='my-orders'),
    path('my-profile', views.my_profile, name='my-profile'),
    path('my-record', views.my_record, name='my-record'),
    path('my-rewards', views.my_rewards, name='my-rewards'),
    path('notification', views.notification, name='notification'),
    path('ocr-reader', views.ocr_reader, name='ocr-reader'),
    path('plus-button-on-front-page-1', views.plus_button_on_front_page_1, name='plus-button-on-front-page-1'),
    path('plus-button-on-front-page', views.plus_button_on_front_page, name='plus-button-on-front-page'),
    path('prescription', views.prescription, name='prescription'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
    path('record-notification', views.record_notification, name='record-notification'),
    path('refer-and-earn', views.refer_and_earn, name='refer-and-earn'),
    path('settings', views.settings, name='settings'),
    path('terms-and-conditions-menu', views.terms_and_conditions_menu, name='terms-and-conditions-menu'),
    path('terms-conditions-2', views.terms_conditions_2, name='terms-conditions-2'),
    path('upload-new-prescriptions', views.upload_new_prescriptions, name='upload-new-prescriptions'),
    path('using-guide-line-video', views.using_guide_line_video, name='using-guide-line-video'),
    path('book-consultation', views.book_consultation, name='abcd'),
    path('past-consultation', views.past_consultation, name='xyz'),
    path('ambulance-page', views.ambulance_page, name='xyz'),
    path('bloodbank-page', views.bloodbank_page, name='777'),
    path('my-device-page', views.mydevice_page, name='777'),
    path('health-welness-page', views.health_welness_page, name='777'),
    path('lab-test-page', views.lab_test_page, name='777'),
    path('medicine-page', views.medicine_page, name='777'),
    path('subscription-page', views.subscription_page, name='777'),
     
]
