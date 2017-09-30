define([
    'jquery',
    'underscore',
], function($, _) {
    return {
        getUrl: function(options) {
            var siteRoot = blog.config.siteRoot;
            switch (options.name) {
                case 'index_articles': return siteRoot + 'api/endpoints/index_articles';
            }
        }
    }
})
