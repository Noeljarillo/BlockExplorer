#api proto
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_block(block_hash):
    conn = sqlite3.connect('../db/block1.db')
    c = conn.cursor()

    c.execute('''
    SELECT * FROM blocks WHERE hash = ?
    ''', (block_hash,))

    result = c.fetchone()

    conn.close()

    return result

def get_transaction(transaction_hash):
    conn = sqlite3.connect('../db/block1.db')
    c = conn.cursor()

    c.execute('''
    SELECT * FROM transactions WHERE transaction_data LIKE ?
    ''', ('%{}%'.format(transaction_hash),))

    result = c.fetchone()

    conn.close()

    return result

@app.route('/block/<block_hash>', methods=['GET'])
def block_route(block_hash):
    block = get_block(block_hash)
    if block is not None:
        return jsonify(block)
    else:
        return jsonify({"error": "Block not found"}), 404

@app.route('/transaction/<transaction_hash>', methods=['GET'])
def transaction_route(transaction_hash):
    transaction = get_transaction(transaction_hash)
    if transaction is not None:
        return jsonify(transaction)
    else:
        return jsonify({"error": "Transaction not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
