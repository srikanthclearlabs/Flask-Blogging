from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class BlogEditor(Form):
    title = StringField("title", validators=[DataRequired()])
    title_image = StringField("title_image", validators=[DataRequired()])
    summary_text = TextAreaField("summary_text", validators=[DataRequired()])
    text = TextAreaField("text", validators=[DataRequired()])
    tags = StringField("tags")
    draft = BooleanField("draft", default=False)
    submit = SubmitField("submit")
