import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# ✅ Sample (dummy) data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 23, 15, 7],
    "Growth": [5, 12, 8, 3]
}
df = pd.DataFrame(data)

# ✅ Create charts
bar_chart = px.bar(df, x="Category", y="Values", title="Bar Chart - Category vs Values")
pie_chart = px.pie(df, names="Category", values="Values", title="Pie Chart - Distribution")
line_chart = px.line(df, x="Category", y="Growth", markers=True, title="Line Chart - Growth Trend")

# ✅ Initialize app
app = dash.Dash(__name__)

# ✅ Layout
app.layout = html.Div([
    html.H1("📊 Internship Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(figure=bar_chart)
    ], style={"width": "50%", "display": "inline-block"}),

    html.Div([
        dcc.Graph(figure=pie_chart)
    ], style={"width": "50%", "display": "inline-block"}),

    html.Div([
        dcc.Graph(figure=line_chart)
    ], style={"width": "100%", "display": "inline-block"})
])
# ✅ Run server
if __name__ == "__main__":
    app.run(debug=True)