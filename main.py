from flask import Flask, render_template


app = Flask(__name__)


@app.errorhandler(404)
def error_404(e):
	return render_template('404.html'), 404


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/security')
def security():
	return render_template('security.html')


@app.route('/seo')
def seo():
	return render_template('seo.html')


@app.route('/analytics')
def analytics():
	return render_template('analytics.html')


if __name__ == '__main__':
	app.run(debug=True)
