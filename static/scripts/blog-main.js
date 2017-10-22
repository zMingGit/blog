$(function(){
    $(".article-btn").click(function(){
        link = '/api/article/?type=uuid&uuid=' + $(this).attr('uuid');
        $(window).attr('location', link);
    });

    $("#search").click(function(){
        search_test = $("#search-text").val();
        link = '/search/?contains=' + search_test;
        $(window).attr('location', link);
        return false;
    })

})
