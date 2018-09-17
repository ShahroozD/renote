var pathArray = location.href.split( '/' );
var protocol = pathArray[0];
var host = pathArray[2];
var url = protocol + '//' + host;
var base_IP = url;
if ($('#server_url_field').val()){
    base_IP = $('#server_url_field').val();
};



function user_login() {


        jQuery.ajax({

            url : base_IP + '/api/user_login/',

            type: 'POST',

            dataType : "json",

            headers: {"Content-type": "application/json"},

            data: JSON.stringify({
                  user_name: $('#login_username').val(),
                  user_pass: $('#login_password').val(),
                  device_type: "web",
                }),

            error: function(xhr, status, error, json) {
                alert('')
            },

            success: function(json) {
                    // Cookies.set('user_token', json.user_data.token, { expires: 60 });
                    console.log(json.token);
                    Cookies.set('user_token', json.token);
                    window.location.replace("/dashboard");
            }

        }).always(function( xhr, status ) {
        });

}


function user_signup() {

    jQuery.ajax({

        url : base_IP + '/api/user_signup/',

        type: 'POST',

        dataType : "json",

        headers: {"Content-type": "application/json"},

        data: JSON.stringify({
              user_name: $('#register_username').val(),
              mobile_no: $('#register_mobile').val(),
              user_pass: $('#register_password').val(),
              device_type: "web",
            }),

        error: function(xhr, status, error, json) {
            alert('')
        },

        success: function(json) {
                // Cookies.set('user_token', json.user_data.token, { expires: 60 });
                Cookies.set('user_token', json.token);
                window.location.replace("/dashboard");
        }

    }).always(function( xhr, status ) {
    });

}



jQuery(document).ready(function() {

    $('#login_btn').click(function() {
      user_login()
    })

    $('#register-btn').click(function() {
      $('.login-form').hide()
      $('.register-form').show()
    })

    $('#register-back-btn').click(function() {
      $('.login-form').show()
      $('.register-form').hide()
    })

    $('#register-submit-btn').click(function() {
      user_signup()
    })


});
