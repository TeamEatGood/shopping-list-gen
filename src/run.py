
from flask import Flask, jsonify
import datetime
from predict import shopping_list_for_household


app = Flask(__name__)

@app.route("/shopping-list/<int:customer>")
def shopping_list(customer):
    return jsonify({
                            "departments": shopping_list_for_household(2300, 247) 
                        })

if __name__ == '__main__':
    app.run(debug=True)