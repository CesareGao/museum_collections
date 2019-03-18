# analysis_of_museum_collections

## Team Member:

- Yan Gao
- Tianxin Deng

## Project Objective:

We gonna make a full analysis on the dataset of [The Metropolitan Museum of Art Open Access]( https://github.com/metmuseum/openaccess/ ). We intend to clean the missing document, duplicated data and letter-number mixed data in this data set. Then we plan to solve the problems like these:

- The proportion of different countries' collections changes with time, according to time and country.
- The cultural bloom era in each country, according to collection amount and time.
- The evidence of war or natural disaster, according to rapid decrease of production.

These are some patterns we want to analyze. We may modify them as the project proceeds. At last we will visualize the result with proper tools.

## Data Attributes:

- Object Number/Object ID: a unique number sequence for each object in museum.
- Is Highlight: a bool to show whether an object is highlighted or not.
- Is Public domain: a bool to show whether an object is displayed in public domain or not.
- Department: the department the object belongs to.
- Object name: how the object called.
- Title: detailed object name with discription.
- Culture/Period/Dynasty/Reign: the background of each object.
- Portfolio: the portfolio the object belongs to.
- Artist Pole/Artist Prefix/Artist Display Name/Artist Display Bio/Artist Suffix/Artist Alpha Sort/Artist Nationality/Artist Begin Date/Artist End Date: all detailed artist background.
- Object Date/Object Begin Date/Object End Date: the display period of each object.
- Medium: the materials using to made the items.
- Dimensions: the dimension of each object.
- Credit Line: the donators of each object.
- Classification: the category of material each objects belongs to.


## Tentative Timeline
Steps and Outlines | Roughly Time Estimate
------------------ | ---------------------
Data Cleanup | Set up Python process: 3 weeks
Data Cleanup | Debug and increasing effectiveness: 1 month
Transformation | written in PPT format : 1 week
Featuring Engineering | Get the results from Data Cleanup and dicussion: 2 weeks
Statistical Summary | Calculate the datas from step 1: 1 week
Visualization | Use the Calculation results, doing plot: 1 week

## Project Binder link
[analysis_of_museum_collections ]( https://mybinder.org/v2/gh/CesareGao/analysis_of_museum_collections/master?filepath=analysis_of_museum_collection.ipynb )

## Project Running result (HTML)
[analysis_of_museum_collections.html]( https://github.com/CesareGao/analysis_of_museum_collections/blob/master/analysis_of_museum_collection.html )
