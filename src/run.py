
from flask import Flask, jsonify
import datetime


app = Flask(__name__)

@app.route("/shopping-list/<int:customer>")
def shopping_list(customer):
    return jsonify({
                            "departments": {
                                "PASTRY": [
                                    {
                                        "id": 312,
                                        "name": "COOKIES: HOLIDAY/SPECIAL OCCAS",
                                        "last_purchased": "2017-04-00T20:31:17.635554",
                                        "norm_interval": 5,
                                        "amount": 5
                                    },
                                    {
                                        "id": 315,
                                        "name": "BREAKFAST SWEETS,SW GDS:MUFFINS-LSS THN 6",
                                        "last_purchased": "2017-03-08T20:31:17.635554",
                                        "norm_interval": 3,
                                        "amount": 5
                                    }
                                ],
                                "NUTRITION": [
                                    {
                                            "id": 315,
                                            "name": "RASIN",
                                            "last_purchased": "2017-03-08T20:31:17.635554",
                                            "norm_interval": 20,
                                            "amount": 5
                                    }
                                ]
                            }
                        })

if __name__ == '__main__':
    app.run(debug=True)