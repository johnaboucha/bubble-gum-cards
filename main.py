from webbrowser import get
from flask import Flask, render_template, url_for
from helpers import get_categories, get_cards, get_next

app = Flask(__name__)

@app.route('/')
def root():
	categories = get_categories()
	cards = get_cards()
	has_next = get_next(10)

	return render_template('home.html', categories=categories, cards=cards, has_next=has_next, has_prev=False, next_page=2)

@app.route('/page/<int:page>')
def page(page):
	skip = (page - 1) * 9
	categories = get_categories()
	cards = get_cards(skip=skip)
	has_next = get_next(skip+1)
	next_page = page + 1
	prev_page = page - 1

	return render_template('home.html', categories=categories, cards=cards, has_next=has_next, has_prev=True, next_page=next_page, prev_page=prev_page)

@app.route('/category/<string:category>')
def category(category):
	return 'Category: ' + category

if __name__ == '__main__':
	app.run(debug=True)