from flask import Blueprint

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/')
def list_transactions():
    return "List of transactions"
