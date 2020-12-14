# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    render_template,
    request,
    flash
)
from .forms import GenForm
from essay_gen.utils import flash_errors, generate_essay

blueprint = Blueprint("public", __name__, static_folder="../static")

@blueprint.route("/")
def home():
    """Home page."""
    return render_template("public/index.html")

@blueprint.route("/generator/", methods=["GET", "POST"])
def generator():
    """Page that renders our generator form"""
    form = GenForm(request.form)
    if form.validate_on_submit():
        essay = generate_essay(form.data)
        flash("Thank you for filling the form {}!".format(form.first_name.data), "success")
        return render_template("public/generator.html", form=form, essay=essay)
    else:
        flash_errors(form)
    return render_template("public/generator.html", form=form)

@blueprint.route("/about/")
def about():
    """About page."""
    return render_template("public/about.html")

@blueprint.route("/error/")
def error():
  """500 Error page"""
  return 1/0