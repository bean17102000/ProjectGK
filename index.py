from flask import Flask, jsonify
import utils

app = Flask(__name__)

@app.route("/categories",methods=["GET"])
def get_categories():
    rows = utils.get_all("SELECT * FROM category")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "url": r[2]
        })

    return jsonify({"categories": data})

@app.route("/news",methods=["GET"])
def get_news():
    rows = utils.get_all("SELECT * FROM news")
    data= []
    for r in rows:
        data.append({
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "original_url": r[4]
        })

    return jsonify({"news":data})


@app.route("/news/<int:news_id>",methods=["GET"])
def get_news_by_id(news_id):
    pass

@app.route("/news/add",methods=["POST"])
def insert_news():
    pass
if __name__ == "__main__":
    app.run()