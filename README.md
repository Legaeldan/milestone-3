
<h1 align="center">
<a href="http://drink-splash.herokuapp.com/" target="_blank"><img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/DrinkSplash.png?raw=true" alt="Drink Splash Logo"/></a>
  Drink Splash - Find your drink today!
</h1>
<h2>Milestone 3 Project - Kieran Cunnane</h2>

This site has been created to give users a simple, easy to navigate system in which to find, create, and update their favourite drink recipes. It enables users to view their own creations in one easy place.

The site is designed with the most intuitive user experience in mind. A strong, defensive design against unwanted changes to the database has also been incorporated into the site.

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**development Goal**](#development-goal)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Design choices**](#design-choices)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Types**](#data-types)
    - [**Collections Structure**](#collections-structure)

4. [**Testing**](#testing)
    - [**Test Planning**](#test-planning)
    - [**Known Bugs**](#known-bugs)

5. [**Technologies Used**](#technologies-used)
    - [**Languages**](#Languages)
    - [**Frameworks/Libraries**](#frameworks/libraries)
    - [**Software**](#Software)
    - [**Additional Resources**](#additional-resources)

6. [**Deployment**](#deployment)
    - [**Deployment to Heroku**](#deployment-to-heroku)
    - [**Running this project locally**](#running-this-project-locally)

7. [**Credits**](#credits)

8. [**Disclaimer**](#disclaimer)

## UX

### Project Goals

The main objective in creating the Drink Splash application is to provide the user with a simple to use repository of recipes for cocktail and drink making. It also provides an every growing database of cocktails, drinks, and ingredients for the users to browse through and add to.

This applications is designed with adventurous drinkers in mind who require an easy way to explore drinks menu based on what they might have on hand, or randomly discover a new drink they may not have tried before. It also allows users to share their recipes with others easily.

As a side goal, I have left room for expansion once I have developed my skills further, and would like to develop this into a commercially viable system with ordering features, and live updates as outlined below in the [**Features Left to Implement**](#features-left-to-implement) section 2.2.4.

#### Development Goal

- A project I'd be excited to show off to people as a testament to my abilities.
- Well thought out programming to account for the unpredictability of users. 
- Something that looked professional even for a novice programmer on their first venture in JavaScript and jQuery.
- To learn and impliment intricate python code that would be impressive to a veteran python programmer.
- To create an ever expanding database project that users can easily add to, and over time will grow to large repository of information on drink creation.

### User Stories

 **As a user I want this application to have:**
 1. A system to search for drinks containing certain ingredients.
 2. A website that is easy to navigate.
 3. A website which is pleasant to look at.
 4. A way to inspect and edit my own creations.
 5. An application which makes it easy to edit my own creations.
 6. An application that makes it possible for only myself to change my own creations.
 7. An application that is fast, with very short load times.
 8. A page that I can easily add my own creations to.

### Wireframes

Wireframes were built in the early stages of development to get a rough outline of the structure needed for the planned features of the site. These can be viewed below:

- [Desktop](https://github.com/Legaeldan/milestone-3/blob/master/static/Wireframes/Desktop-Tablet%20App.pdf)
- [Tablet](#) Not Complete
- [Mobile](https://github.com/Legaeldan/milestone-3/blob/master/static/Wireframes/Mobile%20App.pdf)

### Design Choices

The main approach to this application is made to easy to maintain, and easy to use database. To provide as many features as possible to make the entire experience simple. The following design choices were made to reflect this:

**Fonts**

- The main body font **Josefin Slab** was chosen due to it's simplistic design, as not to distract from the overall site, and to not clash with the colourful images provided in the drinks.

**Colours**

- The colour choices were made to be simplistic, but to constrast the images presented in the drinks.
- Colours of **off-black** and **grey** were chosed to not overload the user, and maintain a simple, clean look.
- **Gold** was chosen as nice contrast to the **black** and **grey** backdrop of the site, and to help highlight any helpful links. **Gold** was found to be the best contrast while remaining easy on the eye.

**Styling**

- Use of the **Materialize** framework was used to keep the site simple, only displaying relevant information, without drawing attention away from the content.
- The use of borders and rounded edges to images was chosen to give the impression that the images are printed onto coasters, keeping in tone with the website overall theme of **drink recipes**. 

**Background**

- Background colour of a **linear gradient** from **black** to **white** was selected to better help the images and text stand out on screen, and to give a feel of a third dimension. This also helps accentuate the colours and images on screen, and give more depth to the overall page.

## Features

### Existing Features

1. **Encrypted Login**
    - A login form with encryption using the bcrypt system in Python. This ensures that any sensitive data passed to the database is first encrypted using a salt, which is then tied to that user.
    - This encrypted login system is also tied to the registration form, which is ecrypted before posting to the database.

2. **Context Sensitive NavBar**
    - The navbar has been created to change from a Login button, to the user's name once they are logged in.
    - This also gives the user access to their own collection from a dropdown menu which is generated once a user is logged in.

<div align="center">
<img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/NavbarChange.png?raw=true" alt="Screenshot: NavBar Changes" >
</div>


3. **My Collection Page**
    - A page specifically designed to show the user only items which they have created themselves, and filter out all other users data.

4. **Context Sensitive Buttons**
    - On the view drinks page, by default, the page only generates the drink information.
    - If a user is logged in, and if the user is the person who created the document, they are then presented with the edit drink, and delete drink options. Delete drink having an extra confirmation in the form of a modal to ensure accidental deletion doesn't occur.

<div align="center">
<img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/ContextButtons.png?raw=true" alt="Screenshot: Context Buttons" >
</div>

5. **Error handling**
    - A system is in place should a user try to access the add drinks page, and they are not logged in.
    - Should a user try the above, they will be immediately redirected to the login page. This also occurs with any registered user only features.
    - Error handling on the ingredients search is also handled by checking if method is POST. Should no ingredient be entered, but method is not POST, it will return the standard page. If method is POST, it will generate content for "No Ingredients Found".

6. **Random Drink Discovery**
    - A system is in place to generate a random document from the library for users to discover drinks on the fly instead of manually scrolling through the documents.

7. **Drinks Search Engine**
    - A search page is in place on the ingredients section. Users can search and filter by particular ingredients. The user is then returned all drinks that contain that particular ingredient.
    - This can also be done from the view drink page by clicking any ingredient on the list. The user will then be directed to the ingredients page, and returned all drinks containing that ingredient.

8. **Add Drink/Edit Drink Modal**
    - A modal style add and edit modal for easy addition of drinks. This feature does away with the need for extra pages to handle the requests.
    - This simplified version results in the addition of drinks facility being available on any page the user may be on.


9. **Switchable Menu**
    - The accommodate more traditional users of the site, I have added in a switchable function via Javascript to switch from the new style FAB menu, and a classic navbar style menu.
    - This feature is also persistence on devices when switched. Even after a session is closed, the users choice is still registered if they favour the FAB menu style.

10. **One to Many Relationships**
    - To improve the site, I have implimented a one-to-many model through MongoDB. This means that information like ingredients would not all have to be stored in one document, and facilitate the search engine being able to pull multiple connected documents.
    - this feature also allows for the registered user feature of the My Collection page. As a seperate collection called users ties the user to specific document as show below.

<div align="center">
<img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/DBStructure.png?raw=true" alt="Screenshot: DB Structure" >
</div>

### Features Left to Implement

1. **Favourites**

I would like to impliment a system that allows the user to favourite a drink, then return all drinks on a favourites page that the user has favourited.

2. **Measurements**

I would like to impliment a system that generates the measurements of ingredients, and add to the ingredients section on view drink. I'm currently tied between a new collection of all possible measurement size, and concatonating the results with the assosciated ingredients, or providing the user with a section which generated new lines on the form whenever an ingredient is selected. I will explore this further going forward with development of this site.

3. **Admin Control Panel**

A page specifically for user stats, how many views their drink has recieved, both unique, and recurring. A section on how many creations, and what their favourite ingredient to use in their recipes. Suggestions of related recipes based on their favourite ingredient.

4. **Ordering Feature**

For future enhancement for practical use of the site. I would like to add an ordering feature. This would be used in a live setting (i.e. a pub/cocktail bar) to search drinks, find certain ingredients, and select a drink based on those criteria. To also provide a full list of ingredients to double as an allergen check. For users to store their orders, and order their favourites for later reordering. And for the list to generate on the fly to operators behind a bar. A good representation of this feature would be related to the Domino's Pizza application, which provides realtime order to a screen in shop.

## Information Architecture

### Database Choice

In the initial planning phase of this project, an SQL structured database was decided on, but was quickly found to be more complex in regards to hosting. Planning for this database choice was then restructed to suit a NoSQL database, with a one to many relationship structure, emulating the initial plan of an SQL database.

To emulate the original SQL planned structure, inner objects satructured as arrays, and pulled from other collections was utilized as shown below and in the schemas supplied.

### Data Types

The types of data in this project stored in MongoDB are:
- ObjectId
- String
- Binary
- Array

### Collections Structure

Drink splash heavily relies on three connected database collections. Case sensitive collections are vital to it's operation as below:

#### Users Collection
| Title         | Key in db | form validation type | Data type |
|---------------|-----------|----------------------|-----------|
| Username ID   | _id       | None                 | ObjectId  |
| Username      | username  | text                 | String    |
| Email Address | email     | email                | String    |
| Password      | password  | text                 | Binary    |

[Example JSON from users collections](https://github.com/Legaeldan/milestone-3/blob/master/data/schemas/users.json)

- Passwords are entered as string, but stored as binary after encryption. The same process is carried our when logging in. The supplied password is encrypted using the supplied key in the password section, and checked to match the existing encrypted binary password.

#### Ingredients Collection
| Title                | Key in db       | form validation type | Data type |
|----------------------|-----------------|----------------------|-----------|
| Ingredient ID        | _id             | None                 | ObjectId  |
| Ingredient Name      | ingredientName  | text                 | String    |
| Ingredient Image URL | ingredientImage | url                  | String    |

[Example JSON from ingredients collections](https://github.com/Legaeldan/milestone-3/blob/master/data/schemas/ingredients.json)

#### Drinks Collection
| Title               | Key in db      | form validation type | Data type |
|---------------------|----------------|----------------------|-----------|
| Drink ID            | _id            | None                 | ObjectId  |
| Drink Name          | drinkName      | text                 | String    |
| Instructions        | instructions   | textarea             | String    |
| Drink Image URL     | drinkImage     | url                  | String    |
| Ingredients List    | ingredientList | checkbox             | Array     |
| Date Modified       | modifiedDate   | None                 | String    |
| Created By Username | createdBy      | None                 | String    |

[Example JSON from drinks collections](https://github.com/Legaeldan/milestone-3/blob/master/data/schemas/drinks.json)

- Note: The Ingredients List array is predefined as a list generated from the Ingredients Collection. For correct functionality of the DB, the items in the array must match an item in the ingredients table, and is case sensitive.

- The Date Modified section is generated from the datetime now function in python, and then converted to a string for easy storage and sorting.

- The Created By Username is generated by the session, and cannot be altered, as adding a drink is a registered user only function.

## Testing

As a first attempt at Python/Flask programming, the code had to be scrutinized, and thoroughly tested throughout. Every function would need to be planned, and tested in depth before moving on to other functionality, as these would be tied together later in the project.

**All testing results can be found in the seperate [TESTING.md](https://github.com/Legaeldan/milestone-3/blob/master/data/testing/TESTING.md) file. 

#### Test Planning:

During planning and development, defensive design was taken into account. The planning of testing was split into two section. **Functionality** and **Defensive Design**. Each function was planned out carefully, then a subsection to testing was added for defensive design, in which that particular function was given every possible variable a user could give, and tested for unwanted activation.

**Example:**
 - **Planning:** A function is needed to remove the drink should the user not be happy with the outcome, or the drink is not required anymore. 
 - **Testing (Phase 1):** The function does as required, and removed the entire entry from the database.
 - **Testing (Phase 2):** the function applied this function regardless of what ID was given, resulting in a crash as the item didn't exist. The function was updated to try find the drink first, then return an error if failed.
 - **Defensive:** After functionality was fully tested. Loop holes in the function were discovered. A user could delete a drink regardless of owning the item by altering the URL. Added checks if the user is firstly valid (As this is a registered user only function), then check if they own the item. If all checks pass, the function runs as normal.
 - **Result:** A simple button that can only be fired under certain circumstances.
 - **Verdict:** Test passed as expected and delete button is now operational..

**All testing results can be found in the seperate [TESTING.md](https://github.com/Legaeldan/milestone-3/blob/master/data/testing/TESTING.md) file. 

### Bugs During Development

Testing for end user experience and defensive design was done by myself, and outsourced during this project to give standard users a chance to experience the site, and for me to get realistic feedback on features. This also had the added benefit of getting reports back on exact errors, and what a standard end user would possibly try to do on this site that had not been accounted for. This also accounted towards defensive design, as near end of testing, the users we given instructions then to intentionally attempt to break the site.

1. **Images not rendering**
    - **Issue:** Users tried to add images to their creations. As they were not familiar what type of link was needed, the site would then render a broken image link, causing surrounding elements to shift out of place.
    - **Solution:** Added jQuery function to check page for errors on images. Should it find an error in an image link, it would replace the image source with a predefined standard image link, with the text "Image not found" inside.
    - **Result:** Function detected errors immediately, and corrected the issue. All sibling elements then rendered correctly around the broken image.
<img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/testing/testing1.png?raw=true" alt="Test Results 1"/>
<img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/testing/testing2.png?raw=true" alt="Test Results 2"/>


2. **Incorrect URL input**
    - **Issue:** Users, when trying to manually type the URL were greeted with a Jinja crash log. Anything outside a valid URL would cause this crash.
    - **Solution:** Impliment a 404 page.
    - **Result:** Added an error handler to flask for 404 errors. Then added a try except to catch all errors and provide a specific messages to the user. Added custom messages as descriptions to the user, which are then rendered on the page. Also added the explicit flag to the error handlers to catch anything that was not a valid URL.

3. **Changing drink URL**
    - **Issue:** Users tried to add custom strings to the end of the drinks URL ``` (pageURL.com/drink/<custom-string>) ```. When anything other than a valid link was inserted, the system crashed, and requested only 12 byte or 24 hex string input.
    - **Solution:** Added a try except block to catch errors, and if failed, would revert to another page.
    - **Result:** Added an error handler to flask for 404 errors. Then added a try except to the drinks page to catch all errors. The if checks within the try block checks for all possible valid variations of the URL, and on failure, returns to the 404 error handler.

4. **Changing drink URL**
    - **Issue:** Users could view a drink, and then change``` (pageURL.com/drink/<drink-id>) ``` to  ``` (pageURL.com/delete-drink/<drink-id>) ```. This would cause the drink to be delete regardless of rights.
    - **Solution:** Add an if check to handle if the user is valid, and allowed to delete the item.
    - **Result:** If check now checks firstly if the user is logged in. Then checks if the user is allowed to delete the drink. If neither of these are true, the user is returned to the 401 error handled, and provided a message of "Not Authorized".

5. **Unable to add drink ingredients**
    - **Issue:** When a user is logged in, the ingredients section of the add drink modal would generate no items. This was due to a for loop prior that expended all the data in that loop.
    - **Solution:** Added a second search on the database specifically for the add drink page, and named it differently. 
    - **Result:** Both add drink and edit drink forms had their own specific list to work from, allowing both forms to iterate over their own respective loops.

6. **Any user could delete/edit**
    - **Issue:** Buttons to edit and delete drinks was available to all users regardless if they added the item or not.
    - **Solution:** Impliment user specific buttons, and encrypted logon system. 
    - **Result:** Users are now only presented with buttons that apply to their own drinks, preventing others from deleteing their creations, and preventing a user stumbling across the site, and removing the entire database.

7. **Drinks able to be duplicated**
    - **Issue:** Users were able to create a drink multiple times. Resulting in duplicate entries.
    - **Solution:** Add a check if the item already exists.
    - **Result:** Should a user duplicate an item. They are then returned the drink they are duplicating, with a message that it already exists.

8. **Ingredients off center in search**
    - **Issue:** When an ingredient is selected for search. The box added a random margin to the left of the name.
    - **Solution:** Removed unused space in for loops for generating ingredients which was the cause for a space to be generated on every item.
    - **Result:** Ingredient selected now lined up correctly with the search box, to enable the user to read the item once select. This especially affected mobile users who had limited space.

<img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/testing/testing4.png?raw=true" alt="Test Results 4"/>

9. **Collection URL returns no user**
    - **Issue:** Users can check other users collection by adding their name to the end of the collection URL. If the user had no items created by them, the system would return "User does not exist."
    - **Solution:** Add additional user check before checking for user created item.
    - **Result:** Collection correctly returns a 404 with custom message that user has no items in their collection. If user doesn't exists, returns a no user exists 404.

10. **No account to maintain database**
    - **Issue:** During testing, any database maintainance had to be done by logging into MongoDB, which was found to be time consuming.
    - **Solution:** Add admin account that has access to all the features provided to users.
    - **Result:** Gives the admin the ability to access all features, and delete drinks on the fly while scanning the website.

### Known Bugs

- **valign-wrapper on IE11**
    There is an issue with the valign-wrapper not being supported on IE11. As this is critical to the layout of the system, including the flex footer, I was unable to remove this for compatibility on Internet Explorer. Flex is crucial to the static footer, and to the vertical layout on Chrome.

- **Windows 10 Flickering**
    When Windows 10 system scale is set to 125%, the webpage flickers when the mouse is moved. A scroll bar also flickers on mouse move. Other than changing system settings back to 100%, I have found no cause or resolution to this.

- **Ingredient List on Mobile**
    An issue arose when adding a drink. When the user scrolls through the ingredients list and selects an item further down the list than the view height. The modal will expand as if the list behind is at full height. This issue has not been replicated on desktop.

- **Menu overlay on mobile**
    When on mobile, and switching from the classic menu to the FAB menu. The overlay remains in place until the user taps again anywhere on the screen. I have tested hiding this overlay on click using jQuery, but it results in the menu opening and sticking on screen when switching back to classic menu. The only way to exit them menu when this happens is clicking another link.

- **Tooltip showing incorrectly**
    When on mobile, tooltips show up incorrectly when clicking the menu switch icon. The tooltips show at the top of the screen until the user clicks again. I have yet to resolve this issue.

<img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/testing/testing3.png?raw=true" alt="Test Results 3"/>

- **Android Search**
    And issue was discovered when testing on Android phones, that when instructions is clicked on the view drink page, chrome immediately tries to do a Google search on the word "Instruction". This also applies to the any headings on the page, but I have yet to find the cause, or fix this issue. This issue does not occur in the developer section for desktop Chrome when scaling for mobile.

- **Responsive Resizing**
    When resizing the screen using Chrome Developer tools. There is an issue in which overflow from the page has expanded past the content. This overflow is retained from the larger screen, and can be removed by reloading the page once the desired size/device has been found. There is no solution to this at present.

- **PEP Standards**
    During linting of the python application, and warning occured on lines 154 & 256 that state an unneccessary elif statement was used after a return. I have tested the program both with, and without these elif statements, and found the function does not complete as expected without these statements. I have not yet found the cause of the warnings.

## Technologies Used

### Languages:
- [Python](https://www.python.org/)
    - The project uses **Python** to run the application.
- [HTML](en.wikipedia.org/wiki/HTML)
    - The project uses **HTML** to structure the DOM.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - The project uses **CSS** to style and theme pages..
 - [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - The project uses **Javascript** to allow for DOM manipulation.

### Frameworks/Libraries:  
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.            
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
    - The project uses the **Flask** to dynamically generate pages, generate dynamic links, and content within the application.
- [PyMongo](https://api.mongodb.com/python/current/)
    - The project uses **Pymongo** to initiate a connection with, and transfer data to and from MongoDB.
- [Materialize](https://materializecss.com/)
    - The project uses the **Materialize** framework to simplify the structure of the website and make the website responsive easily.
- [MongoDB](https://www.mongodb.com/)
    - The project uses **MongoDB** to store all project documents within an easily accessible database.
- [Virtual Env](https://virtualenv.pypa.io/en/latest/)
    - This project utilise Virtualenv to run a closed virtual enviroment specifically tailored for this project.
- [Bcrypt](https://www.npmjs.com/package/bcrypt)
    - This project uses the Bcrypt library to encrypt passwords for user security.

### Software:
- [Visual Studio Code](https://code.visualstudio.com/)
    - The project uses **Visual Studio Code** to create all files contained in the site, and push to GitHub.
- [Git](https://git-scm.com/downloads)
    - This project uses **Git** to commit and push all files to the [GitHub Repository](https://github.com/Legaeldan/milestone-2).
- [GIMP](https://www.gimp.org/)
    - This project used tools in **GIMP** to create and edit images such as the logo and favicon.
- [Visio](https://www.microsoft.com/en-ie/p/visio-standard-2019/cfq7ttc0k7cf?activetab=pivot%3aoverviewtab)
    - This project used tools in **Visio** to create, edit, and present wireframes in a more professional manner.

### Additional Resources:    
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** to style additional website icon links.
- [HTML Validator](https://validator.w3.org/)
    - This project utilised the HTML validator provided by W3C to check and correct any issues in my current HTML code.  

## Deployment

This project was developed using [Visual Studio Code](https://code.visualstudio.com/), [Python](https://www.python.org/), and [Git](https://git-scm.com/downloads), committed to a local [Git](https://git-scm.com/downloads) repository, and pushed to [GitHub](https://github.com/Legaeldan/milestone-3) using a locally installed version of [Git](https://git-scm.com/downloads) via command prompt.

The main method of deployment is [Heroku](http://drink-splash.herokuapp.com/), connected directly to my [GitHub Repository](https://github.com/Legaeldan/milestone-3), and deployed within the [Heroku Dashboard](https://www.heroku.com/).

### Deployment to Heroku

To deploy this page to [Heroku](https://www.heroku.com/) from its [GitHub repository](https://github.com/Legaeldan/milestone-3), the following steps were taken: 
1. Log into [Heroku](https://dashboard.heroku.com/). 
2. From the main dashboard, select the **New** dropdown, then select **Create new app**.
3. Give you app a unique name, and select the region you wish to deploy to.
4. After the app is created, select **Deploy** from the top of the page, and scroll down to **Deployment Method**.
5. Select **GitHub** as the method of deployment.
6. Log in using your **Github credentials.** 
7. Select your username, and search for the reposity in the **repo-name** box.
8. Select **Connect** on the repository you wish to connect to.
9. Under **Manual deploy**, select the branch you wish to deploy, and hit **Deploy Branch**
10. After the application is built, select **Settings** from the top of the page.
11. Select **Reveal Config Vars**.
12. Add the config keys for **IP**, **PORT**, **MONGO_URI**, **MONGO_DBNAME**, and **SECRET_KEY** (These will not be published here for security reasons).
13. Select **More** from the top right of the page, and select **Restart all dynos**.


### Running this project locally

**Please note: This project was created and run on Windows in Visual Studio Code with a Virtual Enviroment using Python 3 and Git. Please ensure you have Python 3 and Git installed locally before running this project. For other OS or Code Editors, please refer to the relevant documentation for your enviroment.**

**Preferred Requirements:**  
 - [Visual Studio Code](https://code.visualstudio.com/)
 - [Git](https://git-scm.com/downloads)
 - [Python](https://www.python.org/)
 - An account with [MongoDB Atlas](https://www.mongodb.com/) or a local instance of MongoDB. Please refer to the [MongoDB Documentation](https://docs.atlas.mongodb.com/) for more help.



To clone this project from GitHub:
1. Follow this link to the [GitHub repository](https://github.com/Legaeldan/milestone-3).
2. Under the repository name, click the green "Clone or download" button.
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local editor program, open a terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.

```
git clone https://github.com/Legaeldan/milestone-3
```

7. Press Enter. Your local clone will be created.
8. From the terminal, type ```pip3 install virtualenv```
9. Once the above is complete, type ```virtualenv env```. This will create your local virtual enviroment.
10. Create a folder in the root directory called **.vscode**.
11. In the **.vscode** folder, create a file called **settings.json**
12. Insert the below code into the settings.json file, wait for the enviroment to load (This can be seen in the lower left hand corner of VSCode).
```json
{
    "python.pythonPath": "env\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintArgs": ["--load-plugins=pylint_flask"],
    "files.autoSave": "onFocusChange",
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "[INSERT YOUR SECRET KEY HERE]",
      "DEV": "1",
      "FLASK_DEBUG": "1",
      "MONGO_URI": "[INSERT YOUR MONGO URI HERE]",
      "MONGO_DBNAME": "[INSERT YOUR DB NAME HERE]"
    }
}
```
13. Restart VSCode. The bottom left should now state **Python X.X.X 64/32-bit ('env':virtualenv)**
14. Open a terminal windows. The directory in terminal should now be preceeded by **(env)**, stating the enviroment is now active.
15. From the terminal, type ```pip3 install -r requirements.txt```.
16. Once complete, type ```python app.py```

For more help on cloning a repository on Github, please click [here](https://help.github.com/en/articles/cloning-a-repository).

## Credits

Inspiration for this project was found at [TheCocktailDB](https://www.thecocktaildb.com/), an open, crowd-sourced database and JSON API. I used this model as inspiration to emulate this system in MongoDB. I liked the concept initially, but wasn't happy with the design or overall layout. I hoped to improve on this with this project.

Credit also to [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) for their tutorial on the - [Flask Login System](https://github.com/PrettyPrinted/mongodb-user-login).


### Acknowledgements

#### Guidance

I received inspiration and assistance on this project from [Simen Daehlin (Eventyret)](https://github.com/Eventyret), who assisted above and beyond to help improve the site. What seemed like the impossible task of understanding [Python](https://www.python.org/), became far simpler that originally believed. He has helped understand this language a lot better, and has pointed me in the right direction everytime whenever an issue arose with how to impliment code.

## Disclaimer

Please note that all code and images in this site are for educational purposes only. The original CocktailDB site or any of it's ideas are in no way owned by me, and this site uses the original site as a concept only to show the developers ability in the language of Python/Flask. 