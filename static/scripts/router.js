define([
    'jquery',
    'backbone',
    'common',
    'views/index',
], function($, Backbone, Common, IndexView){
    "use strict";

    var Router = Backbone.Router.extend({
        routes: {
            '': 'showIndex',
            'index': 'showIndex',
            '*actions': 'showIndex'
        },

        initialize: function(){
            //Common.prepareApiCsrf();
            this.indexView = new IndexView();
            this.indexView.show();
        },

        showIndex: function(){
            this.indexView.show();
        },

    });

    return Router;
});
