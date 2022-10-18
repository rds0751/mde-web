from django.shortcuts import render
from accounts.models import User

# Create your views here.
def index(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/front-pagec.html',  {'user': user})


def add_member(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/add-member.html',  {'user': user})



def bp_and_sugar_control(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/bp-and-sugar-control.html',  {'user': user})



def contact_medose(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/contact-medose.html',  {'user': user})




def daily_dairy_icon(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/daily-dairy-icon.html',  {'user': user})



def find_your_specialist_doctors(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/find-your-specialist-doctors.html',  {'user': user})



def health_tips_icon(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/health-tips-icon.html',  {'user': user})



def hospital_reports(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/hospital-reports.html',  {'user': user})



def iphone_xr_xs_max_11_1(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/iphone-xr-xs-max-11-1.html',  {'user': user})



def lab_test(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/lab-test.html',  {'user': user})



def link_at_dairy_doctor(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/link-at-dairy-doctor.html',  {'user': user})



def login(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/login.html',  {'user': user})



def medicine_reminder(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/medicine-reminder.html',  {'user': user})



def medose_join_now_menu_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/medose-join-now-menu-page.html',  {'user': user})



def menu_icon_1(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/menu-icon-1.html',  {'user': user})



def my_activity_page_2(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-activity-page-2.html',  {'user': user})



def my_activity(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-activity.html',  {'user': user})



def my_cart(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-cart.html',  {'user': user})



def my_consulation(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-consulation.html',  {'user': user})



def my_device(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-device.html',  {'user': user})



def my_doctors_1(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-doctors-1.html',  {'user': user})



def my_doctors(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-doctors.html',  {'user': user})



def my_health(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-health.html',  {'user': user})



def my_orders(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-orders.html',  {'user': user})



def my_profile(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-profile.html',  {'user': user})



def my_record(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-record.html',  {'user': user})



def my_rewards(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-rewards.html',  {'user': user})



def notification(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/notification.html',  {'user': user})



def ocr_reader(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/ocr-reader.html',  {'user': user})



def plus_button_on_front_page_1(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/plus-button-on-front-page-1.html',  {'user': user})



def plus_button_on_front_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/plus-button-on-front-page.html',  {'user': user})



def prescription(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/prescription.html',  {'user': user})



def privacy_policy(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/privacy-policy.html',  {'user': user})



def record_notification(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/record-notification.html',  {'user': user})



def refer_and_earn(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/refer-and-earn.html',  {'user': user})



def settings(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/settings.html',  {'user': user})



def terms_and_conditions_menu(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/terms-and-conditions-menu.html',  {'user': user})



def terms_conditions_2(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/terms-conditions-2.html',  {'user': user})



def upload_new_prescriptions(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/upload-new-prescriptions.html',  {'user': user})



def using_guide_line_video(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/using-guide-line-video.html',  {'user': user})


def book_consultation(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/book-consultation.html',  {'user': user})


def past_consultation(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/past-consultation.html',  {'user': user})



def add_mydoctor(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/add-mydoctor.html',  {'user': user})


def lab_tests(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/lab-tests.html',  {'user': user})

def plusicon(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/plusicon.html',  {'user': user})

    
def ambulance_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/ambulance-page.html',  {'user': user})



def bloodbank_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/bloodbank-page.html',  {'user': user})


def mydevice_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/my-device-page.html',  {'user': user})


def health_welness_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/health-welness-page.html',  {'user': user})


def lab_test_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/lab-test-page.html',  {'user': user})


def medicine_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/medicine-page.html',  {'user': user})


def subscription_page(request):
    user = User.objects.get(useremail = request.session['useremail'])
    request.session['username'] = user.first_name + " "+ user.last_name
    return render(request, 'native/subscription-page.html',  {'user': user})









