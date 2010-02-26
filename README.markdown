django-goodfields
=================

Customizing the markup of Django forms is a pain. django-goodfields tries to
make it hurt less by making it easy to render form fields and add inline
validation.

Requirements
------------

Field rendering only:

* Django 1.1+

Inline validation:

* jQuery
* LiveValidation

Installation
------------

### With Pip

    pip install -e hg+http://bitbucket.org/dwaiter/django-goodfields@stable#egg=django-goodfields
    
    # or...
    
    pip install -e git://github.com/dwaiter/django-goodfields@stable#egg=django-goodfields

### From Source

Get the code:

    hg clone http://bitbucket.org/dwaiter/django-goodfields/
    hg update stable
    
    # or...
    
    git clone git://github.com/dwaiter/django-goodfields/
    git checkout stable

Install:

    cd django-goodfields
    python setup.py install

Usage
-----

django-goodfields can help you render nice form fields, and optionally add
inline validation with Javascript.

### Field Rendering

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
type (`text`, `password`, `radio`, etc) has its own template. You can add new
field types by adding new templates.

Usage (Inline Validation)
-------------------------

