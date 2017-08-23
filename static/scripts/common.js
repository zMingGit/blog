require.config({
    paths: {
        //if jquery file name is jquery.js ,there is no need to exist here.
        jquery: 'lib/jquery-3.2.1',
        underscore: 'lib/underscore'
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
        }
    }
});
