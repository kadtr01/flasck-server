import psycopg2 as psycopg2
from flask import Flask, request
# create the Flask app
import config

app = Flask(__name__)

db_connection = psycopg2.connect(config.DB_URI, sslmode="require")
db_object = db_connection.cursor()

@app.route('/update-score')
def query_example():
    id = int(request.args.get("id"))
    score = int(request.args.get("score"))
    db_object.execute(f"UPDATE users SET score = {score} WHERE id = {id}")
    db_connection.commit()
    return 'ok'

# при запуске файла
if __name__ == "__main__":
    app.run(port=5000)
