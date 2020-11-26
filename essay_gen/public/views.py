# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from essay_gen.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")

@blueprint.route("/")
def home():
    """Home page."""
    return render_template("public/index.html")

@blueprint.route("/about/")
def about():
    """About page."""
    return render_template("public/about.html")

@blueprint.route("/error/")
def error():
  """500 Error page"""
  return 1/0