# Your Wish List Maker
Full-Stack Toolkit Portfolio Project - Code Institute

View the deployed site [here.]()<br>

 *Your Wish List Maker* is . 

![Screenshot of the preview of application](documentation/readme/)<br>

## Table of contents

- [User Experience (UX)](#user-experience-(ux))
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

### User stories/Epics

*Your Wish List Maker* is for those who are interested in . 


## Design

- **Imagery:**<br>
 
background image

Logo


  ![Logo for Your Life in Numbers](documentation/readme_features/)<br>

 
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

![Screenshot Logo](documentation/readme_features/)<br>


</details>

<details>
<summary> Login </summary>
<br>

xxx <br>
![Screenshot of the Login](documentation/readme_features/)<br>

</details>


### Features, which I would like to implement in the future

- xxx

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

5. **Bugs**

**BUG 1:**<br>



**Bug 2::** <br>


**Bug 3** <br>


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

- 
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

- I would like to thank my amazing mentor Brian Macheria for his numerous tips and wonderful assistance during the creation of this project. 
- 

**This is for educational use.**