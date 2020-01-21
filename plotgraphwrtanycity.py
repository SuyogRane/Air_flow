import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv(r'new.csv')
a=input("Enter the origin city")
fig = go.Figure(go.Scatter(x = df['PASSENGERS_ON_WAY'], y = (df['AIRLINE_NAME']==a),
                  name='Share Prices (in USD)'))

fig.update_layout(title='airlines',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()
