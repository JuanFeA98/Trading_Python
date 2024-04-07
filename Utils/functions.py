import yfinance as yf

from plotly import graph_objects as go

def load_data(ticker, start_date, today_date):
    data = yf.download(ticker, start_date, today_date)
    data.reset_index(inplace=True)

    return data

def plot_raw_data(data):
    fig = go.Figure()
    
    # Agregamos el precio de apertura 
    fig.add_trace(
        go.Scatter(
            x = data['Date'],
            y = data['Open'],
            name = 'stock_open'
        )
    )

    # Agregamos el precio de cierre 
    fig.add_trace(
        go.Scatter(
            x = data['Date'],
            y = data['Close'],
            name = 'stock_close'
        )
    )

    # Configuramos el layout
    fig.layout.update(
        title_text = 'Time Series Data with Rangeslider',
        xaxis_rangeslider_visible = True
    )

    return fig