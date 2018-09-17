# -*- coding: utf-8 -*-



ALLOWED_DAY_TYPES = {
    "shanbe": u'شنبه'
    ,
    "1shanbe": u'یکشنبه'
    ,
    "2shanbe": u'دوشنبه'
    ,
    "3shanbe": u'سه‌شنبه'
    ,
    "4shanbe": u'چهارشنبه'
    ,
    "5shanbe": u'پنج‌شنبه'
    ,
    "adine": u'جمعه'
}


ALLOWED_PAYMENT_STATUSES_FARSI = {
    'pending':u'منتظر پرداخت'
    ,
    'paid':u'پرداخت شده'
    ,
    'cancelled':u'لغو شده'
    ,
    'blocked':u'اعتبار بلوکه شده'
    ,
    'unsuccessful':u'ناموفق'
    ,
    '':'نامشخص'
}


ALLOWED_PAYMENT_METHODS_FARSI = {
    'cash':u'نقدی'
    ,
    'credit':u'از محل اعتبار'
    ,
    '':''
}

GAP_BETWEEN_SMS = 30            # The interval before re-sending verification SMS, in seconds
SMS_CODE_LENGTH = 5
SMS_VERIFICATION_DELAY = 3600    # One day is allowed to verify the sms codeURL_BASE

#===================SMS KAVEH PARAMETERS=====================
SMS_API_KAVEH_NEGAR = ' 74625934496B54773138333876686E616F69343247706E426F4A434F46337750'
SMS_SENDER_NUMBER_KAVEH_NEGAR = ''
SMS_API_URL_KAVEH_NEGAR =  'https://api.kavenegar.com/v1/' + SMS_API_KAVEH_NEGAR + '/sms/send.json'
OUR_SMS_NUMBER = "09126058071"
# NEGINADV_TELEGRAM_CHANNEL = "https://telegram.me/Ubaar"
#============================================================



notification_messages = {
     'Registeration_SMS': 'کاربر عزیز،‌ با تشکر از عضویت شما، کد پیامکی شما:'
                        + ' %token',

}


USER_NOT_EXIST_ERR = 100
USER_NOT_REGISTERED_ERR = 101


POST_NOT_EXIST_ERR = 110

USER_EXIST_ERR = 200
SMS_EXIST_ERR = 201
