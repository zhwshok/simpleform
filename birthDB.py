
from google.appengine.ext import ndb

class BirthDetails(ndb.Model):
    name =          ndb.StringProperty()
    date_of_birth = ndb.DateProperty()
    time_of_birth = ndb.TimeProperty()

