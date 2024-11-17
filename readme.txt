This is the readme file for this FlashCard app

Implement Edit feature
Make columns for Decks, dropdown menu
upon creation, it will throw the question into a selected category
one deck is 

dropdown menu to show existing category, enter new category will prompt user to create a category


create a category:
text box - flashcard design

display side:
could use vertical lines to divide decks 
Simple table, each col being a new deck


need to add another column to sql table
drop table, and add another category 
just a regular varchar

to retrieve, select * from table where category =?
validation:
need user input, need to handle mistype, and handling for input validation, use dropdown menu to select previously made tables

js side, validation of category seeing if it already exists, say its an error when typo was given, and do it a fuzzy match
could do a confirm to validate input

need to handle deleting category
must have some confirmation from the user, refresh page after



could also do autocomplete js, to see api to match values if you want to add typing and dropdown menu


should keep in mind of mobile size, for css
go to w3geeks for tables in css
could use bootstrap or just use a html/table with css

bootstrap is another jss library

could use coco 3d for mobile app for python
good experience


need to change schema, change ui for edit and del column
need to change category logic, add categories and autocomplete for searching for categories upon creation

editing categories and editing flashcards on what their categories already
need to figure out how add a category whilst empty, need CRUD operators (create, replace, update, delete)
probably don't have to update

general population of flashcards if no categories specified for flashcard

what type of queries we need for this table, need to handle how we want to put categories
could be a primary key for category.

could default category id 1 to default
