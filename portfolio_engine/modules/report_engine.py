"""REPORT ENGINE"""

# sezione import

from tabulate import tabulate #libreria formattazione tabelle ASCII
from models.position import Position #classe
from models.portfolio import Portfolio #classe

# Funzione per creazione oggetto Position dai dati

def build_position_object(position_data):
    """
    crea un oggetto Position da un dict di dati calcolati
    - position_data: dizionario con i dati di una posizione da portfolio_logic
    - restituisce un oggetto Position    
    """
    position = Position(
        id = position_data["id"],
        ticker = position_data["ticker"],
        name = position_data["name"],
        type = position_data["type"],
        currency = position_data.get("currency", "EUR")
    )
    return position

# Funzione per creare oggetto Portfolio dai dati calcolati

def build_portfolio_object(portfolio_data):
    """
    Crea un oggetto Portfolio dai dati calcolati da portfolio_logic
    - portfolio_data: dizionario restituito da calculate_portfolio()
    - restituisce un oggetto Portfolio con tutte le posizioni e i totali    
    """
    #creo pf vuoto
    portfolio = Portfolio(
        total_value= portfolio_data["total_value"],
        total_cost= portfolio_data["total_cost"],
        pl_total_abs= portfolio_data["pl_total_abs"],
        pl_total_pct= portfolio_data["pl_total_pct"]
    )

    # converte e aggiunge ogni posizione
    for position_data in portfolio_data["positions"]:
        position = build_position_object(position_data)
        portfolio.add_position(position)

    return portfolio

# Funzione per stampare la tabella

def print_portfolio_table(portfolio):
    """
    Stampa una tabella formattata con tutte le posizioni del portafoglio.
    - portfolio: oggetto Portfolio con le posizioni    
    """
    headers = [
        "Ticker",
        "Nome",
        "Tipo",
        "Quantità",
        "Prezzo Medio",
        "Costo Totale",
        "Prezzo COrrente",
        "Valore Attuale",
        "P/L €",
        "P/L &",
        "Weight %"
    ]

    #costruzione dati per ogni riga
    rows = []
    for position in portfolio.position: