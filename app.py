import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Cargar los datos
file_path = "data/DataTransacciones_PruebasIngreso.xlsx"
xls = pd.ExcelFile(file_path)
comercios = pd.read_excel(xls, sheet_name="comercios")
transacciones = pd.read_excel(xls, sheet_name="transacciones")

# Procesar los datos
comercios["Monto ventas Acumulado"] = pd.to_numeric(comercios["Monto ventas Acumulado"])
comercios["Monto ventas ultimo mes"] = pd.to_numeric(comercios["Monto ventas ultimo mes"]) 
transacciones["cantidad transacciones"] =pd.to_numeric(transacciones["cantidad transacciones"])
comercios = comercios.merge(
    transacciones.groupby("Id_comercio", as_index=False)["cantidad transacciones"].sum(),
    on="Id_comercio",
    how="left"
)

# Normalizar los datos
scaler = StandardScaler()
features = ["Monto ventas Acumulado", "Monto ventas ultimo mes", "cantidad transacciones"]
comercios_scaled = scaler.fit_transform(comercios[features])

# Aplicar K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
comercios["Cluster"] = kmeans.fit_predict(comercios_scaled)

# Crear la app Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Segmentación de Comercios"),
    dcc.Dropdown(
        id="cluster-selector",
        options=[{"label": f"Cluster {i}", "value": i} for i in range(4)],
        multi=True,
        value=[0, 1, 2, 3],
        placeholder="Seleccionar Clusters"
    ),
    dcc.Graph(id="scatter-plot")
])

@app.callback(
    Output("scatter-plot", "figure"),
    Input("cluster-selector", "value")
)
def update_graph(selected_clusters):
    filtered_df = comercios[comercios["Cluster"].isin(selected_clusters)]
    fig = px.scatter(filtered_df, x="Monto ventas Acumulado", y="Monto ventas ultimo mes",
                     color=filtered_df["Cluster"].astype(str), hover_data=["Id_comercio"])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8050)
