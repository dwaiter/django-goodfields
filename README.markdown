django-goodfields
=================

Customizing the markup of Django forms is a pain. django-goodfields tries to
make it hurt less by making it easy to render form fields.

* Mercurial repo: <http://bitbucket.org/dwaiter/django-goodfields/>
* Git repo: <http://github.com/dwaiter/django-goodfields/>
* Issues: <http://github.com/dwaiter/django-goodfields/issues/>
* License: MIT/X11

Requirements
------------

* [Django][] 1.1+

[Django]: http://djangoproject.com/

Installation
------------

### With Pip

    pip install -e hg+http://bitbucket.org/dwaiter/django-goodfields#egg=django-goodfields
    # or...
    pip install -e git://github.com/dwaiter/django-goodfields#egg=django-goodfields

Now copy the sample templates into your project:

    cd yourproject
    cp -R /path/to/django-goodfields/goodfields/templates/goodfields/ templates/goodfields

### Or From Source

Get the code:

    hg clone http://bitbucket.org/dwaiter/django-goodfields/
    # or...
    git clone git://github.com/dwaiter/django-goodfields/

Install:

    cd django-goodfields
    python setup.py install

Now copy the sample templates into your project:

    cd yourproject
    cp -R /path/to/django-goodfields/goodfields/templates/goodfields/ templates/goodfields

Usage (Field Rendering)
-----------------------

Use the `{% goodfield [form.field] [field type] %}` template tag to render
fields in your form:

    <h1>Sign up for free!</h1>

    <form action="" method="post">

        {% load goodfields %}
        {% goodfield form.username text %}
        {% goodfield form.first_name text %}
        {% goodfield form.last_name text %}
        {% goodfield form.password password %}

        {{ form.non_field_errors }}
        <input type="submit" value="Sign Up" />
    </form>

The default field templates included with django-goodfields produce HTML that
looks similar to this:

    <div class="field" id="id_username-container">
        <label for="id_username">Username</label>
        <input type="text" class="text" id="id_username"
               name="username"
               value="" />
    </div>

Feel free to customize the templates to look however you prefer. Each field
type (`text`, `password`, `radio`, etc) has its own template in
`templates/goodfields`. You can add new field types by adding new templates.

django-goodfields will use the `label` attribute of the form field to create
the `<label>` element by default. You can specify a custom label for a
particular rendering of a field by using `label "new label"` in the
`{% goodfield %}` tag, like this:

    <form action="" method="post">
        {% load goodfields %}
        {% goodfield form.password password label "Pick a secure password!" %}
        <input type="submit" value="Sign Up" />
    </form>

You can also use the `class` keyword in the tag to pass a value along into the
template as the variable `class`.  This is intended to be used to specify CSS
classes:

    {% goodfield form.email text class "full-column" %}
    {% goodfield form.first_name text class "half-column" %}
    {% goodfield form.last_name text class "half-column" %}

