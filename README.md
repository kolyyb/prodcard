# Objectifs visés
● Explorer un jeu de données et en expliquer ses caractéristiques

● Lire des données depuis une table d’une base de données avec SQL

● Réaliser un premier niveau d’analyses de données avec SQL

● Rendre compte des analyses en créant des graphiques avec Python

Durée estimée
2 heures.

## Énoncé du brief

### Scénario
Vous êtes développeur⸱se python, et une PME, cliente de l’entreprise spécialisée dans l’analyse de
données pour laquelle vous travaillez, souhaite mieux comprendre la dynamique de ses ventes afin
d’améliorer leur prise de décision stratégique.

Dans un premier temps, votre responsable technique vous demande de réaliser une analyse préalable afin
de mieux cadrer le projet final. Pour cela, le client vous a fourni un extrait de leur jeu de données des
ventes sur 20 jours.

Vous devez prendre connaissance du jeu de données et en comprendre ses principales caractéristiques.
Puis vous devez importer ce jeu de données dans une base de données en ligne puis requêter les données
et réaliser un premier niveau d’analyse des ventes avec SQL. Enfin vous devrez rendre compte de vos
conclusions en créant des graphiques avec Python.

### L’organisation de votre travail
1. Rendez-vous sur https://sqliteonline.com/. C’est un environnement bac à sable pour base de
données et SQL. Importez-y le jeu de données, renommez la table “ventes”.
2. Vérifiez que votre import a fonctionné en exécutant la requête SQL suivante : SELECT * FROM
ventes.
3. Créez les requêtes SQL pour répondre aux questions clés sur les ventes de l'entreprise :


   - a. le chiffre d'affaire total du 1er au 20 janvier 2022 :
   
   ```SQL
   SELECT c2, c3, SUM(c3) AS GLOBAL_CA FROM ventes;
   ```
| c2 | c3 | GLOBAL\_CA |
| :--- | :--- | :--- |
| produit | prix | 575 |

   - b. les ventes par produit du 1er au 20 janvier 2022 :

Le produit C s'est le mieux vendu avec 20 produits vendus.

Le produit A s'est le moins vendu avec 10 produits vendus.
   ```SQL
   SELECT c2, c3, SUM(c3) AS GLOBAL_CA_BY_PRODUCT FROM ventes GROUP BY c2;
   ```
| c2 | c3 | GLOBAL\_CA\_BY\_PRODUCT |
| :--- | :--- | :--- |
| Produit A | 10 | 140 |
| Produit B | 15 | 195 |
| Produit C | 20 | 240 |
| produit | prix | 0 |

   - c. les ventes par région :
   - les ventes ont été meilleures dans la région Nord du 1er au 20 janvier 2022

```SQL
SELECT c5, SUM(c3) AS GLOBAL_CA_BY_REGION FROM ventes GROUP BY c5;
```
| c5 | GLOBAL\_CA\_BY\_REGION |
| :--- | :--- |
| Nord | 295 |
| Sud | 280 |
| region | 0 |



6. En vous appuyant sur l’exemple donné, créer deux nouveaux graphiques :
   - a. les ventes par produit :
   
   <img height="300" src="/img/q_v_p.png" width="300"/>
   
   - b. le chiffre d'affaires par produit.

_Ressources associées_

● https://sql.sh/sgbd

● https://sqliteonline.com/

● https://plotly.com/python/plotly-express/

_**Livrables**_

● L’export SQL de vos requêtes (depuis le menu file > save SQL).

● Une fiche synthèse des résultats d’analyse obtenus (point 3.a, 3.b, 3.c).

● Le lien vers votre projet Glitch complété (point 6). *