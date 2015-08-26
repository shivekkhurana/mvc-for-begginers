%rebase('base.tpl', title='Landing')
<div class="hero-unit">
    <h1>Login</h1>
    <form action="/login" method="POST" id="login">
        <label for="username">Username</label>
        <input type="text" name="username" id="name"/>
        
        <label for="password">Password</label>
        <input type="password" name="password" id="password"/>

        <input type="submit" />
    </form>

    %if defined('errors'):
    <div class="errors">
        <ul>
        %for error in errors:
            <li>{{error}}</li>
        %end
        </ul>
    </div>
</div>