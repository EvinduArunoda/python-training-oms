# python-training-oms

Pre-Requisites  

- Backend development experience (strong understanding of concepts) 

- REST API knowledge 

- Strong knowledge on OOP concepts 

- PostgreSQL database knowledge 

- Docker 

 

Outcome 

Knowledge in the following areas of python 

Basics in Python  

Using OOP 

File structure 

Debugging 

Use Python for Backend Development and API integration 

Experience in Django Framework 

Use Wagtail CMS 

API documentation 

Tasks 

Introduction 

Install latest python environment to your laptop. 

It is best practice to do everything in separate virtual environments in python. Therefore, create a virtual environment for python backend development. 

Install PostgreSQL and PgAdmin into your laptop and familiarize with it. 

Install docker to your system. Understand the basics concepts of docker. 

Learn basic things about Django, Flask, FastAPI, CherryPy. 

Compare Django with other python frameworks and other backend technologies like nodejs, spring boot, etc.  

 

Understanding Python Concepts 

Learn how to implement OOP concepts in python 

Learn about decorators and built-in decorators: @classmethod, @staticmethod, @property, etc. 

Learn about python ABC module. 

Learn about python typing module. 

Learn about multiple inheritance, mixins, meta classes. 

Add a new Model 

Install Django via pip 

Add a new Django model called Customer with fields, 

First name 

Last name 

Date of birth 

Currency balance (float) 

Page visits (int) 

Connect it to the admin portal 

Add, edit, and delete Customers with admin portal 

 

Add PostgreSQL 

Connect Django with PostgreSQL 

Make sure last example is still running 

Open PgAdmin and see the changes you do through admin portal is appearing there as well 

 

Expose Rest API 

Expose the following REST APIs endpoints 

POST /customers -> Add new customer 

GET /customers -> Get all customers 

GET /customers/{id} -> Get the customer given by the ID 

PUT /customers/{id} -> Edit customer given by the ID 

DELETE /customers/{id} -> Delete the customer given by the ID 

Use Django REST Framework 

Use postman to call the APIs 

 

Folder Structure 

Text

Description automatically generated 

 

Root folder, where manage.py file is located, has the main project folder (my_project) 

Inside that, main Django site files are located 

In a project we may need to have multiple settings.py files (for prod, dev, etc). Those files are maintained in settings folder instead. 

Templates folder is to store web site’s html files 

Static folder is to store web assets. (css, js, img, etc) 

Folders created with startapp command are the modules. Those are managed in separate folders. 

Inside a module it has everything it need like models, migrations, view files, etc. 

Add Relational Models 

Add a new Django model called CustomerOrder with the following fields: 

Order Created Date 

Customer (Reference to the Customer Model) 

Item count 

Description 

Connect to admin portal 

Expose the following endpoints 

POST /orders 

GET /orders 

GET /orders/{id} 

PUT /orders/{id} 

DELETE /orders/{id} 

 

Documenting APIs 

Look documenting APIs with Django REST Framework 

Add descriptions to, 

Beginning of the API documentation 

To each endpoint 

For every field 

Every response 

Authorize endpoints 

Connect Firebase to the project 

Enable Firebase email & password authentication method 

Create a small web application to login where you can get an ID_TOKEN for the user 

Send that ID_TOKEN in the Authentication header as a bearer token for backend calls 

From the backend, request with only a valid ID_TOKEN can access the endpoints 

 

Wagtail 

See how to create a new wagtail project 

Implement your first wagtail site 

Learn more about page models and templates. 

 

Wagtail Integration 

Integrate wagtail to the previous project. (documentation) 

Models needs to be migrated to Wagtail model admins. 

Create a homepage template and connect it to GET /home endpoint 

Home page should have 

Title 

Description 

Customer information in a table (don’t use the endpoint to get data) 

Title and description can be changed via Wagtail 

 

Customer Search 

In the home page there should be a text box 

When type a text and press enter, only the customers who have that entered text in their first name or last name should appear in the table. 

Should not be case sensitive. 

Clear the text and press enter again should load the whole table 

 

Advertisements 

Home page should have a top navigation bar 

There should be a button to load the advertisements on a separate page 

That page should have these texts 

Title 

Description 

How to donate 

These texts can be changed via Wagtail 

In addition, it should display all the advertisements in cards 

Advertisement cards have, 

Title 

Description 

Learn more button 

Background color is either red, green, or blue. 

Advertisements to show in this page can be added via Wagtail portal. (Snippet) 

Title text 

Description text 

Link to navigate when learn more button is clicked 

Background color of the card 

 

Show Customer Orders 

Customers table in home page should have “view orders” button as the last column of each row. 

Once the button is clicked, navigate to a new page where all the orders of that customer is loaded 

That page should have 

Title: Order of the <customer first name> 

Subtitle 

Description 

Table of all orders of the customer 

Subtitle can be changed via Wagtail 

Description should display basic customer information. Via Wagtail we can configure what fields of the customer to show. 

Don’t use endpoints to get these data. 

 

Working with Wagtail Headless way 

Items 

Create Item model with model admin. 

Attributes: id, name (str), visible (bool), price (float), description (str) 

Attach this with model admin. Visible field should not be visible. 

Create 5 endpoints. Visible field should be false by default. Cannot be edited but should be viewed. 

Create additional endpoint POST /item/{id}/toggle-visibility to toggle the visibility of item 

Add basic authentication. All endpoints should be secured via basic auth. Username & password can be hard coded, no need to integrate with an Auth server. 

 

Category 

Create category model. Attributes: id, name 

Item should have a one-to-many relationship with category. 

Attach with model admin 

Change “get all items” endpoint to query by category name (not id) 

Add pagination to that endpoint. 

 

Orders 

Create order model. Attribute: id, description 

Order should have many-to-many relationship with item. 

Attach with model admin 

When editing order, items should be able to add. 

When editing items, the orders that item is in should be visible, not editable. 

 

Item Visibility 

Item edit page should have a new button. 

If item’s visible=False, the button name is “Make Visible”. Otherwise “Make Invisible”. 

Implement the button action (You cannot use the previous endpoint because it only has basic auth). Implementation should be secure as any other endpoint in wagtail admin. 

 

Item creator 

Item should have additional field: created_by 

When someone creating an item, via endpoint or admin portal, this should automatically be filled with current authenticated user. Not editable via endpoints or admin portal. But should be viewable.  

Item visibility button should be disabled if the current user is not the item creator. Button should show a tooltip, “Visibility can be changed only by the creator”.  

 

Wagtail Groups 

Category should have many-to-many relationship with Wagtail groups (built in groups) 

The groups of a category cannot be edited in category edit page. But should be visible. 

When creating/editing groups, the categories can be selected. 

Categories should be editable only if the logged in user have that group assigned to him. 