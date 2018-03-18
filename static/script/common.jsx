export class PostHead extends React.Component {
    render() {
        return (
            <div className="post_thumbnail-custom mdl-card__media mdl-color-text--grey-50 lazy" data-original="https://cdn.viosey.com/img/blog/netease_music.png!blogthumbnail">
            <p className="article-headline-p"><a href={this.props.post_url}>{this.props.post_title}</a></p>
            <img src={this.props.post_image} />
            </div>
        );
    }
}

export class PostBody extends React.Component {
    render() {
        return (
            <div className="mdl-color-text--grey-600 mdl-card__supporting-text post_entry-content">
                {this.props.post_body}
            </div>
        );
    }
}

export class PostFoot extends React.Component {
    render() {
        return (
           <div id="post_entry-info">
                <div id="post_entry-left-info" className="mdl-card__supporting-text meta mdl-color-text--grey-600">
                    <div id="author-avatar">
                        <img src={this.props.post_avatar} width="44px" height="44px" alt={this.props.post_avatar_alt}/>
                    </div>
                    <div>
                        <strong>{this.props.post_auth}</strong> <span>{this.props.post_time}</span>
                    </div>
                </div>
                <div id="post_entry-right-info"><span className="post_entry-category">
                    <a className="post_category-link" href={this.props.post_category_url}>{this.props.post_category}</a>
                    </span>
                        <span className="post_entry-views">
                    </span>
                </div>
            </div>
        );
    }
}

export class PostObject extends React.Component {
    renderPostHead(post_image, post_url, post_title) {
        return <PostHead post_url={post_url} post_image={post_image} post_title={post_title} />;
    }
    renderPostBody(post_body) {
        return <PostBody post_body={post_body} />;
    }

    renderPostFoot(post_avatar, post_auth, post_time, post_category){
        var post_category_url = "/categorys/" +  post_category;
        var post_avatar_alt = post_avatar + "'s avatar";
        return <PostFoot post_avatar={post_avatar} post_auth={post_auth} post_time={post_time} post_category={post_category} />;
    }

    render() {
        return (
            <div>
                {this.renderPostHead(this.props.post_image, this.props.post_url, this.props.post_title)}
                {this.renderPostBody(this.props.post_body)}
                {this.renderPostFoot(this.props.post_avatar, this.props.post_auth, this.props.post_time, this.props.post_category)}
            </div>
        )
    }
}