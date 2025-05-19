from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("comp_with_states.csv")

data = df.to_dict(orient="records")

@app.route("/api/companies", methods=["GET"])
def get_companies():
    return jsonify(data)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)

