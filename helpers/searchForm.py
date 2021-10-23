from flask_wtf import FlaskForm
from wtforms import StringField
class SearchForm(FlaskForm):
    search = StringField(
      render_kw={"placeholder": "Tell me your issue...", "required": True}, 
    )

