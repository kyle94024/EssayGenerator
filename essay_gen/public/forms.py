# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class GenForm(FlaskForm):
    """The form used to supply the values of the generation questions."""

    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    overall_argument = StringField("What is your overall argument?", validators=[DataRequired()])
    first_para = StringField("What is the first paragraph going to be about?", validators=[DataRequired()])
    second_para = StringField("What is the second paragraph going to be about?", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(GenForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(GenForm, self).validate()
        if not initial_validation:
            return False
        return True
