from wtforms import (BooleanField, Form, HiddenField, PasswordField,
                     SelectField, StringField, validators)


class BaseForm(Form):
    class Meta:
        locales = ['ru']


class LoginForm(BaseForm):
    login = StringField(
        'Логин',
        [
            validators.input_required(),
            validators.length(
                min=3,
                max=15,
            ),
        ],
        render_kw={'autofocus': ''},
    )
    password = PasswordField('Пароль', [
        validators.data_required(),
        validators.length(
            min=6,
            max=15,
        ),
    ])


class RegistrationForm(BaseForm):
    login = StringField(
        'Логин',
        [
            validators.input_required(),
            validators.length(
                min=3,
                max=15,
            ),
        ],
        render_kw={'autofocus': ''},
    )
    password = PasswordField('Пароль', [
        validators.data_required(),
        validators.length(
            min=6,
            max=15,
        ),
    ])
    password_confirmation = PasswordField('Подтверждение пароля', [
        validators.data_required(),
        validators.equal_to('password', message='Пароли должны совпадать.'),
    ])
    email = StringField('Email адрес', [
        validators.email(),
        validators.data_required(),
        validators.length(
            min=4,
            max=100,
        ),
    ])
    lastname = StringField('Фамилия', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])
    firstname = StringField('Имя', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])
    middlename = StringField('Отчество', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])


class ResendEmailForm(BaseForm):
    email = StringField(
        'Email адрес',
        [
            validators.email(),
            validators.data_required(),
            validators.length(
                min=4,
                max=30,
            ),
        ],
        render_kw={'autofocus': ''},
    )


class ProfileOAuthForm(BaseForm):
    login = StringField(
        'Логин',
        [
            validators.input_required(),
            validators.length(
                min=3,
                max=15,
            ),
        ],
        render_kw={'autofocus': ''},
    )
    change_password = BooleanField('Сменить/установить пароль')
    password = PasswordField('Пароль', [
        validators.optional(),
        validators.length(
            min=6,
            max=15,
        ),
        validators.equal_to('password', message='Пароли должны совпадать.'),
    ])
    password_confirmation = PasswordField('Подтверждение пароля')
    email = StringField('Email адрес', [
        validators.email(),
        validators.data_required(),
        validators.length(
            min=4,
            max=100,
        ),
    ])
    lastname = StringField('Фамилия', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])
    firstname = StringField('Имя', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])
    middlename = StringField('Отчество', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])


class ProfileForm(BaseForm):
    email = StringField(
        'Email адрес',
        [
            validators.email(),
            validators.data_required(),
            validators.length(
                min=4,
                max=100,
            ),
        ],
        render_kw={'autofocus': ''},
    )
    lastname = StringField('Фамилия', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])
    firstname = StringField('Имя', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])
    middlename = StringField('Отчество', [
        validators.optional(),
        validators.length(
            min=1,
            max=30,
        ),
    ])


class ChangeAvatarForm(Form):
    chosen_avatar = SelectField('Ваш аватар', choices=[
        ('gravatar', 'обычный'),
        ('face', 'рожица'),
    ])
    default_avatar = BooleanField('Аватар по умолчанию')
    avatar_img_str = HiddenField('')
