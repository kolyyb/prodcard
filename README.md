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
<img height="300" src="/img/ventes_sql.png" width="350"/>

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


   - ### **a. le chiffre d'affaire total du 1er au 20 janvier 2022 :**
   
   ```SQL
SELECT c2 as Produits, sum(c3 * c4) as CA_Global FROM ventes;
   ```
| Produits | CA\_Global |
| :--- | :--- |
| produit | 44825 |


   - **b. les ventes par produit du 1er au 20 janvier 2022 :**

Le produit C s'est le mieux vendu avec 20 produits vendus.

Le produit A s'est le moins vendu avec seulement 10 produits vendus.
   ```SQL
SELECT c2 as Produits, c3 as prix_unitaire, c4 as quantite, sum(c3 * c4) as CA_by_Produit FROM ventes
GROUP BY c2;
   ```
| produit | ca\_by\_produit |
| :--- | :--- |
| Produit A | 17500 |
| Produit B | 15825 |
| Produit C | 11500 |
| produit | 0 |


   ## **- c. les ventes par région :**
   - les ventes ont été meilleures dans la région Nord du 1er au 20 janvier 2022

```SQL
SELECT c5 as Region, sum(c3 * c4)  as CA_by_Region  FROM ventes
group by c5;
```
| Region | CA\_by\_Region |
| :--- | :--- |
| Nord | 20725 |
| Sud | 24100 |
| region | 0 |



6. En vous appuyant sur l’exemple donné, créer deux nouveaux graphiques :
   - **a. les ventes par produit :**
   
   <img height="300" src="/img/q_v_p.png" width="300"/>
   
   - **b. le chiffre d'affaires par produit :**
   - 
   <img height="300" src="/img/q_ca_p.png" width="350"/>

 - **c. le chiffre d'affaire par produit :**
