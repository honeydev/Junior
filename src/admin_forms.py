from http import HTTPStatus

from flask import abort, session
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'  # noqa WPS336
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)  # noqa WPS608


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class QAWYSIWYG(ModelView):
    extra_js = ['https://cdn.ckeditor.com/4.13.0/standard/ckeditor.js']

    form_overrides = {
        'text': CKTextAreaField,
    }
    form_excluded_columns = ['test_questions', 'user_relation', 'answers']


class TestQuestionView(QAWYSIWYG):
    form_choices = {
        'question_type': [
            ('0', 'RADIUS'),
            ('1', 'CHECK_BOX'),
        ],
    }


class CustomAdminView(AdminIndexView):
    @expose('/')
    def index(self):
        sess = session.get('auth')
        user = getattr(sess, 'user', None)
        if user and sess and user.is_superuser:
            return super(CustomAdminView, self).index()  # noqa WPS608
        else:
            abort(int(HTTPStatus.LOCKED))
