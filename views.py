from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from MongoIntegration.models import Image, ClothingFeature, User

clothes = Blueprint('posts', __name__, template_folder='templates')

class ClothingView(MethodView):

    def get(self):
        images = Image.objects.all()
        return render_template('clothing/list.html', images=images)


class ClothingUpdate(MethodView):
    
    def get(self, url):
        clothing_piece = Image.objects.get_or_404(url=url)
        return render_template('clothing/update.html', clothing=clothing_piece)

clothes.add_url_rule("/", view_func=ClothingView.as_view('list'))
clothes.add_url_rule("/<url>/", view_func=ClothingUpdate.as_view('update'))
        
