// Regex summary
// . Any character except newline.
// \.  A period (and so on for \*, \(, \\, etc.)
// ^ The start of the string.
// $ The end of the string.
// \d,\w,\s  A digit, word character [A-Za-z0-9_], or whitespace.
// \D,\W,\S  Anything except a digit, word character, or whitespace.
// [abc] Character a, b, or c.
// [a-z] a through z.
// [^abc]  Any character except a, b, or c.
// aa|bb Either aa or bb.
// ? Zero or one of the preceding element.
// * Zero or more of the preceding element.
// + One or more of the preceding element.
// {n} Exactly n of the preceding element.
// {n,}  n or more of the preceding element.
// {m,n} Between m and n of the preceding element.
// ??,*?,+?,
// {n}?, etc.  Same as above, but as few as possible.
// (expr)  Capture expr for use with \1, etc.
// (?:expr)  Non-capturing group.
// (?=expr)  Followed by expr.
// (?!expr)  Not followed by expr.

// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();


$(window).load(function(){
    $('.flexslider').flexslider({
        namespace: "flex-",             //{NEW} String: Prefix string attached to the class of every element generated by the plugin
        selector: ".slides > li",       //{NEW} Selector: Must match a simple pattern. '{container} > {slide}' -- Ignore pattern at your own peril
        animation: "fade",              //String: Select your animation type, "fade" or "slide"
        easing: "swing",               //{NEW} String: Determines the easing method used in jQuery transitions. jQuery easing plugin is supported!
        direction: "horizontal",        //String: Select the sliding direction, "horizontal" or "vertical"
        reverse: false,                 //{NEW} Boolean: Reverse the animation direction
        animationLoop: true,             //Boolean: Should the animation loop? If false, directionNav will received "disable" classes at either end
        smoothHeight: false,            //{NEW} Boolean: Allow height of the slider to animate smoothly in horizontal mode
        startAt: 0,                     //Integer: The slide that the slider should start on. Array notation (0 = first slide)
        slideshow: true,                //Boolean: Animate slider automatically
        slideshowSpeed: 7000,           //Integer: Set the speed of the slideshow cycling, in milliseconds
        animationSpeed: 600,            //Integer: Set the speed of animations, in milliseconds
        initDelay: 0,                   //{NEW} Integer: Set an initialization delay, in milliseconds
        randomize: false,               //Boolean: Randomize slide order

        // Usability features
        pauseOnAction: true,            //Boolean: Pause the slideshow when interacting with control elements, highly recommended.
        pauseOnHover: true,            //Boolean: Pause the slideshow when hovering over slider, then resume when no longer hovering
        useCSS: true,                   //{NEW} Boolean: Slider will use CSS3 transitions if available
        touch: true,                    //{NEW} Boolean: Allow touch swipe navigation of the slider on touch-enabled devices
        video: false,                   //{NEW} Boolean: If using video in the slider, will prevent CSS3 3D Transforms to avoid graphical glitches

        // Primary Controls
        controlNav: true,               //Boolean: Create navigation for paging control of each clide? Note: Leave true for manualControls usage
        directionNav: false,             //Boolean: Create navigation for previous/next navigation? (true/false)
        prevText: "Previous",           //String: Set the text for the "previous" directionNav item
        nextText: "Next",               //String: Set the text for the "next" directionNav item

        // Secondary Navigation
        keyboard: true,                 //Boolean: Allow slider navigating via keyboard left/right keys
        multipleKeyboard: false,        //{NEW} Boolean: Allow keyboard navigation to affect multiple sliders. Default behavior cuts out keyboard navigation with more than one slider present.
        mousewheel: false,              //{UPDATED} Boolean: Requires jquery.mousewheel.js (https://github.com/brandonaaron/jquery-mousewheel) - Allows slider navigating via mousewheel
        pausePlay: false,               //Boolean: Create pause/play dynamic element
        pauseText: 'Pause',             //String: Set the text for the "pause" pausePlay item
        playText: 'Play',               //String: Set the text for the "play" pausePlay item

        // Special properties
        controlsContainer: "",          //{UPDATED} Selector: USE CLASS SELECTOR. Declare which container the navigation elements should be appended too. Default container is the FlexSlider element. Example use would be ".flexslider-container". Property is ignored if given element is not found.
        manualControls: "",             //Selector: Declare custom control navigation. Examples would be ".flex-control-nav li" or "#tabs-nav li img", etc. The number of elements in your controlNav should match the number of slides/tabs.
        sync: "",                       //{NEW} Selector: Mirror the actions performed on this slider with another slider. Use with care.
        asNavFor: "",                   //{NEW} Selector: Internal property exposed for turning the slider into a thumbnail navigation for another slider

        // Carousel Options
        itemWidth: 0,                   //{NEW} Integer: Box-model width of individual carousel items, including horizontal borders and padding.
        itemMargin: 0,                  //{NEW} Integer: Margin between carousel items.
        minItems: 0,                    //{NEW} Integer: Minimum number of carousel items that should be visible. Items will resize fluidly when below this.
        maxItems: 0,                    //{NEW} Integer: Maxmimum number of carousel items that should be visible. Items will resize fluidly when above this limit.
        move: 0,                        //{NEW} Integer: Number of carousel items that should move on animation. If 0, slider will move all visible items.

        // Callback API
        start: function(){},            //Callback: function(slider) - Fires when the slider loads the first slide
        before: function(){},           //Callback: function(slider) - Fires asynchronously with each slider animation
        after: function(){},            //Callback: function(slider) - Fires after each slider animation completes
        end: function(){},              //Callback: function(slider) - Fires when the slider reaches the last slide (asynchronous)
        added: function(){},            //{NEW} Callback: function(slider) - Fires after a slide is added
        removed: function(){}
    });
});


/*  [GLOBAL] Variables
*******************************************************************/


/*  [GLOBAL] Functions
*******************************************************************/

  // function scrollTo(element){
  //   $('html, body').animate({ scrollTop: element.offset().top}, 500);
  // }

  function lock_screen(){
  }

  function unlock_screen(){
  }

  function chain_of_events(el){
    if (el.attr('data-events-before-request')){
      var events = el.attr('data-events-before-request').split(' ');

      for (var i = 0;i < events.length; i++){
        e = events[i].toString();

        switch(e){
          case 'beActive':
            $('a[data-eventsBeforeRequest=beActive]').removeClass('active');
            el.addClass('active');

            break;
          case 'fadeOut':
            el.fadeOut();

            break;
          case 'addDataIndex':
            el = addDataIndex(el);

            break;
          case 'remove':
            if (events[i + 1]){
              $(events[i + 1]).fadeOut(1000, function(){
                $(this).remove();
              })
            } else {
              el.fadeOut(1000, function(){
                $(this).remove();
              })
            }
          default:
            break;
        }
      }
    }

    return el;
  }

  function process_data(data){
    console.log(data)

    if (data['alert-success']){
      alertify.success(data['alert-success']);
    }

    if (data['alert-error']){
      alertify.error(data['alert-error']);
    }

    setTimeout(function() {
      if (data['redirect']){
        window.location.replace(data['redirect']);
      } else {
        if (data['href']){
          get(data['href']);
        } else if (data['template']){
          if(data['target']){
            $(data['target']).html(data['template']);
          } else {
           $('#page').html(data['template']);
          }
        }

        // if (data['alert-success']){
        //   alertify.success(data['alert-success']);
        // }

        // if (data['alert-error']){
        //   alertify.error(data['alert-error']);
        // }
      }
    }, 1000);
  }

  function before_load(){

  }

  function get(url, lock){
    var lock = (typeof lock === 'undefined') ? 'true' : lock;

    if (lock == 'true'){
      lock_screen();
    }

    $.ajax({
      url     : url,
      type    : 'get',
      cache   : false,
      success : function(data){
        process_data(data);
      },
      error   : function(data){
        alertify.error('Erro desconhecido, por favor entrar em contato com os administradores!');
      },
      complete: function(data){
        before_load();

        if (lock == 'true'){
          unlock_screen();
        }
      }
    });
  }

  function post(form, lock){
    var lock = (typeof lock === 'undefined') ? 'true' : lock;

    if (lock == 'true'){
      lock_screen();
    }

    if (form.attr('data-custom')){
      if (typeof window[form.attr('data-custom')] === 'function'){
        var data = window[form.attr('data-custom')](form);
      }
    } else {
      var data = form.serialize();
    }

    var content = (form.attr('data-content') == 'false') ? false : 'application/x-www-form-urlencoded; charset=UTF-8';
    var process = (form.attr('data-process') == 'false') ? false : true;

    $.ajax({
      url     : form.attr('action'),
      type    : form.attr('method'),
      data    : data,
      cache   : false,
      contentType: content,
      processData: process,
      success : function(data){
        process_data(data);
      },
      error   : function(data){
        alertify.error('Erro desconhecido, por favor entrar em contato com os administradores!');
      },
      complete: function(data){
        before_load();

        if (lock == 'true'){
          unlock_screen();
        }
      }
    });
  }

/*  [GLOBAL] Calls
*******************************************************************/

  $(document).on('click', 'a[data-get]', function(e){
    e.preventDefault();

    el = $(this);

    if (!el.hasClass('active')){

      if (el.attr('data-confirm')){
        alertify.set({ labels : { ok: "Sim", cancel: "Não" } });

        alertify.confirm(el.attr('data-confirm'), function (e) {
          if (e) {
            el = chain_of_events(el);

            get(el.attr('data-get'), el.attr('data-lock'));
          } else {
            alertify.log('Ação cancelada.')
          }
        });
      } else {
        el = chain_of_events(el);

        get(el.attr('data-get'), el.attr('data-lock'));
      }
    }
  });

  $(document).on('click', '[data-submit]', function(e){
    e.preventDefault();

    var el = $(this);
    var form = el.closest('form');
    var form_valid = true;
    var required_fields = form.find('[data-required]');

    required_fields.each(function(index){
      var field = $(this);
      var error_msg = field.attr('data-required');

      if (field.val() == '' || field.val() == 0){
        field.addClass('invalid');
        alertify.error(error_msg);
        form_valid = false;
      }
    });

    if (form.attr('data-default')){
      form.submit();
    } else if (form_valid){
      post(form, form.attr('data-lock'));
    }

    return false;
  })

  $(document).on('submit', 'form', function(){
    var el = $(this);
    var form_valid = true;
    var required_fields = el.find('[data-required]');

    required_fields.each(function(index){
      var field = $(this);
      var error_msg = field.attr('data-required');

      if (field.val() == '' || field.val() == 0){
        field.addClass('invalid');
        alertify.error(error_msg);
        form_valid = false;
      }
    });

    if (el.attr('data-default')){
      return true;
    } else if (form_valid){
      post(el, el.attr('data-lock'));
    }

    return false;
  });

/*  [LOCAL] Functions
*******************************************************************/

function custom_data_save_data_table(form){
    var data =                  $('#data_table').data('handsontable').getData();
    var familias_cadastradas =  $('#familias_cadastradas').val();
    var area =                  $('#area').val();
    var ano =                   $('#ano').val();
    var mes =                   $('#mes').val();
    var csrfmiddlewaretoken =   $('input[name=csrfmiddlewaretoken]').val();

    var data = {
        'data' : JSON.stringify(data),
        'familias_cadastradas' : JSON.stringify(familias_cadastradas),
        'area' : JSON.stringify(area),
        'ano' : JSON.stringify(ano),
        'mes' : JSON.stringify(mes),
        'csrfmiddlewaretoken' : csrfmiddlewaretoken,
    }

    return data;
  }