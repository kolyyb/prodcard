import plotly.express as px
import pandas as pd

src_file = 'csv/ventes.csv'
donnees = pd.read_csv(src_file)

# Rajout colonne 'ca_par_produit' qui contient le resultat du calcul  prix unitaire * quantite
donnees['ca_par_produit'] = donnees.qte * donnees.prix

def create_graph(donnees, values, names, title) :
    figure = px.pie(donnees, values=values, names=names, title=title)

    # TODO Creer nom fichier
    output_html = title.replace(' ', '_')
    figure.write_html(output_html + '.html')

    print(f"Graphique '{title}' généré avec succès !")


create_graph(donnees,'qte', 'region', 'quantite vendue par region')
create_graph(donnees,'qte', 'produit', 'quantite vendue par produit')
create_graph(donnees, 'ca_par_produit', 'produit', 'CA par produit')


# figure = px.pie(donnees, values='qte', names='region', title='quantité vendue par région')
# figure2 = px.pie(donnees, values='qte', names='produit', title='quantité vendue par produit')
# figure3 = px.pie(donnees, values='prix', names='produit', title='CA par produit')

# figure.write_html('ventes-par-region.html')
# figure2.write_html('ventes-par-produit.html')
# figure3.write_html('ca-par-produit.html')


# print('ventes-par-région.html généré avec succès !')
# print('vente-par-produit.html généré avec succès !')
# print('CA-par-produit.html généré avec succès !')
