import django
import webapp2
import birthDB
from django.conf import settings
from google.appengine.ext.webapp import template
from django import forms
from django.forms import models

settings.configure(debug=True)
django.setup()

class BirthDetailsForm(forms.Form):
    class Meta:
        model = birthDB.BirthDetails

class SimpleInput(webapp2.RequestHandler):
    def get(self):
        html = template.render('templates/header.html', {'title': 'Provide your birth details'})
        html = html + template.render('templates/form_start.html', {})
        html = html + str(BirthDetailsForm(auto_id=False))
        html = html + template.render('templates/form_end.html', {'sub_title': 'Submit Details'})
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

application = webapp2.WSGIApplication([('/', SimpleInput)], debug=True)
