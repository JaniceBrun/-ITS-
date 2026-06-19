"""REPORT ENGINE"""

# sezione import

from tabulate import tabulate #libreria formattazione tabelle ASCII
from models.position import Position #classe
from models.portfolio import Portfolio #classe

# Funzione per creazione oggetto Position dai dati

def build_position_object(position_data: dict):
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

def build_portfolio_object(portfolio_data:dict):
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

def print_portfolio_table(portfolio: Portfolio):
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
        "Prezzo Corrente",
        "Valore Attuale",
        "P/L €",
        "P/L %",
        "Weight %"
    ]

    #costruzione dati per ogni riga
    rows = []
    for position in portfolio.positions:
        position: Position
        rows.append([
            position.ticker,
            position.name,
            position.type.upper(),
            f"{position.quantity:.0f}",
            f"€ {position.avg_price:.2f}",
            f"€ {position.total_cost:.2f}",
            f"€ {position.current_price:.2f}",
            f"€ {position.current_value:.2f}",
            f"€ {position.pl_abs:.2f}",
            f"{position.pl_pct:.2f}%",
            f"{position.weight_pct:.2f}%"            
        ])

    # stampa tabella
    print("\n" + "="*140)
    print(f"PORTAFOGLIO - Valore totale: € {portfolio.total_value:.2f}")
    print("="*140 + "\n")
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print("\n" + "="*140)
    print(f"TOTALI | Costo: € {portfolio.total_cost:.2f} | Valore: € {portfolio.total_value:.2f} | P/L: € {portfolio.pl_total_abs:.2f} ({portfolio.pl_total_pct:.2f}%)")
    print("="*140 + "\n")    

    #funzione principale orchestratrice

def generate_report(portfolio_data: dict) -> None:
    """
    Genera un report completo del portafoglio
    Orchestratore principale del report_engine.
    - portafolio_data: dict restituito da portfolio_logic.calculare_portfolio()
    """
    #converte i dati in oggetti OOP
    portfolio = build_portfolio_object(portfolio_data)

    #stampa report
    print_portfolio_table(portfolio)