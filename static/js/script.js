"use strict";

$(function () {



    // SIDEBAR //
  $(document).on("click", ".category_ul_main", function (e) {
    e.preventDefault();

    let dataId = $(this).attr("data-index");
    let currentUl = $(`.sub_category_ul_main[data-index = ${dataId}]`);
    let added = $(currentUl).hasClass("active");
    $(".sub_category_ul_main").removeClass("active");
    if(!(added)){
        $(currentUl).addClass("active");
    }else{
        $(currentUl).removeClass("active");
    }
  });

$(document).on("click", ".sidebar_header", function (e) {
    e.preventDefault();
    $(".sidebar_ul").toggleClass('active');
})


$(document).on('click', '.swiper-slide img', function () {
  let src = $(this).attr('src');
  $('.detail_img_box img').attr('src', src);
  console.log('clicked');
})

// ORDER CALL //

$(document).on('click', '.header_order_call', function (e) {
  e.preventDefault();
  $('.modal_order_call').addClass('active');

  $(document).on('click', '.modal_close_btn', function (e) {
    e.preventDefault();
    $('.modal_order_call').removeClass('active');
  })  
  
})

$(document).on('click', '.order__call', function (e) {
  e.preventDefault();
  $('.modal_order_call').addClass('active');

  $(document).on('click', '.modal_close_btn', function (e) {
    e.preventDefault();
    $('.modal_order_call').removeClass('active');
  })  
  
})


$(document).on('click', '.sidebar_faq a', function () {
  $('.sidebar_faq a').removeClass('active');
  $(this).addClass('active');
})

$(document).on('click', '.filter_head', function () {
  let dataId = $(this).attr('data-id');
let currentSub = $(`.filter_body[data-id = ${dataId}]`);

$(currentSub).toggleClass('active');
  
})


// **********************FILTER RANGE************************ //
$(document).on('click', '.filter_heading', function () {
  $('.filter_main_body').toggleClass('active');
  
})



var lowerSlider = document.querySelector('#lower');
var  upperSlider = document.querySelector('#upper');

document.querySelector('#two').value=upperSlider.value;
document.querySelector('#one').value=lowerSlider.value;

var  lowerVal = parseInt(lowerSlider.value);
var upperVal = parseInt(upperSlider.value);

upperSlider.oninput = function () {
    lowerVal = parseInt(lowerSlider.value);
    upperVal = parseInt(upperSlider.value);

    if (upperVal < lowerVal + 4) {
        lowerSlider.value = upperVal - 4;
        if (lowerVal == lowerSlider.min) {
        upperSlider.value = 4;
        }
    }
    document.querySelector('#two').value=this.value
};

lowerSlider.oninput = function () {
    lowerVal = parseInt(lowerSlider.value);
    upperVal = parseInt(upperSlider.value);
    if (lowerVal > upperVal - 4) {
        upperSlider.value = lowerVal + 4;
        if (upperVal == upperSlider.max) {
            lowerSlider.value = parseInt(upperSlider.max) - 4;
        }
    }
    document.querySelector('#one').value=this.value
}; 







});
