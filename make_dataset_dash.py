import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def get_plot():
    from make_dataset import get_btc
    df = get_btc()
    from preprocess import preprocess_frame
    df = preprocess_frame(df)
    fig = px.line(df, df.index, "Value")
    fig.update_layout( xaxis = dict( rangeslider = {'visible': True}) )
    return df, fig

df, fig = get_plot()
df["Link"] = "[google](http://www.google.com)"
# df["Link"] = "Hello"
df["Date"] = df.index
print (df.head(2).to_dict('records'))

# https://dash.plotly.com/datatable/filtering
# Backend filtering with pandas and derived_filter_query_structure

import dash_table
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Graph(figure=fig),
    dcc.RangeSlider(
        id="my-range",
        min=0,
        max=len(df),
        step=1,
        value=[10, 20]
    ),
    html.Div(id='slider-output-container'),
    dash_table.DataTable(
        id="test-table",
        data=df.to_dict('records'),
        # [{'id': 1, 'name': 'Jhb'}],
        columns=[
            {
                'id': 'Link',
                'name': 'Link',
                'presentation': 'markdown'
            },
            {
                'id': 'Date',
                'name': 'Date',
            },
            {
                'id': 'Volume USD',
                'name': 'Volume USD',
            },
            {
                'id': 'Close',
                'name': 'Close',
            }
        ]
    )
])


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-range', 'value')])
def update_output(drange):
    print (drange)
    print (drange[0])
    start_date = df.index[drange[0]]
    end_date = df.index[drange[1]]
    return 'You have selected "{}:{},{}"'.format(drange, start_date, end_date)


if __name__ == '__main__':
    app.run_server(debug=True)
