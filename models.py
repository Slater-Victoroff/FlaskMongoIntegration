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
    key = db.StringField(max_length=255, required=True)
    value = db.StringField(required=True)

    
