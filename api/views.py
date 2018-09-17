# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from json import JSONEncoder

from django.views.decorators.csrf import csrf_exempt
from api.models import Users_Db_Renote, Users_Tokens_Db_Renote, Note_Db_Renote, Likes_DB, Follow_DB
from django.db.models import Q

from datetime import datetime
import datetime as dt
from api.utils import *
from api.validations import *
from renote.default_vals import *
from khayyam import *

import base64
# import cStringIO
from django.shortcuts import render

import time
import operator



from user_agents import parse



# Create your views here.

#===========================================================================
#========================== user_signup_handler ============================
#===========================================================================
@csrf_exempt
def user_signup_handler(request):


    request_user = {}
    # this_token = generate_token(mobile_no, '')
    this_date = datetime.now()
    verified_flag = 0
    introducer_flag = 0


    if (request.method == "POST"):
        mobile_no,username,user_pass,introduction_code,error_codes,success_flag = validate_user_signup(request)
        if success_flag:

            try:
                # کاربر پیش از این تلاش برای ثبت نام کرده است یا نه
                usr = Users_Db_Renote.objects.filter(username = username).get()
                #کاربر خود را تایید کرده است یا نه
                if usr.isverified:
                    request_user['status'] = 'error'
                    request_user['message'] = 'کاربری با این شماره موجود است'
                    request_user['error_codes'] = USER_EXIST_ERR
                    status = 400
                    return JsonResponse(request_user , status=status)
                else:

                    # بررسی برای اینکه ببنیم کد معرف وجود دارد و اینکه این کد برای یک کاربر هست یا نه
                    if introduction_code:
                        try:
                            Users_Db_Renote.objects.filter(who_introduction_code = introduction_code).get()
                            introducer_flag = 1
                        except:
                            introducer_flag = 0


                    if introduction_code and not introducer_flag:

                        request_user['status'] = 'error'
                        request_user['message'] = "کدمعرف اشتباه است"
                        status = 400
                        return JsonResponse(request_user , status=status)
                    else:
                        #چون کاربر تایید نشده بوده است و ممکن است جعلی بوده باشد گذرواژه دوباره ذخیره می‌شود
                        usr.user_pass = make_hashed_pw(str(mobile_no),str(user_pass))
                        usr.who_introduction_code = introduction_code
                        usr.save()

            except:

            # بررسی برای اینکه ببنیم کد معرف وجود دارد و اینکه این کد برای یک کاربر هست یا نه
            # --------------------------------------------------------------------------------
                if introduction_code:
                    try:
                        Users_Db_Renote.objects.filter(who_introduction_code = introduction_code).get()
                        introducer_flag = 1
                    except:
                        introducer_flag = 0


                if introduction_code and not introducer_flag:

                    request_user['status'] = 'error'
                    request_user['message'] = "کدمعرف اشتباه است"
                    status = 400
                    return JsonResponse(request_user , status=status)

                else:


                    Users_Db_Renote.objects.create(
                            user_id = mobile_no,
                            username = username,
                            user_pass = make_hashed_pw(str(mobile_no),str(user_pass)),
                            who_introduction_code = introduction_code,
                            isverified = 0,
                            status = 'not_valid',
                            introduction_code = generate_tracking_code(7)
                    )
                    usr = Users_Db_Renote.objects.filter(username = username).get()
            # --------------------------------------------------------------------------------


            #TODO usr
            if usr.confirm_sms_time_stamp:
                sms_delay = (datetime.now() - usr.confirm_sms_time_stamp.replace(tzinfo=None)).total_seconds()
            else:
                sms_delay = 10000

            if sms_delay < GAP_BETWEEN_SMS:
                # error_codes.append(handle_errors('Just_Sent_SMS','Just_Sent_SMS','error'))
                error_codes.append('1')
                success_flag = 0

                request_user['status'] = 'error'
                request_user['message'] = "پیامک پیش از این ارسال شده، لطفا شکیبا باشید. \n چنانچه پیامی دریافت نکردید 30 ثانیه دیگر ارسال مجدد را انتخاب نمایید."
                request_user['error_codes'] = SMS_EXIST_ERR
                status = 400
                return JsonResponse(request_user , status=status)

            else:
                try_itr = 0
                sms_sent = ''
                conf_code = generate_tracking_code(SMS_CODE_LENGTH)
                # while (try_itr < 2) and (not sms_sent):

                    #msg = notification_messages_dict['Registeration_SMS']
                    #msg = msg.decode('utf-8')
                    #msg = msg.replace('ConfCode',(conf_code).encode('utf-8'))
                    #TODO @#!@#!@#!@#$@#$@#$
                    # msg = notification_messages['Registeration_SMS'].decode('utf-8')
                    # tokens = [conf_code]

                    # try:
                    #     #sms_sent = send_sms_kaveh(usr.mobile_no,msg)
                    #     #async_result_sms =  pool.apply_async(send_sms_kaveh,[usr.mobile_no,msg])
                    #     # async_result_sms =  pool.apply_async(send_sms_kaveh_etebar_sanji,[usr.mobile_no,msg,'UbaarSigninSMS','sms',tokens])
                    #     task_send_sms_kaveh_etebar_sanji.apply_async([usr.mobile_no, msg,'carmano','sms', tokens],queue='hipri')
                    #
                    #     sms_sent = 1
                    #     if not sms_sent:
                    #         sms_sent = ''
                    #         err_dict = {}
                    #         err_dict['error_code'] = error_codes_dict['Registeration_SMS_Error']
                    #         err_dict['error_msg'] = error_codes_messages['Registeration_SMS_Error']
                    #         error_codes.append(err_dict)
                    #         success_flag = -2
                    # except:
                    #     sms_sent = ''
                    #     err_dict = {}
                    #     err_dict['error_code'] = error_codes_dict['Registeration_SMS_Error']
                    #     err_dict['error_msg'] = error_codes_messages['Registeration_SMS_Error']
                    #     error_codes.append(err_dict)
                    #     success_flag = -1

                    # if sms_sent:
                    #     usr.confirm_sms_val = conf_code
                    #     usr.confirm_sms_time_stamp = datetime.now()
                    #     usr.save()
                    # else:
                    #     try_itr = try_itr + 1

                usr.confirm_sms_val = conf_code
                usr.confirm_sms_time_stamp = datetime.now()
                usr.save()

                return JsonResponse({
                    'status': 'ok',
                    'verifi_code' : conf_code ,
                }, encoder=JSONEncoder)


        else:
            request_user['status'] = 'error'
            request_user['error_codes'] = error_codes
            status = 400
            return JsonResponse(request_user , status=status)





    else:
        request_user['status'] = 'error'
        request_user['error_codes'] = error_codes
        status = 400
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================





#===========================================================================
#========================== user_login_handler =============================
#===========================================================================
@csrf_exempt
def sms_verification_handler(request):

    if (request.method == "POST"):

        status = 0
        request_user = {}
        this_date = datetime.now()

        this_username,this_user_code,error_codes,success_flag = validate_sms_verifi(request)

        if success_flag:
            try:
                this_user = Users_Db_Renote.objects.get(username = this_username)

                if not this_user.isverified:

                    #TODO code check
                    if this_user.confirm_sms_val == this_user_code:
                    # if True:
                        this_user.isverified = 1
                        this_user.save()
                        request_user['status'] = 'ok'
                        status = 200
                    else:
                        request_user['status'] = 'error'
                        request_user['message'] = 'کد وارد شده اشتباه است'
                        request_user['error_codes'] = '101'
                        status = 400

                else:
                    request_user['status'] = 'کاربر تایید شده است'
                    request_user['error_codes'] = USER_EXIST_ERR
                    status = 400

            except:
                request_user['status'] = 'error'
                request_user['error_codes'] = USER_NOT_EXIST_ERR
                status = 400
        else:
            request_user['status'] = 'error'
            request_user['error_codes'] = error_codes
            status = 400
            return JsonResponse(request_user , status=status)

        return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)
#===========================================================================
#===========================================================================








#===========================================================================
#========================== user_login_handler =============================
#===========================================================================
@csrf_exempt
def user_login_handler(request):


    if (request.method == "POST"):

        status = 100
        request_user = {}
        this_date = datetime.now()

        this_username,this_user_pass,error_codes,success_flag = validate_user_login(request)

        if success_flag:

            try:
                this_user = Users_Db_Renote.objects.get(username = this_username)
                pass_check_flag = valid_hash_pw(this_user.user_id, this_user_pass, this_user.user_pass)
                # print(pass_check_flag)

                if pass_check_flag:

                    # if this_user.isverified:
                    if True:
                        token = generate_token(this_user.user_id,'')
                        Users_Tokens_Db_Renote.objects.create(
                                user = this_user,
                                assigned_token = token,
                                assigned_token_stamps = datetime.now(),
                                device = parse(request.META['HTTP_USER_AGENT']),
                        )

                        this_user.devices_last_login_times = parse(request.META['HTTP_USER_AGENT'])
                        this_user.save()

                        request_user['status'] = 'ok'
                        request_user['token'] = token
                        status = 200
                        return JsonResponse(request_user , status=status)
                    else:
                        request_user['message'] = 'این کاربر تایید نشده است'
                        request_user['status'] = 'error'
                        request_user['error_codes'] = USER_NOT_REGISTERED_ERR
                        status = 403
                        return JsonResponse(request_user , status=status)
                else:
                    request_user['message'] = 'نام کاربری یا گذرواژه نادرست است.'
                    request_user['status'] = 'error'
                    status = 403
                    return JsonResponse(request_user , status=status)

            except:
                request_user['status'] = 'error'
                request_user['message'] = 'نام کاربری یا گذرواژه نادرست است.'
                # request_user['error_codes'] = USER_NOT_EXIST_ERR
                status = 400
                return JsonResponse(request_user , status=status)

        else:
            request_user['status'] = 'error'
            request_user['error_codes'] = error_codes
            status = 400
            return JsonResponse(request_user , status=status)



    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)
#===========================================================================
#===========================================================================




#TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

#===========================================================================
#========================= user_analysis_handler ===========================
#===========================================================================
@csrf_exempt
def user_profile_handler(request):

    request_user = {}
    posts_history = []

    if (request.method == "POST"):

        this_token = request.META.get('HTTP_USERTOKEN')

        # c_profit = 0
        # c_count = 0

        # JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate()
        # JalaliDate(1397, 1, 1).todate()
        # (JalaliDatetime(datetime.now()).weekdaynameascii()).encode('utf-8')

        start_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().year,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().month,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().day)



        user_login, this_user = user_login_check(request)

        if user_login:

            users_follower = Follow_DB.objects.filter(follower=this_user , accepted = 1).values_list('followee', flat=True)
            users_followee = Follow_DB.objects.filter(followee=this_user , accepted = 1).values_list('follower', flat=True)

            this_user_posts =  Note_Db_Renote.objects.filter(user=this_user).order_by('-date')

            if this_user_posts :
                for post in this_user_posts:

                    number_of_likes =  Likes_DB.objects.filter(post = post).count()

                    try:
                        Likes_DB.objects.filter(user = this_user, post = post).get()
                        is_like = 1
                    except:
                        is_like = 0

                    post_user = post.user
                    post_details = {}

                    post_details["tracking_code"] = post.tracking_code
                    post_details["note"] = post.note
                    post_details["user_name"] = post_user.username
                    post_details["date"] = str(JalaliDatetime(post.date)).split(" ")[0]
                    post_details['post_photo'] = post.photo.name
                    post_details['likes'] = number_of_likes
                    post_details['is_like'] = is_like

                    posts_history.append(post_details)

            posts_history = sorted(posts_history, key=lambda x: x['date'], reverse=True)


            request_user['status'] = 'ok'
            request_user["note_list"] = posts_history
            request_user['user_data'] = {

                    'user_name': this_user.username,
                    'posts': len(posts_history),
                    'followers': len(users_followee),
                    'following': len(users_follower),
                    # 'status' : this_user.status,
                }

            status = 200
            return JsonResponse(request_user , status=status)
        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================





#===========================================================================
#=========================== submit_tr_handler =============================
#===========================================================================
@csrf_exempt
def submit_post_handler(request):

    request_user = {}
    isincome_method = 0

    if (request.method == "POST"):

        code_length = 15

        this_token = request.META.get('HTTP_USERTOKEN')
        this_tracking_code = generate_tracking_code(code_length)
        this_note,this_photo,this_group,error_codes,success_flag = validate_submit_tr(request)

        user_login, this_user = user_login_check(request)
        print(user_login)
        if user_login:


            this_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().year,\
                JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().month,\
                JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().day)


            if success_flag:

                Note_Db_Renote.objects.create(
                        tracking_code = this_tracking_code,
                        user = this_user,
                        note = this_note,
                        photo = this_photo,
                        group = this_group,
                        hashtag = "",
                        weekday_name = (JalaliDatetime(this_date).weekdaynameascii()).encode('utf-8'),
                        celery_task_id = '',
                        )

                return JsonResponse({
                        'status': 'ok',
                    }, encoder=JSONEncoder)
            else:
                request_user['status'] = 'error'
                request_user['error_codes'] = error_codes
                status = 400
                return JsonResponse(request_user , status=status)

        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر پیدا نشد'
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================












#=================================================================================================================================================
#================================================================  analysis  =====================================================================
#=================================================================================================================================================



#===========================================================================
#========================= user_tr_list_handler ===========================
#===========================================================================
@csrf_exempt
def user_posts_list_handler(request):

    request_user = {}
    posts_history = []
    users_fl = []


    if (request.method == "POST"):

        this_token = request.META.get('HTTP_USERTOKEN')

        # c_profit = 0
        # c_count = 0

        # JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate()
        # JalaliDate(1397, 1, 1).todate()
        # (JalaliDatetime(datetime.now()).weekdaynameascii()).encode('utf-8')

        start_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().year,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().month,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().day)

        user_login, this_user = user_login_check(request)

        if user_login:

            try:

                try:
                    users = Follow_DB.objects.filter(follower=this_user , accepted = 1).values_list('followee', flat=True)

                    for user in users:
                        users_fl.append(user)
                    if not users_fl:
                        users_fl = [this_user]
                    else:
                        users_fl.append(this_user)


                except:
                    users_fl = [this_user]

                # print(users_fl)
                # users_fl = Follow_DB.objects.filter(follower=this_user , accepted = 1)
                this_user_posts =  Note_Db_Renote.objects.filter(user__in=users_fl).order_by('-date')

                # this_user_posts = Note_Db_Renote.objects.filter().order_by('-date')
            except:
                this_user_posts = []

            if this_user_posts :
                for post in this_user_posts:

                    number_of_likes =  Likes_DB.objects.filter(post = post).count()

                    try:
                        Likes_DB.objects.filter(user = this_user, post = post).get()
                        is_like = 1
                    except:
                        is_like = 0

                    post_user = post.user
                    post_details = {}

                    post_details["tracking_code"] = post.tracking_code
                    post_details["note"] = post.note
                    post_details["user_name"] = post_user.username
                    post_details["date"] = str(JalaliDatetime(post.date)).split(" ")[0]
                    post_details['post_photo'] = post.photo.name
                    post_details['likes'] = number_of_likes
                    post_details['is_like'] = is_like

                    posts_history.append(post_details)
            posts_history = sorted(posts_history, key=lambda x: x['date'], reverse=True)



            request_user['status'] = 'ok'
            request_user["note_list"] = posts_history

            status = 200
            return JsonResponse(request_user , status=status)
        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================






#===========================================================================
#========================= user_tr_list_handler ===========================
#===========================================================================
@csrf_exempt
def like_post_handler(request):

    request_user = {}
    notes_history = []


    if (request.method == "POST"):

        this_token = request.META.get('HTTP_USERTOKEN')

        this_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().year,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().month,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().day)

        user_login, this_user = user_login_check(request)

        this_tracking_code,this_type,error_codes,success_flag = validate_post_like(request)

        if user_login:
            if success_flag:

                if this_type == "like":
                    try:
                        this_user_post = Note_Db_Renote.objects.get(tracking_code = this_tracking_code)
                        try:
                            is_like = Likes_DB.objects.filter(user = this_user, post = this_user_post).get()
                        except:
                            is_like = 0


                        if not is_like:
                            Likes_DB.objects.create(
                                    user = this_user,
                                    post = this_user_post,
                                    celery_task_id = '',
                                    )

                            return JsonResponse({
                                    'status': 'ok',
                                }, encoder=JSONEncoder)
                        else:
                            request_user['status'] = 'error'
                            request_user['message'] = 'از پیش پسندیده شده است'
                            status = 400
                            return JsonResponse(request_user , status=status)
                    except:
                        request_user['status'] = 'error'
                        request_user['message'] = 'ناتوانی در انجام عملیات'
                        status = 400
                        return JsonResponse(request_user , status=status)

                elif this_type == "dislike":

                    try:
                        this_user_post = Note_Db_Renote.objects.get(tracking_code = this_tracking_code)
                        Likes_DB.objects.filter(user = this_user, post = this_user_post).get().delete()

                        return JsonResponse({
                                'status': 'ok',
                            }, encoder=JSONEncoder)
                    except:
                        request_user['status'] = 'error'
                        request_user['message'] = 'ناتوانی در انجام عملیات'
                        status = 400
                        return JsonResponse(request_user , status=status)
            else:
                request_user['status'] = 'error'
                request_user['error_codes'] = error_codes
                status = 400
                return JsonResponse(request_user , status=status)

        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================





#===========================================================================
#========================= user_tr_list_handler ===========================
#===========================================================================
@csrf_exempt
def post_details_handler(request):

    request_user = {}
    post_details = {}


    if (request.method == "POST"):

        this_token = request.META.get('HTTP_USERTOKEN')

        # c_profit = 0
        # c_count = 0

        # JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate()
        # JalaliDate(1397, 1, 1).todate()
        # (JalaliDatetime(datetime.now()).weekdaynameascii()).encode('utf-8')

        start_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().year,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().month,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().day)

        user_login, this_user = user_login_check(request)

        this_tracking_code,error_codes,success_flag = validate_post_code(request)

        if user_login:
            if success_flag:

                try:
                    # users_fl = Follow_DB.objects.filter(follower=this_user , accepted = 1).values_list('station_id', flat=True)
                    # users_fl = Follow_DB.objects.filter(follower=this_user , accepted = 1)
                    this_user_post =  Note_Db_Renote.objects.filter(tracking_code=this_tracking_code).get()

                    if this_user_post.user.private and this_user_post.user != this_user:
                        Follow_DB.objects.filter(follower=this_user , followee=this_user_post.user , accepted = 1).get()

                except:
                    this_user_post = []

                if this_user_post:
                    # if this_user_post.user.private:

                    number_of_likes =  Likes_DB.objects.filter(post = this_user_post).count()

                    try:
                        Likes_DB.objects.filter(user = this_user, post = this_user_post).get()
                        is_like = 1
                    except:
                        is_like = 0

                    post_user = this_user_post.user

                    post_details["tracking_code"] = this_user_post.tracking_code
                    post_details["note"] = this_user_post.note
                    post_details["user_name"] = post_user.username
                    post_details["date"] = str(JalaliDatetime(this_user_post.date)).split(" ")[0]
                    post_details['post_photo'] = this_user_post.photo.name
                    post_details['likes'] = number_of_likes
                    post_details['is_like'] = is_like


                    request_user['status'] = 'ok'
                    request_user["post_details"] = post_details

                    status = 200
                    return JsonResponse(request_user , status=status)


                    # else:
                    #     request_user['status'] = 'error'
                    #     request_user['message'] = 'این پست در دسترس نمی باشد '
                    #     request_user['error_codes'] = POST_NOT_EXIST_ERR
                    #     status = 400
                    #     return JsonResponse(request_user , status=status)
                else:
                    request_user['status'] = 'error'
                    request_user['message'] = 'این پست در دسترس نمی باشد '
                    request_user['error_codes'] = POST_NOT_EXIST_ERR
                    status = 400
                    return JsonResponse(request_user , status=status)


            else:
                request_user['status'] = 'error'
                request_user['error_codes'] = error_codes
                status = 400
                return JsonResponse(request_user , status=status)
        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================









#===========================================================================
#========================= user_tr_list_handler ===========================
#===========================================================================
@csrf_exempt
def following_handler(request):

    request_user = {}
    notes_history = []


    if (request.method == "POST"):

        this_token = request.META.get('HTTP_USERTOKEN')

        this_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().year,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().month,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, JalaliDatetime(datetime.now()).day).todate().day)

        user_login, this_user = user_login_check(request)

        this_username,this_type,error_codes,success_flag = validate_user_follow(request)

        if user_login:

            if this_type == "follow":
                try:
                    this_followee = Users_Db_Renote.objects.get(username = this_username)

                    if this_followee != this_user:
                        try:
                            is_follow = Follow_DB.objects.filter(follower = this_user, followee = this_followee).get()
                        except:
                            is_follow = 0


                        if not is_follow:
                            Follow_DB.objects.create(
                                    follower = this_user,
                                    followee = this_followee,
                                    celery_task_id = '',
                                    )

                            return JsonResponse({
                                    'status': 'ok',
                                }, encoder=JSONEncoder)
                        else:
                            request_user['status'] = 'error'
                            request_user['message'] = 'از پیش دنبال می‌شود'
                            status = 400
                            return JsonResponse(request_user , status=status)
                    else:
                        request_user['status'] = 'error'
                        request_user['message'] = 'شما نمیتوانید خود را دنبال کنید'
                        status = 400
                        return JsonResponse(request_user , status=status)
                except:
                    request_user['status'] = 'error'
                    request_user['message'] = 'همچین کاربری برای دنبال کردن وجود ندارد'
                    status = 400
                    return JsonResponse(request_user , status=status)

            elif this_type == "unfollow":

                try:
                    this_followee = Users_Db_Renote.objects.get(username = this_username)
                    Follow_DB.objects.filter(follower = this_user, followee = this_followee).get().delete()

                    return JsonResponse({
                            'status': 'ok',
                        }, encoder=JSONEncoder)
                except:
                    request_user['status'] = 'error'
                    request_user['message'] = 'ناتوانی در انجام عملیات'
                    status = 400
                    return JsonResponse(request_user , status=status)

        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================








#===========================================================================
#========================= user_tr_list_handler ===========================
#===========================================================================
@csrf_exempt
def explore_posts_list_handler(request):

    request_user = {}
    posts_history = []


    if (request.method == "POST"):

        this_token = request.META.get('HTTP_USERTOKEN')

        # c_profit = 0
        # c_count = 0

        # JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate()
        # JalaliDate(1397, 1, 1).todate()
        # (JalaliDatetime(datetime.now()).weekdaynameascii()).encode('utf-8')

        start_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().year,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().month,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().day)

        user_login, this_user = user_login_check(request)

        if user_login:

            try:
                this_explore_posts = Note_Db_Renote.objects.filter(user__private__contains=0).exclude(user =this_user).order_by('-date')
            except:
                this_explore_posts = []

            if this_explore_posts :
                for post in this_explore_posts:

                    number_of_likes =  Likes_DB.objects.filter(post = post).count()

                    try:
                        Likes_DB.objects.filter(user = this_user, post = post).get()
                        is_like = 1
                    except:
                        is_like = 0

                    post_user = post.user
                    post_details = {}

                    post_details["tracking_code"] = post.tracking_code
                    post_details["note"] = post.note
                    post_details["user_name"] = post_user.username
                    post_details["date"] = str(JalaliDatetime(post.date)).split(" ")[0]
                    post_details['post_photo'] = post.photo.name
                    post_details['likes'] = number_of_likes
                    post_details['is_like'] = is_like

                    posts_history.append(post_details)
            posts_history = sorted(posts_history, key=lambda x: x['date'], reverse=True)



            request_user['status'] = 'ok'
            request_user["note_list"] = posts_history

            status = 200
            return JsonResponse(request_user , status=status)
        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================






#TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

#===========================================================================
#========================= user_analysis_handler ===========================
#===========================================================================
@csrf_exempt
def users_page_handler(request):

    request_user = {}
    posts_history = []

    if (request.method == "POST"):

        this_token = request.META.get('HTTP_USERTOKEN')

        # c_profit = 0
        # c_count = 0

        # JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate()
        # JalaliDate(1397, 1, 1).todate()
        # (JalaliDatetime(datetime.now()).weekdaynameascii()).encode('utf-8')

        start_date = dt.date(JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().year,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().month,\
            JalaliDate(JalaliDatetime(datetime.now()).year, JalaliDatetime(datetime.now()).month, 1).todate().day)



        user_login, this_user = user_login_check(request)

        this_username,error_codes,success_flag = validate_user_page(request)

        if user_login:

            this_page_user = Users_Db_Renote.objects.get(username = this_username)

            users_follower = Follow_DB.objects.filter(follower=this_page_user , accepted = 1).values_list('followee', flat=True)
            users_followee = Follow_DB.objects.filter(followee=this_page_user , accepted = 1).values_list('follower', flat=True)

            try:
                Follow_DB.objects.filter(follower=this_user , followee=this_page_user , accepted = 1).get()
                is_follow = 1
            except:
                is_follow = 0

            this_user_posts =  Note_Db_Renote.objects.filter(user=this_page_user).order_by('-date')

            if this_user_posts :
                for post in this_user_posts:

                    number_of_likes =  Likes_DB.objects.filter(post = post).count()

                    try:
                        Likes_DB.objects.filter(user = this_user, post = post).get()
                        is_like = 1
                    except:
                        is_like = 0

                    post_user = post.user
                    post_details = {}

                    post_details["tracking_code"] = post.tracking_code
                    post_details["note"] = post.note
                    post_details["user_name"] = post_user.username
                    post_details["date"] = str(JalaliDatetime(post.date)).split(" ")[0]
                    post_details['post_photo'] = post.photo.name
                    post_details['likes'] = number_of_likes
                    post_details['is_like'] = is_like

                    posts_history.append(post_details)

            posts_history = sorted(posts_history, key=lambda x: x['date'], reverse=True)


            request_user['status'] = 'ok'
            request_user["note_list"] = posts_history
            request_user['user_data'] = {

                    'user_name': this_page_user.username,
                    'posts': len(posts_history),
                    'followers': len(users_followee),
                    'following': len(users_follower),
                    'is_follow': is_follow,
                    # 'status' : this_user.status,
                }

            status = 200
            return JsonResponse(request_user , status=status)
        else:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)

#===========================================================================
#===========================================================================






#=================================================================================================================================================
#================================================================  end  =====================================================================
#=================================================================================================================================================



#===========================================================================
#=========================== register_handler ==============================
#===========================================================================
@csrf_exempt
def user_logout_handler(request):

    request_user = {}
    if (request.method == "POST"):
        time.sleep(1)

        this_token = request.META.get('HTTP_USERTOKEN')


        try:
            Users_Tokens_Db_Renote.objects.filter(assigned_token = this_token).get().delete()


            request_user['status'] = 'ok'
            request_user['message'] = "کاربر به درستی خارج شد"
            status = 200
            return JsonResponse(request_user , status=status)

        except:
            request_user['status'] = 'error'
            request_user['message'] = 'کاربر وارد نشده است '
            request_user['error_codes'] = USER_NOT_EXIST_ERR
            status = 403
            return JsonResponse(request_user , status=status)
    else:
        request_user['status'] = 'error'
        status = 403
        return JsonResponse(request_user , status=status)
#===========================================================================
#===========================================================================




#===========================================================================
#===========================================================================
#===========================================================================

@csrf_exempt
def defaults_val_handler(request):

    #------------------------Assign HTML Parameters-------------------------
    error_codes = []
    warning_codes = []
    request_user = {}
    #-----------------------------------------------------------------------

    #------------------------Check for Authorization------------------------

    #-----------------------------------------------------------------------

    #---------------------If the User Is NOT Authorized---------------------
    if request.method == "POST":
        success_flag = 0
        try:
            input_data = json.loads(request.body)
        except:
            input_data = {}
        try:
            API_token = request.META.get('HTTP_APITOKEN')
        except:
            API_token = ''



        if (API_token not in [API_TOKEN_USER]):  #and (request.method == "POST"):
            #success_flag = 0
            err_dict = {'error_code':'6700','error_msg':'Sorry! You are not allowed to view this page.'}
            error_codes.append(err_dict)
            request_user = {}
            request_user['status'] = 'error'
            status = 403
            return JsonResponse(request_user , status=status)
    #-----------------------------------------------------------------------

    #-------------------------If the User Is Authorized---------------------
        else:
            success_flag = 1
            request_user = DEFAULT_VALUES
            # request_user['status'] = 'ok'
            status = 200
            return JsonResponse(request_user , status=status)
    else:
        request_user = {}
        request_user['status'] = 'error'
        status = 400
        return JsonResponse(request_user , status=status)
#===========================================================================
#===========================================================================
