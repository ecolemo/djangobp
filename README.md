# Django BoilerPlate codes
The goal of djangobp is providing collection of common codes for django so that developers can skip boilerplate jobs.

## Installation
	git clone git@github.com:ecolemo/djangobp.git
	cd djangobp
	python setup.py install
	
## manage.py commands
### scaffoldapp
Scaffold app for quick start. 

	./manage.py startapp someapp
	djangobp-install
	./manage.py scaffoldapp someapp

This commands do these:

* Set up controllers for [Convention over Configuration](http://en.wikipedia.org/wiki/Convention_over_configuration) and set up urls for this. Routing works like this:
  * `/some_resource` -> index function in your_app/controllers/some_resource.py
  * `/some_resource/resource_id/some_function` -> some_function in your_app/controllers/some_resource.py
  * `/` -> index function in your_app/controllers/__init__.py 
* Register app to INSTALLED_APPS if not done
* Copy commonly used static files.
  * jQuery
  * twitter bootstrap
  * fancybox
  * etc
* Copy sample templates for mako. They are made on top of twitter bootstrap.

After do that, you can see initial page in [http://localhost:8000](http://localhost:8000).

## utils
* fixture
* httputil - bson encoder for mongodb
* mako render_to_response
* mongomodel

## ToDo
* clean up tests
* remove unused codes
* remove app specific codes
 
## Roadmap
* scaffold model
* install other apps
* pip & virtualenv support
* django-social-auth support
* install JavaScript libraries

