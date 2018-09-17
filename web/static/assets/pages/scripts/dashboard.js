var pathArray = location.href.split( '/' );
var protocol = pathArray[0];
var host = pathArray[2];
var url = protocol + '//' + host;
var base_IP = url;
if ($('#server_url_field').val()){
    base_IP = $('#server_url_field').val();
};



function post_submit() {


        var tr_data = new FormData();
        tr_data.append('photo', $('#invoice')[0].files[0]);
        tr_data.append('json', JSON.stringify({
              note: $('#note').val().replace(/,/g , ''),
            }));

        jQuery.ajax({

            url : base_IP + '/api/submit_post/',

            type: 'POST',

            // dataType : "json",
            cache: false,
            contentType: false,
            processData: false,
            enctype: 'multipart/form-data',

            headers: {"USERTOKEN": Cookies.get('user_token')},

            data: tr_data,

            error: function(xhr, status, error, json) {
                alert('خطا')
            },

            success: function(json) {
                    // Cookies.set('user_token', json.user_data.token, { expires: 60 });
                    // Cookies.set('user_token', json.token);
                    // window.location.replace("/dashboard");
                    alert("ثبت شد")
                    location.reload();
            }

        }).always(function( xhr, status ) {
        });

}






function add_wallet() {


  var wallet_data = new FormData();
  wallet_data.append('json', JSON.stringify({
        count: $('#wallet_count').val().replace(/,/g , ''),
        description: "",
        isincome: 1,
        payment_method: "initial",
        Tr_group: $('#Tr_group_reg').val(),
      }));


  jQuery.ajax({

      url : base_IP + '/api/submit_tr/',

      type: 'POST',

      cache: false,
      contentType: false,
      processData: false,
      enctype: 'multipart/form-data',

      headers: {"USERTOKEN": Cookies.get('user_token')},

      data: wallet_data,

      error: function(xhr, status, error, json) {
          alert('خطا')
      },

      success: function(json) {
              // Cookies.set('user_token', json.user_data.token, { expires: 60 });
              // Cookies.set('user_token', json.token);
              // window.location.replace("/dashboard");
              alert("ثبت شد")
              location.reload();
      }

  }).always(function( xhr, status ) {
  });

}






function posts_list() {

  jQuery.ajax({

      url : base_IP + '/api/user_posts_list/',

      type: 'POST',

      dataType : "json",

      headers: {"USERTOKEN": Cookies.get('user_token'), "Content-type": "application/json"},

      data: {},

      error: function(xhr, status, error, json) {
          alert('خطا')
      },

      success: function(json) {

              $('#list').html("")

              for (var tr in json.note_list) {
                (json.note_list[tr].is_like)? classname = "red_like" : classname = ""
                $('#list').append('<div class="card"><div class="card-header"><h4 class="card-title">'+ json.note_list[tr].user_name +
                 '</h4></div><img src="/img/'+ json.note_list[tr].post_photo + '" class="post-image" alt="note_image" style="width:100%">\
                 <div class="text_p"><p class="card-text">'+json.note_list[tr].note + '</p> </div><div class="card-footer">\
                 <a data-toggle="liking" class="'+classname+'"  data-code="'+ json.note_list[tr].tracking_code + '"><i class="fa fa-heart">\
                 </i></a><a href="#" class="card_num_likes">'+ json.note_list[tr].likes + '</a></div></div>');
              }
              // Cookies.set('user_token', json.user_data.token, { expires: 60 });
              // Cookies.set('user_token', json.token);
              // window.location.replace("/dashboard");


              $('.card-footer a').on('click', function(){
                if ($(this).data('toggle') == "liking") {
                  if($(this).hasClass("red_like")){


                      jQuery.ajax({

                          url : base_IP + '/api/like_post/',

                          type: 'POST',
                          context: this,
                          cache: false,
                          contentType: false,
                          processData: false,
                          enctype: 'multipart/form-data',

                          headers: {"USERTOKEN": Cookies.get('user_token')},

                          data: JSON.stringify({
                              "tracking_code":$(this).data('code'),
                              "type":"dislike"
                          }),

                          error: function(xhr, status, error, json) {
                              alert('خطا')
                          },

                          success: function(json) {
                             $(this).removeClass("red_like")

                             $(this).closest(".card-footer").find(".card_num_likes").html( Number($(this).closest(".card-footer").find(".card_num_likes").html())-1)


                          }

                      }).always(function( xhr, status ) {
                      });

                   }
                   else {

                     jQuery.ajax({

                         url : base_IP + '/api/like_post/',

                         type: 'POST',
                         context: this,
                         cache: false,
                         contentType: false,
                         processData: false,
                         enctype: 'multipart/form-data',

                         headers: {"USERTOKEN": Cookies.get('user_token')},

                         data: JSON.stringify({
                             "tracking_code":$(this).data('code')
                         }),

                         error: function(xhr, status, error, json) {
                             alert('خطا')
                         },

                         success: function(json) {
                            $(this).addClass("red_like");
                            $(this).closest(".card-footer").find(".card_num_likes").html( Number($(this).closest(".card-footer").find(".card_num_likes").html())+1)
                         }

                     }).always(function( xhr, status ) {
                     });
                   }

                } else {

                }

              })


              $('.card-title').on('click', function(){

                      jQuery.ajax({

                          url : base_IP + '/api/users_page/',

                          type: 'POST',
                          context: this,
                          cache: false,
                          contentType: false,
                          processData: false,
                          enctype: 'multipart/form-data',

                          headers: {"USERTOKEN": Cookies.get('user_token')},

                          data: JSON.stringify({
                              "user_name":$(this).html(),
                          }),

                          error: function(xhr, status, error, json) {
                              alert('خطا')
                          },

                          success: function(json) {

                            $("#usernamePage").html(json.user_data.user_name)
                            $("#postsPage").html(json.user_data.posts)
                            $("#postFollowers").html(json.user_data.followers)
                            $("#postFollowing").html(json.user_data.following)
                            $('#btn-req').data('username',json.user_data.user_name)

                            if (json.user_data.is_follow) {
                              $('#btn-req').removeClass('btn')
                              $('#btn-req').html('دنبال شده')
                            } else {
                              $('#btn-req').addClass('btn')
                              $('#btn-req').html('دنبال کردن')
                            }

                            $('#pageModal .row').html('')
                            for (var tr in json.note_list) {
                              $('#pageModal .row').append('<div class="card explore col-xs-4"><a data-toggle="" class="pageImage"  \
                              data-code="'+ json.note_list[tr].tracking_code + '"><img src="/img/'+ json.note_list[tr].post_photo + '" \
                              class="card-image" alt="note_image" style="width:100%"></a> </div>');
                            }

                            $("#pageModal").modal();

                          }

                      }).always(function( xhr, status ) {
                      });


              })

      }

  }).always(function( xhr, status ) {
  });

}








function user_profile() {

  jQuery.ajax({

      url : base_IP + '/api/user_profile/',

      type: 'POST',
      context: this,
      cache: false,
      contentType: false,
      processData: false,
      enctype: 'multipart/form-data',

      headers: {"USERTOKEN": Cookies.get('user_token')},

      data: {},

      error: function(xhr, status, error, json) {
          alert('خطا')
      },

      success: function(json) {

        $("#usernameProfile").html(json.user_data.user_name)
        $("#postsUser").html(json.user_data.posts)
        $("#userFollowers").html(json.user_data.followers)
        $("#userFollowing").html(json.user_data.following)
        $('#btn-req').data('username',json.user_data.user_name)


        $('#profile .row').html('')
        for (var tr in json.note_list) {
          $('#profile .row').append('<div class="card explore col-xs-4"><a data-toggle="" class="pageImage"  \
          data-code="'+ json.note_list[tr].tracking_code + '"><img src="/img/'+ json.note_list[tr].post_photo + '" \
          class="card-image" alt="note_image" style="width:100%"></a> </div>');
        }

      }

  }).always(function( xhr, status ) {
  });

}







function explore_list() {

  jQuery.ajax({

      url : base_IP + '/api/explore_posts_list/',

      type: 'POST',

      dataType : "json",

      headers: {"USERTOKEN": Cookies.get('user_token'), "Content-type": "application/json"},

      data: {},

      error: function(xhr, status, error, json) {
          alert('خطا')
      },

      success: function(json) {

              $('#explore_list .row').html("")

              for (var tr in json.note_list) {
                $('#explore_list .row').append('<div class="card explore col-xs-4"><a data-toggle="" class=""  \
                data-code="'+ json.note_list[tr].tracking_code + '"><img src="/img/'+ json.note_list[tr].post_photo + '" \
                class="card-image" alt="note_image" style="width:100%"></a> </div>');
              }
              // Cookies.set('user_token', json.user_data.token, { expires: 60 });
              // Cookies.set('user_token', json.token);
              // window.location.replace("/dashboard");
              $('.card.explore a').click(function() {

                    jQuery.ajax({

                        url : base_IP + '/api/post_details/',

                        type: 'POST',

                        dataType : "json",

                        headers: {"USERTOKEN": Cookies.get('user_token'), "Content-type": "application/json"},

                        data: JSON.stringify({
                            "tracking_code":$(this).data('code'),
                        }),

                        error: function(xhr, status, error, json) {
                            alert('خطا')
                        },

                        success: function(json) {
                          $('#post_username').html(json.post_details.user_name);
                          $('#post_note').html(json.post_details.note);
                          $('#post_num_likes').html(json.post_details.likes);
                          (json.post_details.is_like)?$('#post_like').addClass('red_like'):$('#post_like').removeClass('red_like');
                          $('#post_like').data('code' , json.post_details.tracking_code);
                          $('#post_image').attr('src','/img/'+json.post_details.post_photo);
                          $("#postModal").modal();

                        }

                    }).always(function( xhr, status ) {
                    });


              })
      }

  }).always(function( xhr, status ) {
  });

}













function logout() {


  jQuery.ajax({

      url : base_IP + '/api/user_logout/',

      type: 'POST',

      dataType : "json",

      headers: {"USERTOKEN": Cookies.get('user_token'), "Content-type": "application/json"},

      data: {},

      error: function(xhr, status, error, json) {
          alert('خطا')
      },

      success: function(json) {
          document.cookie = 'user_token=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
          window.location.replace("/");
      }

  }).always(function( xhr, status ) {
  });

}










jQuery(document).ready(function() {

    explore_list()
    posts_list()
    user_profile()


    $('#post_submit_btn').click(function() {
      post_submit()
    })



    $('#register-btn').click(function() {
      $('.login-form').hide()
      $('.register-form').show()
    })


    $('#radioBtn a').on('click', function(){
        var sel = $(this).data('title');
        var tog = $(this).data('toggle');
        $('#'+tog).prop('value', sel);

        if (sel == "0") {
          $('.costing').show()
          $('.transfer').hide()
        } else if (sel == "1"){
          $('.costing').hide()
          $('.transfer').hide()
        } else {
          $('.costing').hide()
          $('.transfer').show()
        }

        $('a[data-toggle="'+tog+'"]').not('[data-title="'+sel+'"]').removeClass('active').addClass('notActive');
        $('a[data-toggle="'+tog+'"][data-title="'+sel+'"]').removeClass('notActive').addClass('active');
    })



    $('#radioBtn_out a').on('click', function(){
        var sel = $(this).data('title');
        var tog = $(this).data('toggle');
        $('#'+tog).prop('value', sel);

        $('a[data-toggle="'+tog+'"]').not('[data-title="'+sel+'"]').removeClass('active').addClass('notActive');
        $('a[data-toggle="'+tog+'"][data-title="'+sel+'"]').removeClass('notActive').addClass('active');
    })


    $('#date a').on('click', function(){
        var sel = $(this).data('title');
        var tog = $(this).data('toggle');
        $('#'+tog).prop('value', sel);

        if (sel == "1") {
          $('.date-picker').show()
        } else {
          $('.date-picker').hide()
        }

        $('a[data-toggle="'+tog+'"]').not('[data-title="'+sel+'"]').removeClass('active').addClass('notActive');
        $('a[data-toggle="'+tog+'"][data-title="'+sel+'"]').removeClass('notActive').addClass('active');
    })




    $('#icon_bar a').on('click', function(){
        var sel = $(this).data('title');
        var tog = $(this).data('toggle');
        $('.page-title span').html(tog)
        // $('#'+tog).prop('value', sel);
        if (sel == "explore") {
          $('#explore_list').show()
          $('#addtransaction').hide()
          $('#list').hide()
          $('#profile').hide()
        } else if(sel == "profile") {
          $('#explore_list').hide()
          $('#addtransaction').hide()
          $('#list').hide()
          $('#profile').show()
        } else if(sel == "list") {
          $('#explore_list').hide()
          $('#addtransaction').hide()
          $('#list').show()
          $('#profile').hide()
        } else {
          $('#explore_list').hide()
          $('#profile').hide()
          $('#list').hide()
          $('#addtransaction').show()
        }

        // $('a[data-toggle="'+tog+'"]').not('[data-title="'+sel+'"]').removeClass('active').addClass('notActive');
        // $('a[data-toggle="'+tog+'"][data-title="'+sel+'"]').removeClass('notActive').addClass('active');
    })



    $('#logout_btn').click(function() {
      logout()
    })





    $('#btn-req').click(function() {


      jQuery.ajax({

          url : base_IP + '/api/following/',

          type: 'POST',

          dataType : "json",

          headers: {"USERTOKEN": Cookies.get('user_token'), "Content-type": "application/json"},

          data: JSON.stringify({
              "user_name":$(this).data('username'),
              "type":(!$('#btn-req').hasClass('btn'))? "unfollow":"follow"
          }),

          error: function(xhr, status, error, json) {
              alert('خطا')
          },

          success: function(json) {

              if (!$('#btn-req').hasClass('btn')) {
                $('#btn-req').addClass('btn')
                $("#postFollowers").html(parseInt($("#postFollowers").html())-1)
                $('#btn-req').html('دنبال کردن')
              } else {
                $('#btn-req').removeClass('btn')
                $("#postFollowers").html(parseInt($("#postFollowers").html())+1)
                $('#btn-req').html('دنبال شده')
              }

          }

      }).always(function( xhr, status ) {
      });

    })





});
