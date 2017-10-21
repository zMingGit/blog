$(function(){
    $(".article-btn").click(function(){
        link = '/api/article/?type=uuid&uuid=' + $(this).attr('uuid');
        $(window).attr('location', link);
    });
})
