from hashlib import md5

from flask import Blueprint, current_app, render_template, session
from flask.views import MethodView
from sqlalchemy import null

from src.qa.models import Chapter, Section
from src.user import User

bp: Blueprint = Blueprint('index', __name__, template_folder='templates')


class BaseView(MethodView):

    def __init__(self, template_name):
        self.context = {
            'auth': session.get('auth'),
            'app_name': current_app.config['APP_NAME'],
        }
        self.template_name: str = template_name

    def avatar(self, size, image_str):
        digest = md5(image_str.encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{0}?d=identicon&s={1}'.format(
            digest, size)


class HomePage(BaseView):

    def __init__(self, template_name):
        super().__init__(template_name)

    def get(self):

        return render_template(self.template_name, **self.context)


class IndexPage(BaseView):

    def __init__(self, template_name):
        super().__init__(template_name)

    def get(self, section_id: int):
        section = Section.query.get(section_id)

        self.context.update(
            dict(
                chapters=Chapter.query.filter(Chapter.section_id == section.id),
            ),
        )

        if self.context['auth']:
            auth = self.context['auth']
            user_email = auth.user.email
            user_image = auth.user.image
            if not user_image:
                avatar_str = user_email
                User.query.filter_by(id=auth.user.id).update(
                    {'image': user_email},
                )
            else:
                avatar_str = user_image
            self.context['avatar'] = self.avatar(48, avatar_str)

        return render_template(self.template_name, **self.context)


class NotFoundPage(BaseView):

    def get(self):
        return render_template(self.template_name, **self.context)


bp.add_url_rule(
    '/',
    view_func=HomePage.as_view(name='home', template_name='home.jinja2'),
)


bp.add_url_rule(
    '/<int:section_id>',
    view_func=IndexPage.as_view(name='index', template_name='index.jinja2'),
)

bp.add_url_rule(
    '/',
    view_func=IndexPage.as_view(name='404', template_name='404.jinja2'),
)
