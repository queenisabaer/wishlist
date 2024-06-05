# Your Wish List Maker
Full-Stack Toolkit Portfolio Project(PP4) - Code Institute

View the deployed site [here.]()<br>

 *Your Wish List Maker* is a website designed to help people keep their wish lists for special occasions organised.  
 It is a full stack Django project running on Heroku.

![Screenshot of the preview of application](documentation/readme/)<br>

## Table of contents

- [User Experience (UX)](#user-experience-(ux))
- [Design](#design)
- [Features](#features)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

I used an Agile methodology approach to plan this project. This was implemented through the GitHub Project board with milestones, epics, user storie and tasks.
Each user story was classified with a label according to MoSCoW prioritization.<br>
The Kanban board can be seen [here](https://github.com/users/queenisabaer/projects/3/views/1).

### Milestones

The project was divided into three milestones, each containing the corresponding epics and user stories:<br>
- [Basic Website Setup](https://github.com/queenisabaer/wishlist/milestone/1)
- [Wishlist MVP Management](https://github.com/queenisabaer/wishlist/milestone/2)
- [Testing and Validation](https://github.com/queenisabaer/wishlist/milestone/4)

### Epics & User stories

*Your Wish List Maker* is for those who are interested in organizing their wish lists for special occasions in one place and sending those wish lists to family and friends to provide them with all the desired items.
Although the website can be used by users of any age, my main target group was working parents, especially women between 30-50 years. <br>

List of Epics: <br>
- [EPIC 1: Repository and agile tool](https://github.com/queenisabaer/wishlist/issues/2)
- [EPIC 2: Basic Website and Database Structure](https://github.com/queenisabaer/wishlist/issues/3)
- [EPIC 3: User authentication](https://github.com/queenisabaer/wishlist/issues/4)
- [EPIC 4: Wish List Management](https://github.com/queenisabaer/wishlist/issues/5)
- [EPIC 5: Testing](https://github.com/queenisabaer/wishlist/issues/6)
- [EPIC 6: Validation](https://github.com/queenisabaer/wishlist/issues/7)

User Stories with their id:  <br>
- As a new website user I am able to identify the website's goal so that I can decide whether to continue or leave. [#9](https://github.com/queenisabaer/wishlist/issues/9)
- As a new user I can register an account so that I can create and manage wish lists or items of other wish lists. [#12](https://github.com/queenisabaer/wishlist/issues/12)
- As a registered user, I want to log in to my account so that I can create, read, update and delete my wish list(s) [#13](https://github.com/queenisabaer/wishlist/issues/13)
- As a registered user I want to manage my profile so that I can update my account. [#13](https://github.com/queenisabaer/wishlist/issues/13)
- As a registered user, I want to edit my wishlist so that I can update its details. [#16](https://github.com/queenisabaer/wishlist/issues/16)
- As a registered user, I want to be able to delete a wishlist so that I can remove outdated or unnecessary lists. [#17](https://github.com/queenisabaer/wishlist/issues/17)
- As a registered user, I want to edit items in my wishlist so that I can update their details.[#19](https://github.com/queenisabaer/wishlist/issues/19)
- As a registered user, I want to be able to delete items from my wishlist so that I can remove unwanted items.[#20](https://github.com/queenisabaer/wishlist/issues/20)
- As a registered user, I want to reserve an item of a wishlist, so that no other user will purchase this. [#23](https://github.com/queenisabaer/wishlist/issues/23)
- As a registered user, I want to be able to collaborate on a wishlist with others so that we can collectively manage it. [#24](https://github.com/queenisabaer/wishlist/issues/23)
- As a logged-in user, I want to update my profile information so that my account details are current. [#14](https://github.com/queenisabaer/wishlist/issues/14)
- As a frequent website user I can easily login to my account so that I have access to my wish lists and items I want to purchase. [#9](https://github.com/queenisabaer/wishlist/issues/9)
- As a user of the website I want to create a wish list for a specific occasion so that I can organize my desired items. [#15](https://github.com/queenisabaer/wishlist/issues/15)
- As a user, I want to add items to my wishlist so that I can keep track of things I want. [#18](https://github.com/queenisabaer/wishlist/issues/18)
- As a user, I want to share my wishlist with others so that they can see my wishlist and know what I want to have. [#22](https://github.com/queenisabaer/wishlist/issues/22)
<br>

- As a developer I want to define a database structure so that it matches the objectives of the project. [#10](https://github.com/queenisabaer/wishlist/issues/10)
- As a developer I want to set up and configure a database so that I can store and manage the application data securely and efficiently. [#11](https://github.com/queenisabaer/wishlist/issues/11)
- As a developer, I need to verify that all html files pass the W3C validation so that the code is executed correctly. [#25](https://github.com/queenisabaer/wishlist/issues/25)
- As a developer, I need to verify that my css files pass the W3C validation so that the code is executed correctly. [#26](https://github.com/queenisabaer/wishlist/issues/26)
- As a developer, I need to verify that my JavaScript files pass the jshint validation so that the code is executed correctly. [#27](https://github.com/queenisabaer/wishlist/issues/27)
- As a developer, I need to verify that my python files pass the pep8 validation so that the code is executed correctly. [#28](https://github.com/queenisabaer/wishlist/issues/28)
- As a developer, I want to implement python test procedures so that I can assess functionality, usability, responsiveness and data management throughout the web application. [#29](https://github.com/queenisabaer/wishlist/issues/29)
- As a developer, I want to implement JavaScript test procedures so that I can assess functionality, usability, responsiveness and data management throughout the web application. [#30](https://github.com/queenisabaer/wishlist/issues/30)
- As a developer, I want to implement manual test cases so that I can assess functionality, usability, responsiveness and data management throughout the web application. [#31](https://github.com/queenisabaer/wishlist/issues/31)
<br>

- As an admin I want to access the site's administrative features so that I have access to the admin panel. [#8](https://github.com/queenisabaer/wishlist/issues/8)

## Design

- **Wireframes** <br>

<details>
<summary> Home </summary>
<br>

![Mobile wireframe](/documentation/wireframes/wish-list-home-mobil.png)
![Desktop wireframe](/documentation/wireframes/wish-list-home-desktop.png)

</details>

<details>
<summary> About </summary>
<br>

![Mobile wireframe](/documentation/wireframes/wish-list-about-mobil.png)
![Desktop wireframe](/documentation/wireframes/wish-list-about-desktop.png)

</details>

<details>
<summary> Create New Wish List </summary>
<br>

![Mobile wireframe](/documentation/wireframes/wish-list-new-wish-list-mobil-admin.png)
![Desktop wireframe](/documentation/wireframes/wish-list-new-wish-list-desktop-admin.png)

</details>

<details>
<summary> Add Item </summary>
<br>

![Mobile wireframe](/documentation/wireframes/wish-list-add-item-mobil-admin.png)
![Desktop wireframe](/documentation/wireframes/wish-list-add-item-desktop-admin.png)

</details>

<details>
<summary> User Dashboard </summary>
<br>

![Mobile wireframe](/documentation/wireframes/wish-list-dashboard-mobil.png)
![Desktop wireframe](/documentation/wireframes/wish-list-dashboard-desktop.png)

</details>

<details>
<summary> Sign Up </summary>
<br>

![Mobile wireframe](/documentation/wireframes/wish-list-signUp-mobil.png)
![Desktop wireframe](/documentation/wireframes/wish-list-signUp-desktop.png)

</details>

<details>
<summary> Sample Wish List </summary>
<br>

![Mobile wireframe](/documentation/wireframes/wish-list-sample-wish-list-mobil-user.png)
![Desktop wireframe](/documentation/wireframes/wish-list-sample-wish-list-desktop-user.png)

</details>

- **Imagery:**<br>
 
background image

Logo


  ![Logo for Your Wish List Maker](documentation/readme_features/)<br>

 
- **Colour Scheme:**<br>
  
Why those colors?

<details>
<summary> Click here to see the colour palette </summary>
<br>

I created the colour palette with [coloors](https://coolors.co/).<br>
![Colour palette ](documentation/readme/)<br>

</details>

### Structure 

The flowchart was crafted during the planning phase of the project and was created with [Lucid](https://lucid.app/). It still displays a third topic (Food/Drinks), that I would love to implement in the future. Furthermore, it has some additional input (smoking/alcohol) that I didn't use in the end. This could be a future enhancement.
<details>
<summary> Site Map </summary>
<br>

![Flowchart](documentation/readme/)

</details>

details>
<summary> Database Schema  </summary>
<br>

![Flowchart](documentation/readme/)

</details>

### Wireframes

<details>
<summary> Home page </summary>
<br>

![Mobile wireframe](documentation/wireframes/)
![Desktop wireframe](documentation/wireframes/)

</details>

<details>
<summary> Wish list Dashboard </summary>
<br>

![Mobile wireframe](documentation/wireframes/)
![Desktop wireframe](documentation/wireframes/)

</details>

## Features

### Existing Features

To learn more about each feature, please click on the respective headline

<details>
<summary> Logo </summary>
<br>

![Screenshot Logo](/documentation/readme_features/)<br>


</details>

<details>
<summary> Login </summary>
<br>

xxx <br>
![Screenshot of the Login](/documentation/readme_features/)<br>

</details>


### Features, which I would like to implement in the future

- xxx

## Bugs

<details>
<summary> TEMPLATES_DIR </summary>
<br>
After I tried to load the home app, I was shown that the template base.html does not exist due to the fact that I recalled the TEMPLATES_DIRS as string. After removing the quotation mark, everything worked.
  <br>
![Screenshot of the error message in Browser](/documentation/bugs/bug_templates_dir.png)<br>
![Screenshot of the error message in Browser](/documentation/bugs/bug_templates_dir2.png)

</details>

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)/ [CSS](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used to save and store the files for the website.
- [Heroku](https://www.heroku.com) was used to deploy the application.
- [VS Code](https://code.visualstudio.com/) was used as IDE. 
- [Lucid](https://lucid.app/) was used to create the Flowchart.
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) to beautify the code
- [LanguageTool](https://languagetool.org/) was used to check the grammar and spelling in the README and the Code. 
- [Coloors](https://coolors.co/image-picker) was used to create the color scheme.
- [Pixelied](https://pixelied.com/convert/jpg-converter/jpg-to-webp) was used to convert jpg images into wepb images.
- [Tinypng](https://tinypng.com/) was used to compress the webp background-image.
- [Pixabay](https://www.pixabay.com/de-de/) was used to search and load the background image.
- [QuickTime Player](https://support.apple.com/en_GB/downloads/quicktime) was used to create for recording the screen.
- [xconvert](https://www.xconvert.com/) was used to convert the screen recording from mov into gif.
- [Browserling](https://www.browserling.com/) was used to test the application on different browsers.

**Libraries and modules used:** <br>
- [sys](https://docs.python.org/3/library/sys.html) was used to get system-specific functions like exit(). It was also necessary for the typing-print effect. 
- [time](https://docs.python.org/3/library/time.html) was used to access the sleep() function for the time delay.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) was used to get access to Google authentication. 
- [gspread](https://docs.gspread.org/en/v5.10.0/) was used for the Google sheets functionality 
- [datetime](https://docs.python.org/3/library/time.html) was used to get the current year and give the copied worksheets a time stamp in the name to make it unique. 
- [colorama](https://pypi.org/project/colorama/) was used to color the text in the terminal.

## Testing

1. **Validator Testing**

- **[HTML Validator](https://validator.w3.org/)**
 
  - result for index.html<br>
    xxx
    1. result with error<br>
    ![HTML results index with errors](documentation/readme/)
    2. final result<br>
    ![HTML results index](documentation/readme/)<br>
  - result for 404.html<br>
  ![HTML results 404 page](documentation/readme/html-validator-404.png)
  <br>



- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**
   - result for styles.css <br>
     
     ![CSS result](documentation/readme/)
     The warning is due to import of the Google fonts.


  - **[CI Python Linter](https://pep8ci.herokuapp.com/#)**

  - result for xx.py<br>
  text 
    ![Python linter result for xx.py](documentation/readme/)<br>




2. **Lighthouse Test** <br>
   To measure the website against performance, accessibility, SEO and best practice, I used [Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=de).<br>
   - result <br>
  
   ![Lighthouse](documentation/readme/)

3. **Manual testing** <br>

| **Test** | **Test Description** | **Expected Outcome** | **Result** |
|:---|:---|:---|:---|
| Header - Logo | Click on the logo to return to main page | Clicking on the logo on each page will return you to the main page | Pass |
| Header - Navbar toggler in mobile view | Click in mobile view on the burger icon to open the navigation | When the burger icon in mobile view is clicked, the navigation should open | Pass |
| Header - Navigation underline | The page you are currently on should be underlined in the menu | After reaching "Home", "About", "Gallery" or "Contact" the corresponding navigation item should be underlined | Pass |
| Header - Navigation link | Click on a term in the navigation bar to go to the corresponding page | Clicking "Home", "About", "Gallery" or "Contact" should take the user to the corresponding page | Pass |



4. **Browser Compatibility**<br>
  The tests were conducted using the following browsers:

- Google Chrome Version 121.0.6167.160 <br>
The following tests were conducted by using [browserling](https://www.browserling.com/) <br>
- Edge Version 118
- Firefox 119
- Opera 104

I have tested the website on Safari on macOS Sonoma 14.3, but unfortunately, it just opens the website and starts the program, but I can’t enter any input.


## Deployment NEEDS UPDATE

### Heroku
This site is deployed using Heroku. To deploy it from its GitHub repository to Heroku, I took the following steps:

1. Create a list of requirements in the requirements.txt file by using the command _pip3 freeze > requirements.txt_
2. Log in (or sign up) to Heroku
3. Click on the _New_ button and select _Create new app_
4. Give it a unique name and choose the region _Europe_
5. Click the *Settings* tab, go to the _Config Vars_ section and click on the _Reveal Config Vars_ button
6. Copy the content of the creds.json file() and paste it into the value field, then name the _Key_ CREDS, like the variable that holds the json file in the run.py file
7. Click the _Add_ button
8. Add a second key _PORT_ and set the value to _8000_
9. Go to the _Buildpacks_ section and click the _Add Buildpacks_ button
10. Select _python_ and click the _Save changes_ button
11. Add a second buildpack: _nodejs_
12. Click the *Deploy* tab, go to the _Deployment method_ section, select _GitHub_ and confirm this selection by clicking on the _Connect to Github_ button
13. Search for the repository name on github _life-in-numbers_ and click the _Connect_ button 
14. Enable the automatic deploy or manually deploy the code from the main branch.<br>

To see the [view of the live site]() click on the _Open app_ button on the top right corner or, if you enabled automatic deploy(step 14), log in to GitHub, navigate to the repository for this project by selecting [*queenisabaer/wishlist*](https://github.com/queenisabaer/wishlist), click on _Deployment_ and choose in the _Environments_ section _life-in-numbers_. On top of the latest deployment is the link to the [live site]().

### Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*queenisabaer/wishlist*](https://github.com/queenisabaer/wishlist)
3. Click at the top of the repository on the **Fork** button on the right side

### Clone this repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*queenisabaer/wishlist*](https://github.com/queenisabaer/wishlist)
3. In the top right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key


## Credits

### Content

- 

### Code

- A great help and inspiration was the [*Django Recipe Sharing Tutorial*](https://www.youtube.com/playlist?list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) by Daisy Mc Girr.
- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [mdn](https://developer.mozilla.org/en-US/)
  - [W3C](https://www.w3.org/)
  - [W3schools](https://www.w3schools.com/)
  - [DevDocs](https://devdocs.io/)
  - [Stack Overflow](https://stackoverflow.com/)
  - Slack Community

### ReadMe

- Still, a big thank you to [Kera Cudmore](https://github.com/kera-cudmore) and all of her tips on what makes a good README.

### Acknowledgments

- I would like to thank my amazing mentor Brian Macharia for his numerous tips and wonderful assistance during the creation of this project. 
- 

**This is for educational use.**