from flask_wtf import FlaskForm
from flask import (url_for, render_template, redirect)
from helpers.searchForm import SearchForm

class SearchController():

  @staticmethod
  def render():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for("result"))

    return render_template(
        "search/index.jinja2",
        form=form
    )
