import os
from quickbooks import QuickBooks
from quickbooks.objects import Invoice

def fetch_quickbooks_data():
    qb_client = QuickBooks(
        client_id=os.getenv("QB_CLIENT_ID"),
        client_secret=os.getenv("QB_CLIENT_SECRET"),
        refresh_token=os.getenv("QB_REFRESH_TOKEN"),
        realm_id=os.getenv("QB_REALM_ID")
    )
    invoices = Invoice.query.select("*").all(qb=qb_client)
    result = []
    for inv in invoices:
        result.append({
            "id": inv.Id,
            "total": inv.TotalAmt,
            "txn_date": inv.TxnDate
        })
    return result