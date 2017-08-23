define([
    'jquery',
    'lib/backbone',
    'common',
    'views/index',
    'views/article'
], function($, Backbone, Common, Index, Article){
    "use strict";

    var Router = Backbone.Router.extend({
        router: {
            '': 'showIndex',
            '*actions': 'showIndex'
        },

        initialize: function(){
            //Common.prepareApiCsrf();
            this.index = Index();
        },

        showIndex: function(){
           this.index.show(); 
        }
    });

    return Router;
})
