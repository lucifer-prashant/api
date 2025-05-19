from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("comp.csv")

data = df.to_dict(orient="records")

@app.route("/api/companies", methods=["GET"])
def get_companies():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
