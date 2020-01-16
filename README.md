
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
