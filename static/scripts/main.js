require.config({
    paths: {
        //if jquery file name is jquery.js ,there is no need to exist here.
        'jquery': 'lib/jquery-3.2.1',
        'underscore': 'lib/underscore',
        'backbone': 'lib/backbone'
    },
    shim: {
        underscore: {
            exports: '_'
        },
        backbone: {
            deps:[
                'underscore',
                'jquery'
            ],
            exports: 'Backbone'
        }
    }
});

require(['./common'], function (common){
    require(['blog-main']);
})
