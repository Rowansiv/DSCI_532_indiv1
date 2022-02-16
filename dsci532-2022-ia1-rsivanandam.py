from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

def plot_altair(xcol):
    chart = alt.Chart(iris).mark_point().encode(
        x=xcol,
        y='petal_length',
        tooltip='sepal_length').interactive()
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        dcc.Dropdown(
            id='xcol', value='sepal_length',
            options=[{'label': i, 'value': i} for i in iris.columns]),
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_altair(xcol='sepal_length'))])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol', 'value'))
def update_output(xcol):
    return plot_altair(xcol)
        
if __name__ == '__main__':
    app.run_server(debug=True)