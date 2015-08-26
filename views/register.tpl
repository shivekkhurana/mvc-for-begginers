%rebase('base.tpl', title='Landing')
<div class="hero-unit">
    <h1>Register</h1>
    <form action="/register" method="POST" id="register">
        <label for="real-name">Real Name</label>
        <input type="text" name="real-name" id="name"/>

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