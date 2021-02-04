from collections import defaultdict
from typing import Dict

from flask import Flask, request, jsonify

app = Flask(__name__)


def count(query_string: str) -> Dict[str, int]:
    """
    Takes a string and returns a dictionary with the counts of
    each individual character.

    >>> count('hi')
    {'h': 1, 'i': 1}

    >>> count('')
    {}

    >>> count("!")
    {'!': 1}
    """

    counts = defaultdict(lambda: 0)

    for char in query_string:
        counts[char] += 1

    return dict(counts)


@app.route('/')
def hello_world():
    """
    This endpoint takes a single querystring parameter, "query",
    And returns a JSON object with the counts for each individual character in the parameter

    """

    count_query = request.args.get('query')

    if count_query is None:
        return jsonify({"error": "Please specify a query parameter"}), 400

    return jsonify(count(count_query)), 200

