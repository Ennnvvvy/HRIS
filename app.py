from flask import render_template

from hris import create_app

app = create_app()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template('413.html'), 413


# checks if the app.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True, threaded=True)