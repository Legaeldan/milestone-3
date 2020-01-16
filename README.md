
<h1 align="center">
<a href="http://drink-splash.herokuapp.com/" target="_blank"><img src="https://github.com/Legaeldan/milestone-3/blob/master/static/images/DrinkSplash.png?raw=true" alt="Drink Splash Logo"/></a>
  Drink Splash - Find your drink today!
</h1>
<h2>Milestone 3 Project - Kieran Cunnane</h2>
<p>This site has been created to give users a simple, easy to navigate site to find, create, update their favourite drink recipes, and view their own creations in one easy place.

The site is designed with the best user experience in mind, while maintaining a strong, defensive design against unwanted changes to the database.</p>

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**development Goal**](#development-goal)
    - [**User Stories**](#user-stories)
    - [**Design choices**](#design-choices)

2. [**Features**](#features)

3. [**Testing**](#testing)

4. [**Technologies Used**](#technologies-used)

5. [**Deployment**](#deployment)
    - [**Deployment to Heroku**](#deployment-to-heroku)
    - [**Running this project locally**](#running-this-project-locally)

6. [**Credits**](#credits)

7. [**Disclaimer**](#disclaimer)

## UX

### Project Goals

The main objective in creating the Drink Splash application is to provide the user with a simple to use repository of recipes for cocktail and drink making. It also provides an every growing database of cocktails, drinks, and ingredients for the users to browse through and add to.

This applications is designed with adventurous drinkers in mind that require an easy way to explore drinks based on what they might have on hand, or randomly discover a new drink they may not have tried before. And for those who wish to share their recipes with others easily.

#### Development Goal

- A project I'd be excited to show off to people as a testament to my abilities.
- Well thought out programming to account for the unpredictability of users. 
- Something that looked professional even for a novice programmer on their first venture in JavaScript and jQuery.
- To learn and impliment intricate python code that would be impressive to a veteran python programmer. 

### User Stories

 **As a user I want this application to have:**
 1. A system to search for drinks containing certain ingredients.
 2. A website that is easy to navigate.
 3. A website which is pleasant to look at.
 4. A way to inspect and edit my own creations.
 5. An application which makes it easy to edit my own creations.
 6. An application that makes it possible for only the creator to change their creations.
 7. An application that is fast, which very little load times.

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

- Background colour of a *linear gradient** from **black** to **white** was selected to better help the images and text stand out on screen, and to give a feel of a third dimension. This also helps accentuate the colours and images on screen, and give more depth to the overall page.

## Features
 
## Testing

## Technologies Used

- This project uses HTML, CSS and JavaScript programming languages.
- [Python](https://www.python.org/)
    - The project uses **Python** to run the application.
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
    - The project uses the **Flask** to dynamically generate pages, generate dynamic links, and content within the application.
- [MongoDB](https://www.mongodb.com/)
    - The project uses **MongoDB** to store all project documents within an easily accessible database.
- [PyMongo](https://api.mongodb.com/python/current/)
    - The project uses **Pymongo** to initiate a connection with, and transfer data to and from MongoDB.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Visual Studio Code](https://code.visualstudio.com/)
    - The project uses **Visual Studio Code** to create all files contained in the site, and push to GitHub.
- [Git](https://git-scm.com/downloads)
    - This project uses **Git** to commit and push all files to the [GitHub Repository](https://github.com/Legaeldan/milestone-2).
- [Materialize](https://materializecss.com/)
    - The project uses the **Materialize** framework to simplify the structure of the website and make the website responsive easily.
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** to style additional website icon links.
- [GIMP](https://www.gimp.org/)
    - This project used tools in **GIMP** to create and edit images such as the logo and favicon.
- [Visio](https://www.microsoft.com/en-ie/p/visio-standard-2019/cfq7ttc0k7cf?activetab=pivot%3aoverviewtab)
    - This project used tools in **Visio** to create, edit, and present wireframes in a more professional manner.
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
6. Log in using your Github credentials. 
7. Select your username, and search for the reposity in the **repo-name** box.
8. Select **Connect** on the repository you wish to connect to.
9. Under **Manual deploy**, select the branch you wish to deploy, and hit **Deploy Branch**
10. After the application is built, select **Settings** from the top of the page.
11. Select **Reveal Config Vars**.
12. Add the config keys for **MONGO_URI**, **MONGO_DBNAME**, and **SECRET_KEY** (These will not be published here for security reasons).
13. Select **More** from the top right of the page, and select **Restart all dynos**.


### Running this project locally

To clone this project from GitHub:
1. Follow this link to the [GitHub repository](https://github.com/Legaeldan/milestone-3).
2. Under the repository name, click the green "Clone or download" button.
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local editor program, open a terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.

```git clone https://github.com/Legaeldan/milestone-3```

7. Press Enter. Your local clone will be created.
8. From the terminal, type ```pip3 install -r requirements.txt```.
9. Once complete, type ```python app.py```

For more help on cloning a repository on Github, please click [here](https://help.github.com/en/articles/cloning-a-repository).

## Credits

## Disclaimer
