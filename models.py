import datetime
from MongoIntegration import db

class Image(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=False)
    url = db.StringField(required=True)
    metadata = db.ListField(db.EmbeddedDocumentField('ClothingFeature'))

    def __unicode__(self):
        return self.url + "<" + self.title + ">"

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created-at', 'url'],
        'ordering': ['-created-at']
    }

class ClothingFeature(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    value = db.DictField(required=True)

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=False)
    username = db.StringField(max_length=255, required=True)
    password = db.StringField(max_length=255, required=True)
    email = db.EmailField(max_length=255, required=True)
    is_staff = db.BooleanField(default=False, required=True)
    associated_company = db.StringField(default="Spool" required=True)
    
    
