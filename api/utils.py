# -*- coding: utf-8 -*-
from math import sin, cos, sqrt, atan2, radians
import random
import binascii
import os
from numpy.random import RandomState
from numpy.random import randint
import time
import string
import hashlib
from datetime import datetime
from user_agents import parse



from api.models import Users_Db_Renote, Users_Tokens_Db_Renote, Note_Db_Renote





#===========================================================================
#=========================generate_tracking_code============================
#===========================================================================
def generate_tracking_code(code_length):

    prng = RandomState(int(time.time()))
    temp = str(prng.randint(1,10,code_length))
    tracking_code = temp.strip('[]')
    tracking_code = tracking_code.replace(' ','')

    return tracking_code
#===========================================================================
#===========================================================================




#===========================================================================
#===============================generate_token==============================
#===========================================================================
def generate_token(cellphone,backend_key=''):
    # token = binascii.b2a_hex(os.urandom(15))
    lst = [random.choice('0123456789abcdefghijklmnopqrstuvwxyz' + cellphone) for n in range(27)]
    token = "".join(lst)
    return token
#===========================================================================
#===========================================================================



#===========================================================================
#===============================send_sms_kaveh==============================
#===========================================================================
def send_sms_kaveh(receiver_phone_no,msg):
    sender_phone = SMS_SENDER_NUMBER_KAVEH_NEGAR
    sms_params = ''
    sms_params = sms_params + '?receptor=' + receiver_phone_no
    sms_params = sms_params + '&message=' + msg
    sms_params = sms_params + '&sender=' + sender_phone

    api_url = SMS_API_URL_KAVEH_NEGAR + sms_params

    try_notif = 0
    notif_sent = ''

    while ((not notif_sent) and (try_notif<2)):
        response = send_request(api_url, method='POST')
        if response.ok:
            notif_sent = response.content
        else:
            try_notif = try_notif + 1

    if notif_sent:
        if json.loads(notif_sent)['return']['status'] != 200:
            #notif_sent = ''
            # print 1
            pass
    return notif_sent
#===========================================================================
#===========================================================================




#===========================================================================
#================================make_salt==================================
#===========================================================================
def make_salt():
    output = []
    for i in range(0,5):
        output.append(random.choice(string.ascii_letters))
    return("".join(output))
    # return(string.join(output,""))
#===========================================================================
#===========================================================================


#===========================================================================
#==============================make_hashed_pw===============================
#===========================================================================
def make_hashed_pw(name, pw):
    salt = make_salt()
    # name = name.encode('utf-8')
    # pw = pw.encode('utf-8')
    return hashlib.sha256((name + pw + salt).encode('utf-8')).hexdigest() + '|' + salt
#===========================================================================
#===========================================================================

#===========================================================================
#===============================valid_hash_pw===============================
#===========================================================================
def valid_hash_pw(name, pw, h):
    temp = h.split('|',3)
    hashed_val = temp[0]
    salt = temp[1]
    # print(hashlib.sha256(name + pw + salt).hexdigest())
    # print(hashlib.sha256((name + pw + salt).encode('utf-8')).hexdigest())
    # print(hashed_val)

    if (hashed_val == hashlib.sha256((name + pw + salt).encode('utf-8')).hexdigest()):
        return hashed_val
    else:
        return 0
#===========================================================================
#===========================================================================





#===========================================================================
#=========================generate_tracking_code============================
#===========================================================================
def user_login_check(request):

    user_token = request.META.get('HTTP_USERTOKEN')
    user_login = 0
    this_user = ''


    try:
        this_tok_obj = Users_Tokens_Db_Renote.objects.filter(assigned_token = user_token).get()
        this_user = this_tok_obj.user

        if this_user and this_tok_obj.device == str(parse(request.META['HTTP_USER_AGENT'])):
            user_login = 1

            this_user.last_login_time = datetime.now()
            this_user.save()

            this_tok_obj.assigned_token_last_time = datetime.now()
            this_tok_obj.save()

    except:
        pass



    return user_login, this_user
#===========================================================================
#===========================================================================
