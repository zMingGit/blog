$(function(){
    $(".article-btn").click(function(){
        $article = $(this).parent().parent()
        link = '/api/article/?type=uuid&uuid=' + $article.attr('uuid');
        $(window).attr('location', link);
    });

    $("#search").click(function(){
        search_test = $("#search-text").val();
        link = '/search/?contains=' + search_test;
        $(window).attr('location', link);
        return false;
    })

})
