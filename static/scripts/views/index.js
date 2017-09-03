define([
    'jquery',
    'underscore',
], function($, _){
    var IndexView = Bachbone.View.extend({
        id: 'index',

        template: _.template($('index-tmpl').html()),
    });
    return IndexView;
})
