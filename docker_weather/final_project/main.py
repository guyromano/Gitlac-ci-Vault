from flask import Flask, render_template, request
from templates.forcast_api import data_to_present

website = Flask(__name__)


@website.route('/result', methods=['POST'])
def data():
    """A page for the result, in case the API couldn't find the location,
    render the search page again with error message,
    otherwise render the date from the API"""
    user_input = request.form.get('u_input')
    location, forcast = data_to_present(user_input)
    if location:
        return render_template("result.html", location=location, forcast=forcast)
    error_msg = f"Sorry, couldn't find {user_input} location, please try another location."
    return render_template("search_bar.html", error=error_msg)


@website.route('/', methods=['POST', 'GET'])
def home():
    """A home page with the search engine"""
    return render_template("search_bar.html")


if __name__ == "__main__":
    website.run(host="0.0.0.0", port=5000, debug=True)
