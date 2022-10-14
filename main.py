from webbrowser import get
from flask import Flask, render_template, url_for, redirect
from helpers import get_categories, get_cards, has_next

app = Flask(__name__)

@app.route('/')
def root():
	return redirect('/page/1')

@app.route('/page/<int:page>')
def page(page):
	skip = (page - 1) * 9
	categories = get_categories()
	cards = get_cards(skip=skip)
	data = {}
	url = "https://2wf0rg.deta.dev/api/cards/?skip="+str(page*9)+"&top=1"
	data["has_next"] = has_next(url=url)
	data["next_page"] = "/page/"+str(page + 1)
	data["prev_page"] = "/page/"+str(page - 1)
	if page > 1:
		data["has_prev"] = True
	else:
		data["has_prev"] = False

	return render_template('home.html', categories=categories, cards=cards, data=data)


@app.route('/category/<string:category>/page/<int:page>')
def category(category, page):
	category = category.replace(" ", "%20")
	skip = (page - 1) * 9
	categories = get_categories()
	cards = get_cards(skip=skip, category=category)
	data = {}
	url = "https://2wf0rg.deta.dev/api/cards/?category="+category+"&skip="+str(page*9)+"&top=1"
	data["has_next"] = has_next(url=url)
	data["next_page"] = "/category/"+category+"/page/"+str(page + 1)
	data["prev_page"] = "/category/"+category+"/page/"+str(page - 1)
	if page > 1:
		data["has_prev"] = True
	else:
		data["has_prev"] = False

	return render_template('home.html', categories=categories, cards=cards, data=data)


if __name__ == '__main__':
	app.run(debug=True)