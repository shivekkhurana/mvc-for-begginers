%rebase('base.tpl', title='Landing')
<div class="hero-unit">
    <h1>Hello</h1>
    <p>{{real_name}} - <a href="/logout">Logout</a></p>
    <p>This is the super secret page that no one can access without logging in.</p>

    <div>
        <h3>Create a post</h3>
        <form action="/new-blog-post" method="POST">
            <label for="title">Title</label>
            <input type="text" name="title" id="title">

            <label for="body">Body</label>
            <input type="text" name="body" id="body">

            <input type="submit">
        </form>
        %if defined('errors'):
        <div class="errors">
            <ul>
            %for error in errors:
                <li>{{error}}</li>
            %end
            </ul>
        </div>
        %end
    </div>

    % if defined('posts'):
    <div class="posts">
        <ul>
        %for post in posts:
            <li>
                <h2>{{post[1]}}</h2>
                <p>{{post[2]}}</p>
            </li>
        %end
        </ul>
    </div>
    %end
</div>