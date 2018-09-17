# -*- coding: utf-8 -*-

#===========================================================================
#=========================IMPORT NECESSARY LIBRARIES========================
#===========================================================================
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader
from django.template.loader import get_template
# from carmano.default_vals import *


from web.utils import *
#===========================================================================
#===========================================================================

#===========================================================================
#=============================  CO Data  ==============================
#===========================================================================
tel = ''
telC = ''
telE = ''

co_email = ""
co_address = ""

cont = 123423

BASE_IP_A4 = "127.0.0.1:8000"
VERSION_NUM = 0.001







#===========================================================================
#=================================login_handler=============================
#===========================================================================
# This function handles login requests from users
#===========================================================================

def login_handler(request):

    current_url = request.get_full_path() #resolve(request.path_info).url_name

    #--------------------Check if the user has already logged in------------
    user_login = 0
    userid,name_usr,organization_usr,user_login,admin_flag,isHamyar_flag,user_mobile,error_tmp,phone_number,address,access_level = get_cookie(request)
    #-----------------------------------------------------------------------

    #-------------------------Show the Related Page-------------------------
    if user_login :
        response = HttpResponseRedirect('/dashboard')
        return response
    else:
        html_parameters = {}
        html_parameters['SERVER_URL'] = BASE_IP_A4
        html_parameters['VERSION_NUM'] = "0.001"


        html_parameters['API_TOKEN'] = "AC2zToa6934"
            # if Freight_login_flag:
            #     html_parameters['Freight_login'] = 1
        template = get_template('login.html')
        contxt = RequestContext(request)
        # print(contxt)

        return HttpResponse(template.render())
    #-----------------------------------------------------------------------

#===========================================================================
#===========================================================================





#===========================================================================
#=========================== dashboard_handler =============================
#===========================================================================
def dashboard_handler(request):
    html_parameters = {}

    # user_login, user_name, user_photo = get_web_base_data(request)
    userid,name_usr,organization_usr,user_login,admin_flag,isHamyar_flag,user_mobile,error_tmp,phone_number,address,access_level = get_cookie(request)
    this_group_list = get_wallet_list(request)

    if user_login:
        html_parameters['group_list'] = this_group_list
        html_parameters['VERSION_NUM'] = VERSION_NUM
        template = get_template('dashboard.html')
        return HttpResponse(template.render(html_parameters))
    else:
        response = HttpResponseRedirect('/')
        return response


    # return render_to_response('Landing_Page.html', html_parameters)
#===========================================================================
#===========================================================================
