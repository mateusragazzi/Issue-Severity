from flask import render_template
from helpers.searchForm import SearchForm

class SearchController():
  def processInput(form):
    return {
        "result": "major", 
        "accuracy": 65.2, 
        "words": [
          {"tag": "Teste", "weight": 4},
          {"tag": "Teste", "weight": 6}, 
          {"tag": "Teste", "weight": 21}, 
          {"tag": "Teste", "weight": 10}, 
          {"tag": "Teste", "weight": 5}, 
          {"tag": "Teste", "weight": 8},
          {"tag": "Teste", "weight": 15}, 
          {"tag": "Teste", "weight": 123}, 
          {"tag": "Teste", "weight": 16}, 
          {"tag": "Teste", "weight": 2}, 
        ]
      }

  @staticmethod
  def render():
    form = SearchForm()

    if form.validate_on_submit():
      result = SearchController.processInput(form)
      return render_template(
        "result/index.jinja2",
        result=result
    )

    return render_template(
        "search/index.jinja2",
        form=form
    )
