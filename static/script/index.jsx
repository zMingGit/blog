import React from 'react';
import { render } from 'react-dom';
import { PostObject } from './common.jsx';

ReactDOM.render(
    <PostObject post_image="text" post_url="test" post_title="test" post_body="text" post_avatar="avatar" post_auth="test_auth" post_time="test" post_category="test" />,
    document.getElementById('blog')
);