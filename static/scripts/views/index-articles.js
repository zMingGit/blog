define([
    'jquery',
    'underscore',
    'backbone',
    'common',
    'collections/index-articles'
], function($, _, Backbone, Common, IndexArticles){
    var IndexArticleView = Backbone.View.extend({
        tagName: 'tr',

        template: _.template($('#index-articles-tmpl').html()),

        initialize: function() {
            this.indexArticles = new IndexArticles();
            this.render();
        },

        render: function() {
            this.$el.html(this.template());
        },

        showIndexArticles: function() {
            var __this = this;
            this.indexArticles.fetch({
                cache: false,
                success: function() {
                },
                error: function(){
                    alert('please check network');
                }
            })
        },

        show: function() {
            this.showIndexArticles();
        }

    });
    return IndexArticleView
})
