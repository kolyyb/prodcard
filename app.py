import plotly.express as px
import pandas as pd

donnees = pd.read_csv('csv/ventes.csv')
sail_by_products = pd.read_csv('csv/ventes.csv')
ca_total = pd.read_csv('csv/ventes.csv')

figure = px.pie(donnees, values='qte', names='region', title='quantité vendue par région')
figure2 = px.pie(sail_by_products, values='qte', names='produit', title='quantité vendue par produit')
figure3 = px.pie(ca_total, values='prix', names='produit', title='CA par produit')

figure.write_html('ventes-par-region.html')
figure2.write_html('ventes-par-produit.html')
figure3.write_html('ca-par-produit.html')


print('ventes-par-région.html généré avec succès !')
print('vente-par-produit.html généré avec succès !')
print('CA-par-produit.html généré avec succès !')
