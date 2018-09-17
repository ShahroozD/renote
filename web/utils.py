from __future__ import division
import re
# import requests
import string
import random
import hashlib
import binascii
from datetime import datetime,timedelta
import time
import json
import os
import math
# import urllib2,urllib, httplib, socket
# from urllib import quote
# from multiprocessing.pool import ThreadPool
# from django.db.models import Q
from user_agents import parse

from django.core.mail import EmailMessage
from django.db.models import Sum

from api.models import Users_Db_Renote, Users_Tokens_Db_Renote, Note_Db_Renote








#===========================================================================
#==============================get_cookie===============================
#===========================================================================
def get_cookie(request):


    #--------------------Check if the user has already logged in------------
    user_token = request.COOKIES.get('user_token')
    login_flag = 0
    isHamyar_flag = 0
    userid = ''
    admin_flag = 0
    name_usr = ''
    user_role = ''
    access_level = ''
    phone_number = ''
    user_mobile = ''
    organization_usr = ''
    address = ''
    error_codes = []

    if user_token:


        try:

            # this_user = Users_Db_Renote.objects.filter(assigned_token = user_token).get()
            this_tok_obj = Users_Tokens_Db_Renote.objects.filter(assigned_token = user_token).get()
            this_user = this_tok_obj.user

            # TODO
            if this_tok_obj.device == str(parse(request.META['HTTP_USER_AGENT'])):

                login_flag = 1

                # resp = json.loads(response.content)
                # users_data = resp['user_data']
                # userid = users_data['userid']
                # name_usr = users_data['name_usr']
                # phone_number = users_data['phone_number']
                # user_mobile = users_data['mobile_number']
                # address = users_data['address']

        except:
            # error_codes.append(handle_errors('Error_API_Call','Error_API_Call','error'))
            response = ''
    #----------------------------------------------------------------------

    return userid,name_usr,organization_usr,login_flag,admin_flag,isHamyar_flag,user_mobile,error_codes,phone_number,address,access_level
#===========================================================================
#===========================================================================







#===========================================================================
#==============================get_cookie===============================
#===========================================================================
def get_wallet_list(request):


    #--------------------Check if the user has already logged in------------
    user_token = request.COOKIES.get('user_token')
    login_flag = 0

    error_codes = []
    Tr_groups = []

    if user_token:


        try:

            # this_user = Users_Db_Renote.objects.filter(assigned_token = user_token).get()
            this_tok_obj = Users_Tokens_Db_Renote.objects.filter(assigned_token = user_token).get()
            this_user = this_tok_obj.user
            if this_tok_obj.device == str(parse(request.META['HTTP_USER_AGENT'])):
                this_tr = Note_Db_Renote.objects.filter(user=this_user)

                for transaction in this_tr:
                    if transaction.Tr_group and transaction.Tr_group not in Tr_groups:
                        Tr_groups.append(transaction.Tr_group)


        except:
            # error_codes.append(handle_errors('Error_API_Call','Error_API_Call','error'))
            response = ''
    #----------------------------------------------------------------------

    return Tr_groups
#===========================================================================
#===========================================================================
