from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField(
        [DataRequired()],
        render_kw={"placeholder": "Tell me your issue..."}, 
    )

