# Analysis of Museum Collections

## Coworkers

Tianxin Deng

## Project Objective:

This is a project we want to do data cleaning and statistical analysis to a large dataset. We intend to visualize the patterns in the data and explain them.

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

## Summary

- We corrected many misspelled names. But there are so many names in the dataset. Once if there is just a typo, it's really hard to tell which is the right one and the other is a typo.
- Each time there is a large amount of collections being collected by the museum, there is a history events correspondingly.

## Project Binder link
[analysis_of_museum_collections ]( https://mybinder.org/v2/gh/CesareGao/analysis_of_museum_collections/master?filepath=analysis_of_museum_collection.ipynb )

## Project Running result (HTML)
[analysis_of_museum_collections.html]( https://github.com/CesareGao/analysis_of_museum_collections/blob/master/analysis_of_museum_collection.html )
