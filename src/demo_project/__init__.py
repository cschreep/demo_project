from collections import defaultdict
from typing import Dict

from flask import Flask, request, jsonify

app = Flask(__name__)


def count(query_string: str) -> Dict[str, int]:
    counts = defaultdict(lambda: 0)

    for char in query_string:
        counts[char] += 1

    return dict(counts)


@app.route('/')
def hello_world():
    count_query = request.args.get('query')

    if count_query is None:
        return jsonify({"error": "Please specify a query parameter"}), 400

    return jsonify(count(count_query)), 200

