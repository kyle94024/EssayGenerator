# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash

def generate_essay(form_data):
  """Generate the essay given parameters"""
  return "{2} because {3}, and {4}".format(form_data["first_name"], form_data["last_name"], form_data["overall_argument"],form_data["first_para"], form_data["second_para"])


def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)
