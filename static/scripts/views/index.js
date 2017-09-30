define([
    'jquery',
    'underscore',
    'backbone',
    'views/index-articles'
], function($, _, Backbone, IndexArticlesView){
    var IndexView = Backbone.View.extend({
        id: 'index',
        template: _.template($('#index-articles-tmpl').html()),

        initialize: function() {
            this.indexArticlesView =  new IndexArticlesView();
            this.render();
        },

        render: function() {
            this.$el.html(this.template());
        },


        show: function() {
            alert('go');
            this.indexArticlesView.show();
        }
    });
    return IndexView;
});
