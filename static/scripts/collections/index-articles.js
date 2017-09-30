define([
    'underscore',
    'backbone',
    'common',
    'models/index-article',
], function(_, Backbone, Common, IndexArticle){
    'use strice';

    var IndexArticleCollection = Backbone.Collection.extend({
        model: IndexArticle,

        url: function(option) {
            return Common.getUrl({name: 'index_articles'}) + "?type=" + option;
        },

    });

    return IndexArticleCollection;
});
