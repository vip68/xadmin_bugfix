//===================
//  DOCUMENT READY JS
//===================
jQuery(document).ready(function() {
  'use strict';
      // OWL CAROUSELS //
    jQuery('.owl-carousel').owlCarousel({
      navigation: false,
      pagination: false,
      navigationText: [
      "<i class='pe-7s-angle-left'></i>",
      "<i class='pe-7s-angle-right'></i>"
      ], 
      autoPlay: 8000,
      loop: true
    });

    jQuery('.owl-carousel-paged').owlCarousel({
      navigation: false,
      pagination: false,
      autoPlay: 8000,
      loop: true
    });

    jQuery('#single-slider').owlCarousel({
      navigation: false,
      pagination: true,
      autoPlay: 8000,
      loop: true
    });
    
  /* RESPONSIVE VIDEOS */
  jQuery(".frame-wrapper").fitVids();

  /* LIGHTBOX */
  var magnificPopup = jQuery.magnificPopup.instance;
  jQuery('.lb-link, .image-gallery').magnificPopup({
    preloader:true,
    type: 'image',
    removalDelay: 300,
    mainClass: 'fadeInDown',
    callbacks: {
        open: function() {
          magnificPopup.content.addClass('mobile');
        }
      }
  });


  /* PRELOADER */
  Pace.on("done", function() {
    new WOW().init();
    $(window).trigger('resize');
  });

  /* NAVIGATION EFFECTS */
  $(function() {
    var headerNav = $(".nav-wrapper");
    $(window).scroll(function() {
      var scroll = $(window).scrollTop();
      if (scroll >= 360) {
        headerNav.removeClass('clearHeader').addClass("scrolled fadeInDown");
      } else {
        headerNav.removeClass("scrolled fadeInDown").addClass('clearHeader');
      }
    });
  });

  $('#testimonial-carousel').carousel({
    pause: true,
    interval: 10000
  });

  $('#music-carousel').carousel({
    interval: 10000
  })

  

  //CONTACT FORM
  $('#contactform').submit(function() {
    var action = $(this).attr('action');
    $("#message").slideUp(750, function() {
      $('#message').hide();
      $('#submit').attr('disabled', 'disabled');
      $.post(action, {
        name: $('#name').val(),
        email: $('#email').val(),
        website: $('#website').val(),
        comments: $('#comments').val()
      }, function(data) {
        document.getElementById('message').innerHTML = data;
        $('#message').slideDown('slow');
        $('#submit').removeAttr('disabled');
        if (data.match('success') != null) $('#contactform').slideUp('slow');
        $(window).trigger('resize');
      });
    });
    return false;
  });

  $('a.page-scroll').on('click', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: $($anchor.attr('href')).offset().top
    }, 1500, 'easeInOutExpo');
    event.preventDefault();
  });

  $("#home.food-slider").backstretch(["assets/images/food/food-slide-1.jpg", "assets/images/food/food-slide-1.jpg"], {
    duration: 6000,
    fade: 1200
  });  

  $("#home.business-slider").backstretch(["assets/images/business/business-slide-1.jpg", "assets/images/business/business-slide-2.jpg"], {
    duration: 6000,
    fade: 1200
  });  

  $("#home.fashion-slider").backstretch(["assets/images/fashion/fashion-slide-1.jpg", "assets/images/fashion/fashion-slide-2.jpg"], {
    duration: 6000,
    fade: 1200
  });  

  $("#home.backstretched").backstretch(["assets/images/home/slide-1.jpeg", "assets/images/home/slide-2.jpeg", "assets/images/home/slide-3.jpeg", ], {
    duration: 6000,
    fade: 1200
  });

  $("a[href*=#prev-slide]").on("click",function(event) {
      event.preventDefault(); 
      jQuery('#home.backstretched').data('backstretch').prev();
    });
  $("a[href*=#next-slide]").on("click",function(event) {
      event.preventDefault(); 
      jQuery('#home.backstretched').data('backstretch').prev();
  });

  $('.dropdown').on('show.bs.dropdown', function(e) {
    var $dropdown = $(this).find('.dropdown-menu');
    var orig_margin_top = parseInt($dropdown.css('margin-top'));
    $dropdown.css({
      'margin-top': (orig_margin_top + 10) + 'px',
      opacity: 0
    }).animate({
      'margin-top': orig_margin_top + 'px',
      opacity: 1
    }, 300, function() {
      $(this).css({
        'margin-top': ''
      });
    });
  });

  // Add slidedown & fadeout animation to dropdown
  $('.dropdown').on('hide.bs.dropdown', function(e) {
    var $dropdown = $(this).find('.dropdown-menu');
    var orig_margin_top = parseInt($dropdown.css('margin-top'));
    $dropdown.css({
      'margin-top': orig_margin_top + 'px',
      opacity: 1,
      display: 'block'
    }).animate({
      'margin-top': (orig_margin_top + 10) + 'px',
      opacity: 0
    }, 300, function() {
      $(this).css({
        'margin-top': '',
        display: ''
      });
    });
  });

  if ($('#back-to-top').length) {
    var scrollTrigger = 100, // px
        backToTop = function () {
            var scrollTop = $(window).scrollTop();
            if (scrollTop > scrollTrigger) {
                $('#back-to-top').addClass('show');
            } else {
                $('#back-to-top').removeClass('show');
            }
        };
    backToTop();
    $(window).on('scroll', function () {
        backToTop();
    });
    $('#back-to-top').on('click', function (e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: 0
        }, 700);
    });
  }

  function isotope_handler() {
    var masonry_portfolio_selectors = $('.masonry-portfolio-filter li a');
    var masonry_container = $('.masonry-portfolio .masonry-portfolio-items');

    if(masonry_portfolio_selectors!='undefined'){
        var masonry_portfolio = $('.masonry-portfolio-items');
        masonry_portfolio.imagesLoaded( function(){
             masonry_portfolio.isotope({
                itemSelector: '.masonry-portfolio-item',
                masonry: {
                  columnWidth: masonry_container.width() / 3
                }
            });
        });

        masonry_portfolio_selectors.on('click', function(e){
            e.preventDefault();
            masonry_portfolio_selectors.removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            masonry_portfolio.isotope({ filter: selector });
            return false;
        });
    }
  };

  isotope_handler();

  $('a.submenu-link').on('click', function(event){
    event.preventDefault();
    $(this).next().slideToggle();
  });
});
//===================
//  WINDOW LOADED JS
//===================
$(window).load(function() {
  'use strict';
  $('.match-height').matchHeight();
  $('.vertical-center-js').flexVerticalCenter({
    cssAttribute: 'padding-top'
  });
  $('#music-carousel').bind('slide.bs.carousel', function(e) {
    $(window).trigger('resize');
  });

  function toggleIcon(e) {
    $(e.target)
        .prev('.panel-heading')
        .toggleClass('panel-open');
        jQuery(window).trigger('resize').trigger('scroll');
  }
  $('.styled-accordion').on('hidden.bs.collapse', toggleIcon);
  $('.styled-accordion').on('shown.bs.collapse', toggleIcon);
  
  $('a#open-map').click(function(e) {
    e.preventDefault();
    $('#map-holder').slideToggle();
      $("#map-holder #mapwrapper").gMap({
      controls: false,
      scrollwheel: false,
      markers: [{
        latitude: 40.7566,
        longitude: -73.9863,
        icon: {
          image: "assets/images/marker.png",
          iconsize: [44, 44],
          iconanchor: [12, 46],
          infowindowanchor: [12, 0]
        }
      }],
      icon: {
        image: "assets/images/marker.png",
        iconsize: [26, 46],
        iconanchor: [12, 46],
        infowindowanchor: [12, 0]
      },
      latitude: 40.7566,
      longitude: -73.9863,
      zoom: 14,
      styles: [{"featureType":"all","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"all","elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#000000"},{"lightness":40}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#000000"},{"lightness":16}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":17},{"weight":1.2}]},{"featureType":"administrative.country","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"administrative.province","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"administrative.locality","elementType":"labels.text","stylers":[{"visibility":"on"}]},{"featureType":"administrative.neighborhood","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"administrative.land_parcel","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"landscape","elementType":"geometry.fill","stylers":[{"color":"#414039"},{"lightness":"-20"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":21}]},{"featureType":"poi","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"on"}]},{"featureType":"road","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#a59e93"},{"lightness":"0"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.highway","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"road.highway.controlled_access","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"road.arterial","elementType":"all","stylers":[{"visibility":"on"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":18}]},{"featureType":"road.arterial","elementType":"geometry.fill","stylers":[{"color":"#25241f"}]},{"featureType":"road.arterial","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"road.local","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":16}]},{"featureType":"road.local","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":19}]},{"featureType":"transit","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"transit.line","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"transit.station.airport","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"transit.station.bus","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#25241f"},{"lightness":17}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"color":"#25241f"}]}]
    });
    $('#contact-holder').slideUp();
  });
  $('a#open-contact').click(function(e) {
    e.preventDefault();
    $('#contact-holder').slideToggle();
    $('#map-holder').slideUp();
  });

    $('.pushy').mCustomScrollbar({
      theme:"minimal"
    });
});

//===================
//  OHTER JS
//===================
$(function() {
  'use strict';
  $('a.page-scroll').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var $target = $(this.hash);
      $target = $target.length && $target || $('[name=' + this.hash.slice(1) + ']');
      if ($target.length) {
        var targetOffset = $target.offset().top - 0;
        $('html,body').animate({
          scrollTop: targetOffset
        }, 800);
        return false;
      }
    }
  });
});

(function($) {
  'use strict';
  jQuery(window).load(function() {
    jQuery('.masonry').masonry({
      columnWidth: '.grid-sizer',
      gutter: '.gutter-sizer',
      itemSelector: '.item'
    });
  });
}(jQuery));