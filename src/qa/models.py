from src.base.base_models import BaseDateTimeModel
from src.extensions import db


class Section(db.Model):
    __tablename__ = 'sections'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    name = db.Column(db.Text(), nullable=False)
    order_number = db.Column(db.Integer, nullable=False)
    chapters = db.relationship('Chapter', back_populates='section')

    def __str__(self):
        return self.name


class Chapter(db.Model):
    __tablename__ = 'chapters'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    name = db.Column(db.Text(), nullable=False)
    order_number = db.Column(db.Integer, nullable=False)
    questions = db.relationship('Question', back_populates='chapter')
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))
    section = db.relationship(
        'Section', back_populates='chapters')


class Question(BaseDateTimeModel):
    __tablename__ = 'questions'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True)  # noqa: A003
    text = db.Column(db.Text(), nullable=False)
    order_number = db.Column(db.Integer, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    answers = db.relationship(
        'Answer', backref='questions', lazy='dynamic',
    )
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'))
    chapter = db.relationship(
        'Chapter', back_populates='questions')
    test_case = db.relationship(
        'TestCase', back_populates='question', uselist=False)

    def __str__(self):
        return f'Вопрос #{self.order_number} {self.text}'


class Answer(BaseDateTimeModel):
    __tablename__ = 'answers'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)  # noqa: A003
    text = db.Column(db.Text(), nullable=False)
    is_approve = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    likes_count = db.Column(db.Integer, default=0, nullable=False)
    user_relation = db.relationship(
        'AnswerUsersRelations',
        back_populates='answers',
    )


class AnswerUsersRelations(BaseDateTimeModel):
    __tablename__ = 'answer_users_relations'

    id = db.Column(db.Integer, primary_key=True)  # noqa: A003
    answer_id = db.Column(
        db.Integer,
        db.ForeignKey('answers.id'),
    )
    answers = db.relationship(
        'Answer',
        back_populates='user_relation',
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(
        'User',
        back_populates='answer_relation',
    )
