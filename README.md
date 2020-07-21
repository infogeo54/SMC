# SMC

Ce plugin permet d'effectuer une sélection de toutes les entités contenues au sein de couches choisies par l'utilisateur, et ceux sur toutes les couches du projet QGIS.

## Fonctionnement

### 1. Réglage de l'emprise

Avant de procéder à la sélection des entités, il est nécessaire de régler l'emprise de sorte à se concentrer uniquement sur les communes intéressantes.

Il n'est pas nécessaire de contenir la totalité de la ou des communes au sein de l'emprise : il suffit simplement qu'une partie ou seulement la délimitation d'une commune soit contenue dans l'emprise courante pour qu'elle soit prise en compte.

### 2. Utilisation de l'extension

Arpès avoir réglé l'emprise, il suffit de lancer l'extension.

Il est alors nécessaire d'indiquer à l'extension les noms des communes sur lesquelles vous souhaiter effectuer la sélection des entités.

Pour ajouter une commune à la liste depuis laquelle l'extension procèdera à la sélection, il suffit de cocher la case à côté du nom de la commune en question.

### 3. Sélection

En cliquant sur le bouton `valider`, l'extension se charge de passer en revue la totalité des couches du projet afin de repérer les entités contenues au sein des communes choisies. Ces dernières sont alors ajoutées à la sélection globale.

Notez que le temps de traitement est proportionnel au nombre d'entités présentes dans le projet QGIS. La sélection peut alors prendre quelques secondes dans le cas d'un projet de grande envergure.