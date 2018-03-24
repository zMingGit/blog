
/**
 * Created by Kupletsky Sergey on 17.10.14.
 *
 * Material Sidebar (Profile menu)
 * Tested on Win8.1 with browsers: Chrome 37, Firefox 32, Opera 25, IE 11, Safari 5.1.7
 * You can use this sidebar in Bootstrap (v3) projects. HTML-markup like Navbar bootstrap component will make your work easier.
 * Dropdown menu and sidebar toggle button works with JQuery and Bootstrap.min.js
 */

// Sidebar toggle
//
// -------------------

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {  
    // these HTTP methods do not require CSRF protection  
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));  
}  
function sameOrigin(url) {  
    // test that a given url is a same-origin URL  
    // url could be relative or scheme relative or absolute  
    var host = document.location.host; // host + port  
    var protocol = document.location.protocol;  
    var sr_origin = '//' + host;  
    var origin = protocol + sr_origin;  
    // Allow absolute or scheme relative URLs to same origin  
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||  
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||  
        // or any other URL that isn't scheme relative or absolute i.e relative.  
        !(/^(\/\/|http:|https:).*/.test(url));  
}  

$(document).ready(function() {
    var $overlay = $('.sidebar-overlay');
    var $infobtn = $('.info_button');
    var $articleCard = $('.articleCard');
    var $authorCard = $('.authorCard');
    var $addcommentBtn = $('.add-comment-btn');
    var $indexImg = $('.sidebar-image');
    var $searchBtn = $('.search_btn');

    $('.sidebar-toggle').on('click', function() {
        var sidebar = $('#sidebar');
        sidebar.toggleClass('open');
        if ((sidebar.hasClass('sidebar-fixed-left') || sidebar.hasClass('sidebar-fixed-right')) && sidebar.hasClass('open')) {
            $overlay.addClass('active');
        } else {
            $overlay.removeClass('active');
            $infobtn.removeClass('hide');
        }
    });

    $overlay.on('click', function() {
        $(this).removeClass('active');
        $('#sidebar').removeClass('open');
        $infobtn.removeClass('hide');
    });

    $infobtn.on('click', function() {
        $('#sidebar').addClass('open');
        $overlay.addClass('active');
        $(this).addClass('hide');
    });

    $articleCard.each(function() {
        $(this).on('click', function() {
            var uuid = $(this).attr('uuid');
            window.location.href = '/api/article?type=uuid&uuid=' + uuid;
            return false;
        });
    });

    $authorCard.each(function() {
        $(this).on('click', function() {
            window.location.href = '/api/profile';
            return false;
        });
    });

    $addcommentBtn.click(function() {
        csrftoken = getCookie('csrftoken');  
        $.ajaxSetup({  
            beforeSend: function(xhr, settings) {  
                if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {  
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);  
                }  
            }  
        });  
        var article = $('#comment').attr('uuid')
        var comment = $('#comment').val()
        var $cmts = $('.comment')
        var url = '/api/comment';
        $.ajax({
            url: '/api/comment/',
            type: 'PUT',
            dataType: 'json',
            data: {
                'comment': comment,
                'article': article
            },
            cache: false,
            success: function(data) {
            $cmts.append('<header class="comment__header"><img src="/static/images/co1.jpg" %}" class="comment__avatar"><div class="comment__author"><strong>someone</strong><span>just now</span></div></header><div class="comment__text">'+ comment +'</div>');
            },
            error: function(xhr) {
                alert("Network error");
            }
        });
        return false
    });

    $indexImg.on('click', function() {
        window.location.href = '/';
    });

    $searchBtn.on('click', function() {
        $('.search_target').addClass('is-focused');
        $('#search_input').addClass('activate').removeClass('deactivate').focus();
        return false;
    });

    $('.demo-blog').on('click', function() {
        $('.search_target').removeClass('is-focused').addClass('deactivate').removeClass('activate');
        $('#search_input').removeClass('activate').addClass('deactivate');
        $('.search_target').on('click', function(){
            $('#search_input').focus();
            return false;
        });
    });

});

// Sidebar constructor
//
// -------------------
$(document).ready(function() {

    var sidebar = $('#sidebar');
    var sidebarHeader = $('#sidebar .sidebar-header');
    var sidebarImg = sidebarHeader.css('background-image');
    var toggleButtons = $('.sidebar-toggle');

    // Hide toggle buttons on default position
    // toggleButtons.css('display', 'none');
    $('body').css('display', 'table');


    // Sidebar position
    $('#sidebar-position').change(function() {
        var value = $( this ).val();
        sidebar.removeClass('sidebar-fixed-left sidebar-fixed-right sidebar-stacked').addClass(value).addClass('open');
        if (value == 'sidebar-fixed-left' || value == 'sidebar-fixed-right') {
            $('.sidebar-overlay').addClass('active');
        }
        // Show toggle buttons
        if (value != '') {
            toggleButtons.css('display', 'initial');
            $('body').css('display', 'initial');
        } else {
            // Hide toggle buttons
            toggleButtons.css('display', 'none');
            $('body').css('display', 'table');
        }
    });

    // Sidebar theme
    $('#sidebar-theme').change(function() {
        var value = $( this ).val();
        sidebar.removeClass('sidebar-default sidebar-inverse sidebar-colored sidebar-colored-inverse').addClass(value)
    });

    // Header cover
    $('#sidebar-header').change(function() {
        var value = $(this).val();

        $('.sidebar-header').removeClass('header-cover').addClass(value);

        if (value == 'header-cover') {
            sidebarHeader.css('background-image', sidebarImg)
        } else {
            sidebarHeader.css('background-image', '')
        }
    });
});

/**
 * Created by Kupletsky Sergey on 08.09.14.
 *
 * Add JQuery animation to bootstrap dropdown elements.
 */

(function($) {
    var dropdown = $('.dropdown');

    // Add slidedown animation to dropdown
    dropdown.on('show.bs.dropdown', function(e){
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    });

    // Add slideup animation to dropdown
    dropdown.on('hide.bs.dropdown', function(e){
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    });
})(jQuery);



(function(removeClass) {

	jQuery.fn.removeClass = function( value ) {
		if ( value && typeof value.test === "function" ) {
			for ( var i = 0, l = this.length; i < l; i++ ) {
				var elem = this[i];
				if ( elem.nodeType === 1 && elem.className ) {
					var classNames = elem.className.split( /\s+/ );

					for ( var n = classNames.length; n--; ) {
						if ( value.test(classNames[n]) ) {
							classNames.splice(n, 1);
						}
					}
					elem.className = jQuery.trim( classNames.join(" ") );
				}
			}
		} else {
			removeClass.call(this, value);
		}
		return this;
	}

})(jQuery.fn.removeClass);

