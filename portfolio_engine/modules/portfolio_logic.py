#import funzioni necessarie
from db.dbmanager import (
    get_all_positions,
    get_position_summary,
    get_latest_price,
    add_price_snapshot,
    get_position_by_ticker,
    get_price_by_date
)
from modules.market_api import get_all_prices

def calculate_position(position, summary, current_price, previous_price=None, previous_date=None):
    """
    Calcola tutti i valori economici di una singola posizione.
    - position: dizionario con i dati statici da positions
    - summary: dizionario con total_quantity, avg_price, total_cost da purchases
    - current_price: prezzo corrente da yfinance
    - previous_price: ultimo prezzo salvato in price_history (opzionale)
    - previous_date: data a cui si riferisce il previous_price (opzionale, solo per info)
    - restituisce un dizionario con tutti i valori calcolati
    """
    # dati base
    quantity    = summary["total_quantity"]
    avg_price   = summary["avg_price"]
    total_cost  = summary["total_cost"]

    # calcolo valore attuale
    current_value = round(current_price * quantity, 2)

    # calcolo P/L assoluto e percentuale
    pl_abs  = round(current_value - total_cost, 2)
    pl_pct  = round((pl_abs / total_cost) * 100, 2)

    # calcolo delta rispetto all'ultimo prezzo salvato
    if previous_price and previous_price > 0:
        delta_abs = round(current_price - previous_price, 4)
        delta_pct = round((delta_abs / previous_price) * 100, 2)
    else:
        #nessun prezzo precendente disp
        delta_abs = None
        delta_pct = None

    return {
        "ticker":         position["ticker"],
        "name":           position["name"],
        "type":           position["type"],
        "quantity":       quantity,
        "avg_price":      round(avg_price, 4),
        "total_cost":     round(total_cost, 2),
        "current_price":  current_price,
        "current_value":  current_value,
        "pl_abs":         pl_abs,
        "pl_pct":         pl_pct,
        "delta_abs":      delta_abs,
        "delta_pct":      delta_pct,
        "previous_date":  previous_date,        
    }