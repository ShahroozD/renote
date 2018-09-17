from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from datetime import datetime
import datetime as dt
from khayyam import *
# from django.core.context_processors import csrf

# from khayyam import *



#===========================================================================
#========================= validate_user_login =============================
#===========================================================================
def validate_user_signup(request):
    error_codes = []
    warning_codes = []
    success_flag = 1


    try:
        input_data = json.loads(request.body)
    except:
        input_data = {}

    #-------------------------Validate the Details--------------------------

    try:
        mobile_no = input_data['mobile_no']
        if not (mobile_no):
            error_codes.append('1')
            success_flag = 0
    except:
        mobile_no = ''
        error_codes.append('1')
        success_flag = 0

    try:
        user_name = input_data['user_name']
        if not (user_name):
            error_codes.append('1')
            success_flag = 0
    except:
        user_name = ''
        error_codes.append('1')
        success_flag = 0

    try:
        user_pass = input_data['user_pass']
        if not (user_pass):
            error_codes.append('1')
            success_flag = 0
    except:
        user_pass = ''
        error_codes.append('2')
        success_flag = 0

    try:
        introduction_code = input_data['introduction_code']
    except:
        introduction_code = ''
        # error_codes.append('2')
        # success_flag = 0



    return mobile_no,user_name,user_pass,introduction_code,error_codes,success_flag



#===========================================================================
#===========================================================================






#===========================================================================
#========================= validate_user_login =============================
#===========================================================================
def validate_sms_verifi(request):
    error_codes = []
    warning_codes = []
    success_flag = 1


    try:
        input_data = json.loads(request.body)
    except:
        input_data = {}

    #-------------------------Validate the Details--------------------------

    try:
        user_name = input_data['user_name']
        if not (user_name):
            error_codes.append('1')
            success_flag = 0
    except:
        user_name = ''
        error_codes.append('0')
        success_flag = 0

    try:
        user_code = input_data['user_code']
        if not (user_code):
            error_codes.append('1')
            success_flag = 0
    except:
        user_code = ''
        error_codes.append('0')
        success_flag = 0

    return user_name,user_code,error_codes,success_flag

#===========================================================================
#===========================================================================






#===========================================================================
#========================= validate_user_login =============================
#===========================================================================
def validate_user_login(request):
    error_codes = []
    warning_codes = []
    success_flag = 1


    try:
        input_data = json.loads(request.body)
    except:
        input_data = {}

    #-------------------------Validate the Details--------------------------

    try:
        user_name = input_data['user_name']
        if not (user_name):
            error_codes.append('1')
            success_flag = 0
    except:
        user_name = ''
        error_codes.append('0')
        success_flag = 0

    try:
        user_pass = input_data['user_pass']
        if not (user_pass):
            error_codes.append('1')
            success_flag = 0
    except:
        user_pass = ''
        error_codes.append('0')
        success_flag = 0

    return user_name,user_pass,error_codes,success_flag

#===========================================================================
#===========================================================================





#===========================================================================
#=========================== validate_submit_re ============================
#===========================================================================
def validate_submit_tr(request):
    error_codes = []
    warning_codes = []
    success_flag = 1

    try:
        input_data = json.loads(request.POST['json'])
    except:
        input_data = {}

    try:
        input_file = request.FILES['photo']
    except:
        input_file = ""

    #-------------------------Validate the Details--------------------------
    try:
        user_token = request.META.get('HTTP_USERTOKEN')
        if not (user_token):
            error_codes.append('1')
            success_flag = 0
    except:
        user_token = ''
        success_flag = 0
        error_codes.append('0')


    if success_flag:

        try:
            note = input_data['note']
            if not (note):
                error_codes.append('1')
                success_flag = 0
        except:
            note = 0
            error_codes.append('0')
            success_flag = 0


        photo = input_file

        try:
            group = input_data['group']
        except:
            group = ''
            # error_codes.append('0')
            # success_flag = 0


    else:
        error_codes.append('403')
        success_flag = 0

        this_note,this_photo,this_group
    return note,photo,group,error_codes,success_flag

#===========================================================================
#===========================================================================





#===========================================================================
#========================= validate_user_login =============================
#===========================================================================
def validate_post_like(request):
    error_codes = []
    warning_codes = []
    success_flag = 1


    try:
        input_data = json.loads(request.body)
    except:
        input_data = {}

    #-------------------------Validate the Details--------------------------

    try:
        tracking_code = input_data['tracking_code']
        if not (tracking_code):
            error_codes.append('1')
            success_flag = 0
    except:
        tracking_code = ''
        error_codes.append('0')
        success_flag = 0

    try:
        this_type = input_data['type']
        # if not (type):
        #     error_codes.append('1')
        #     success_flag = 0
    except:
        this_type = 'like'
        # error_codes.append('0')
        # success_flag = 0

    return tracking_code,this_type,error_codes,success_flag

#===========================================================================
#===========================================================================




#===========================================================================
#========================= validate_user_login =============================
#===========================================================================
def validate_post_code(request):
    error_codes = []
    warning_codes = []
    success_flag = 1


    try:
        input_data = json.loads(request.body)
    except:
        input_data = {}

    #-------------------------Validate the Details--------------------------

    try:
        tracking_code = input_data['tracking_code']
        if not (tracking_code):
            error_codes.append('1')
            success_flag = 0
    except:
        tracking_code = ''
        error_codes.append('0')
        success_flag = 0



    return tracking_code,error_codes,success_flag

#===========================================================================
#===========================================================================


#===========================================================================
#========================= validate_user_login =============================
#===========================================================================
def validate_user_page(request):
    error_codes = []
    warning_codes = []
    success_flag = 1


    try:
        input_data = json.loads(request.body)
    except:
        input_data = {}

    #-------------------------Validate the Details--------------------------

    try:
        user_name = input_data['user_name']
        if not (user_name):
            error_codes.append('1')
            success_flag = 0
    except:
        user_name = ''
        error_codes.append('0')
        success_flag = 0



    return user_name,error_codes,success_flag

#===========================================================================
#===========================================================================




# validate_user_follow

#===========================================================================
#========================= validate_user_login =============================
#===========================================================================
def validate_user_follow(request):
    error_codes = []
    warning_codes = []
    success_flag = 1


    try:
        input_data = json.loads(request.body)
    except:
        input_data = {}

    #-------------------------Validate the Details--------------------------

    try:
        user_name = input_data['user_name']
        if not (user_name):
            error_codes.append('1')
            success_flag = 0
    except:
        user_name = ''
        error_codes.append('0')
        success_flag = 0

    try:
        this_type = input_data['type']
        # if not (type):
        #     error_codes.append('1')
        #     success_flag = 0
    except:
        this_type = 'follow'
        # error_codes.append('0')
        # success_flag = 0

    return user_name,this_type,error_codes,success_flag

#===========================================================================
#===========================================================================







# =================================================================================================================
# =================================================================================================================
# =================================================================================================================




#===========================================================================
#=============================validate_address==============================
#===========================================================================
def validate_address(address):
    if len(address) >= 3:
        return 1
    else:
        return 0
#===========================================================================
#===========================================================================

#===========================================================================
#============================validate_city_name=============================
#===========================================================================
def validate_city_name(city_name):
    #regex = re.compile(r'^[^\W\d_]+(-[^\W\d_]+)?$', re.U)
    #regex = re.compile(r'^(?:(?![\d_])\w )+$', re.U)
    regex = re.compile(r'^(?:[^\W\d_]|[\s])+$', re.U)

    val = format(regex.match(city_name) is not None)
    if val == 'True':
        return city_name
    else:
        return True#False
#===========================================================================
#===========================================================================


#===========================================================================
#============================validate_state_name=============================
#===========================================================================
def validate_state_name(state_name):
    #regex = re.compile(r'^[^\W\d_]+(-[^\W\d_]+)?$', re.U)
    #regex = re.compile(r'^(?:(?![\d_])\w )+$', re.U)
    if 0:
        regex = re.compile(r'^(?:[^\W\d_]|[\s])+$', re.U)

        val = format(regex.match(city_name) is not None)
        if val == 'True':
            return city_name
        else:
            return False
    if len(state_name)>2:
        return state_name
    else:
        return True#False
#===========================================================================
#===========================================================================


#===========================================================================
#==============================validate_name================================
#===========================================================================
def validate_name(name):
    #regex = re.compile(r'^[^\W\d_]+(-[^\W\d_]+)?$', re.U)
    #regex = re.compile(r'^(?:(?![\d_])\w )+$', re.U)
    regex = re.compile(r'^(?:[^\W\d_]|[\s])+$', re.U)

    val = format(regex.match(name) is not None)
    if val == 'True':
        return True
    else:
        return False
#===========================================================================
#===========================================================================

#===========================================================================
#=============================validate_address==============================
#===========================================================================
def validate_address(address):
    if len(address) > 10:
        return 1
    else:
        return 0
#===========================================================================
#===========================================================================


#===========================================================================
#===========================validate_cellphone==============================
#===========================================================================
def validate_cellphone(phone_no):
    try:
        if phone_no[0:3] == '+98':
            phone_no = phone_no[3:]

        if phone_no[0] != '0':
            phone_no = "0" + phone_no

        if phone_no[0:2] != '09':
            return 0
        else:
            MOBILEPHONE_RE = re.compile(r"^[0-9]{11}$")
            if MOBILEPHONE_RE.match(phone_no):
                return phone_no
            else:
                return 0
    except:
        return 0
#===========================================================================
#===========================================================================


#===========================================================================
#=============================validate_phone================================
#===========================================================================
def validate_phone(phone_no):
    if phone_no[0:3] == '+98':
        phone_no = phone_no[3:]


    if phone_no[0] != "0":
        return 0
    #MOBILEPHONE_RE = re.compile(r"^[0-9]{8,14}$")
    MOBILEPHONE_RE = re.compile(r"^[0-9]{11}$")
    if MOBILEPHONE_RE.match(phone_no):
        return phone_no
    else:
        return 0
#===========================================================================
#===========================================================================


#===========================================================================
#=========================validate_national_id==============================
#===========================================================================
def validate_national_id(national_id):
    national_id = national_id.replace('-','')
    if not national_id.isdigit():
        return 0
    else:
        return national_id
#===========================================================================
#===========================================================================


#===========================================================================
#===========================validate_user_name===============================
#===========================================================================
def validate_user_name(name):
    regex = re.compile(r"^[a-zA-Z0-9_.]+$", re.U)
    val = format(regex.match(name) is not None)
    if val == 'True':
        return True
    else:
        return False
#===========================================================================
#===========================================================================

#===========================================================================
#==========================validate_number_plate============================
#===========================================================================
def validate_number_plate(plate_no):
    if len(plate_no) < 8:
        return 0
    else:
        return plate_no
#===========================================================================
#===========================================================================

#===========================================================================
#============================validate_date==================================
#===========================================================================
def validate_date(input_date):
    try:
        return_date = datetime.strptime(input_date, '%Y-%m-%d')
        return return_date.date()
    except ValueError:
        return_date = "Incorrect data format, should be YYYY-MM-DD"

        return 0
#===========================================================================
#===========================================================================




#===========================================================================
#============================validate_bank_card=============================
#===========================================================================
def validate_bank_card(bank_card):
    if (len(bank_card) != 16):
        return 0
    else:
        return 1
#===========================================================================
#===========================================================================



#===========================================================================
#===============================valid_website===============================
#===========================================================================
def valid_website(website_name):
    import validators
    if ('http://' not in website_name) and ('https://' not in website_name):
        website_name = 'http://' + website_name
    if validators.url(website_name):
        return True
    else:
        return False
#===========================================================================
#===========================================================================


#===========================================================================
#================================valid_email================================
#===========================================================================
def valid_email(email):
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    return EMAIL_RE.match(email)
#===========================================================================
#===========================================================================


#===========================================================================
#================================valid_email================================
#===========================================================================
def valid_pass(password):
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    return PASSWORD_RE.match(password)
#===========================================================================
#===========================================================================


#===========================================================================
#===========================validate_descriptions===========================
#===========================================================================
def validate_descriptions(text_str):
    regex = re.compile(r'^[A-Za-z0-9.,:;!?()\s\n\-\t\%]+$', re.U)
    return format(regex.match(text_str) is not None)
#===========================================================================
#===========================================================================



#===========================================================================
#================================validate_time==============================
#===========================================================================
def validate_time(input_time):
    try:
        t = datetime.strptime(input_time, '%H:%M')
    except:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        t =  0
    return t
#===========================================================================
#===========================================================================
