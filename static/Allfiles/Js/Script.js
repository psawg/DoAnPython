$(function () {

    console.log("SCRIPT.JS LOADED");

    $("#checkForm").on("submit", function (e) {

        e.preventDefault();

        console.log("AJAX RUNNING");

        $.ajax({

            url: "/check-availability/",
            type: "POST",

            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),

                check_in: $("#check_in").val(),
                check_out: $("#check_out").val(),

                adults: $("select[name=adults]").val(),
                children: $("select[name=children]").val()
            },

            success: function (response) {

                console.log("AJAX SUCCESS");

                sessionStorage.setItem(
                    "check_in",
                    $("#check_in").val()
                );

                sessionStorage.setItem(
                    "check_out",
                    $("#check_out").val()
                );

                sessionStorage.setItem(
                    "adults",
                    $("select[name=adults]").val()
                );

                sessionStorage.setItem(
                    "children",
                    $("select[name=children]").val()
                );


                $("#roomTableBody").html(response);

                $("#roomModal").fadeIn();
            },

            error: function (xhr, status, error) {

                console.log("AJAX ERROR");
                console.log(xhr.responseText);
                console.log(error);
            }
        });

        return false;
    });

    $(document).on("click", ".room-close", function () {
        $("#roomModal").fadeOut();
    });

    //slide part js
    $('.late').textillate({
        loop: true,
        minDisplayTime: 3000,
        initialDelay: 1000,
        in: {
            effect: 'bounceInDown',
            delayScale: 2,
        },
        out: {
            effect: 'bounce',
            delayScale: 1,
            shuffle: true,
        },
    });

    //slide part js
    $('#slider').slick({
        dots: false,
        autoplay: true,
        autoplaySpeed: 5000,
        prevArrow: '.pre_btn',
        nextArrow: '.next_btn',
    });

    //Book A Table Area js
    $('.Check_in').datetimepicker({
        formatTime: 'H:i:i',
        formatDate: 'd.m.Y',
        theme: 'dark',
        step: 30,
        hours12: false,
    });

    $('.open').click(function () {
        $('.Check_in').datetimepicker('show');
    });

    $('.Check_out').datetimepicker({
        formatTime: 'H:i:i',
        formatDate: 'd.m.Y',
        theme: 'dark',
        step: 30,
        hours12: false,
    });

    $('.open1').click(function () {
        $('.Check_out').datetimepicker('show');
    });

    // about part js
    $(".video_btn").modalVideo({
        theme: 'dark',
    });

    // EXPLOR OUR ROOMS js
    $('.room_slide').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 3,
        slidesToScroll: 2,
        dots: true,
        arrows: false
    });

    //OUR AWESOME SERVICES js
    $('#example').tabs({
        delay: 500,
    });

    //OUR GALLERY js
    $('.gallary_overly').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true,
            tPrev: 'Gallery_pre',
            tNext: 'Gallery_next',
        },
    });

    $('.GALLERY_slider').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 4,
        slidesToScroll: 2,
        dots: true,
        arrows: false
    });

    //Our Special Staff Part start
    $('.Staff_slider').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 4,
        slidesToScroll: 2,
        dots: true,
        arrows: false
    });

    //counter part js
    $('.counter').counterUp({
        delay: 5,
        time: 1000,
    });

});