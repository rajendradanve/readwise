# **ReadWise- MS3**
    
![Main Page Responsive Design](./static/images/readwise-responsive-main-page.png)

![Game Page Responsive Design](./static/images/readwise-responsive-all-book-page.png)

For live website [click here](https://read-wise.herokuapp.com/)

For GitHub repository [click here](https://github.com/rajendradanve/readwise)

#   **Table of Content**

 1. [About](#About)
 2. [UX](#UX)
    *   [Project Goals](#project-goals)
    *   [Targeted Audiance](#targeted-audiance)
    *   [User Goals](#player-goals)
    *   [Developer Goals](#developer-goals)
    *   [User Stories](#user-stories)
    *   [Design Choice](#design-choice)
    *   [Wireframes](#wireframes)

 2. [Features](#features)
    *   [Existing Features](#existing-features)
    *   [Features Left to Implement](#features-left-to-implement)

3.  [Technologies Used](#technologies-used)
   
4.  [Testing](#testing)

5. [Deployment](#deployment)

6. [Credits](#credits)

7. [Acknowledgements](#acknowledgements)
  

 # **About**
 This is my third project to exibhit my learning during backend development. 
 For this project I made a website name [ReadWise](https://read-wise.herokuapp.com/).
 ReadWise is the website to register book with summary and other book information and allowing users to add book reviews. 
 This will help book readers to get overview of the books before buying it. Books are categorized based on subject, language and age group. 
 This website also gives direct link to buy this book. Register user can provide star rating and write review about the book. 

 # **UX**

##  **Project Goals**
Goal of this website is to add as much as book information along with user reviews as possible. 
Register user to add different books and reviews for already added book.
Book will provide information such as author, category, age group, language and basic book summary. User will also able to buy book online by  provided buying link. Non register users will able to browse or search book and read book information and reviews.  
Admin (website owner) of the website has authority to add or delete category and language, set book as featured book and delete book. User who added book can also delete their book. 

## **Targeted Audiance**
- This website can be use by any book reader.
- Non register users can browse or search book and read related book information along with reviews.
- Register users can add, delete and provide book review which can help to other readers.


##   **User Goals**

**Goad for Non-register Users** 

* Simple webpage layout    
* Get overview of the some good books at main page.
* Easy navigaton tab to access to all books page.
* Getting good information about book along with reivews if available.
* Easy access to register as new user. Minimal information to fill to register as new user.

**Goal for Register Users**

* Good and simple page layout for all pages.
* Easy access to sign in page.
* Simple accessable page to add new book with proper informaiton such as category, language, age-group, book summary, buying link etc.
* Possibility to add review for the book along with review stars which helps other book readers.
* Possibility to delete book added by register user.

**Goal for Admin**

* Good and simple page layout for all pages which suitable for all users.
* Able to add book. 
* Able to set book as featured or non featured.
* Simple accessable page to add new book with proper informaiton such as category, language, age-group, book summary, buying link etc.
* Possibility to add review for the book along with review stars which helps other book readers.
* Possibility to delete book added by any users.
* Possibility to add or delete category and language.

## **Developer Goals**

To develop the ReadWise website which has
* Shows developer's understanding of backend development along with interactive front end.
* Simple webpages with simple layout which to be accessable by register and also non register users.
* Webpages suitable for all screen sizes. 
        
## **User Stories**

**Non-register User**

* As a non register user, I shall able to access book list and book pages to get more information without registration.
* As a non register user, I want to be able to register as new user on the site.

**Registered User**

* As a registered user, I shall able to sign in and sign out off the site successfully.
* As a registered user, I shall able to access all pages meant for registered users.
* As a registered user, I shall able to add new book. 
* As a registered user, I shall able to add review and star rating to any book.
* As a registered user, I shall able to edit book added by me.
* As a registered user, I shall able to delete book added by me.

**Admin**

* As a admin, I shall able to sign in and sign out off the site successfully.
* As a admin, I shall able to access all pages.
* As a admin, I shall able to add new book. 
* As a admin, I shall able to add review and star rating to any book.
* As a admin, I shall able to edit or delete book added by anyone.
* As a admin, I shall able to add or delete category and language.

## **Design Choice**

- **Framework**

ReadWise used 


Done till this time
- **Colour Scheme**

The main colors used are from got from pokemon theme colors which as mainly yellow, blue, and navy blue color. 
Color codes taken from [this link](https://brandpalettes.com/pokemon-color-codes/)

- **Typography**

Petrona font is mainly used throughout the website with a serif as a backup font in case of any reason the font isn't being imported into the site correctly.
Petrona looks stylish but still clean font to read and correctly goes with a simple design. Fonts are imported using [Google Fonts](https://fonts.google.com/).

- **Pages**

The game has mainly 2 pages. Index.html page for choosing a second player and game.html page for main game page.
Also, the error.html page is designed in case there is an error in the game. 

##  **Wireframes**

*   [Desktop wireframe](assets/wireframe/Wireframe-for-desktop.pdf)

*   [Tablet wireframe](assets/wireframe/Wireframe-For-Tablet.pdf)

*   [Mobile wireframe](assets/wireframe/Wireframe-Phone.pdf)

## **Features**

### **Existing Features**

-   Index Page: The main feature of the index page is to choose an opponent player and provide instruction about how to play the game.
    To justify Pokeball theme page has a background image from pokemon. Also, the page has animated red and yellow Pokeball.
    It is possible to choose a second player as another human or computer. 
    
-   Game Page: The game page has 3 buttons - refresh, home, and music toggle. The main game board has 7 columns and 6 rows.
    One more of the top row is used to insert the coin. When the second player is computer yellow Pokeball coin will be played randomly.

-   Music on and off switch - which allows the users to switch on the music if they would like to. 

-   If any player won or the game is drawn, further coin playing is not possible. 

### **Features Left to Implement**

-   Choosing who will play first in case one of the players is a computer. 

-   Possibility for the player to choose the Pokeball color.

-   Logical moves by the computer when one of the players is a computer.

-   More audio interaction to be added based on how the game is proceeding. 


## **Technologies Used**

**Languages Used**

- [HTML5](https://en.wikipedia.org/wiki/HTML#:~:text=The%20HyperText%20Markup%20Language%2C%20or,displayed%20in%20a%20web%20browser.)

  - The language used to give the site its main structure and all necessary features.

- [CSS3](https://en.wikipedia.org/wiki/CSS)

  - The language used to give the application its visual effects including the font, color, and layout, etc.

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

  - The language used to implement the site's interactive features, allows the users to be interactive and take actions during their visit.

**Frameworks, Libraries & Programs Used**

- [Bootstrap](https://getbootstrap.com/)

    - Bootstrap library is used to create responsive design, beautiful buttons, modal templates.

- [Jquery](https://jquery.com/)

    - Jquery library used to create DOM elements, event handling, animation.

- [Github](https://github.com/)

  - Github is used to create, store and maintain all codes in a repository.

  - Github is also used as the site hosting service for the final website to be published on.

- [Git Version control](https://git-scm.com/)

  - Git 2.30.1 for Mac is used for commit and push codes to Github.

- [Google Fonts](https://fonts.google.com/)

  - The font used for text is imported from google fonts.

- [Fontawesome](https://fontawesome.com/)

  - The icons used for this game are taken from fontawesome.

- [Balsamiq](https://balsamiq.com/)

  - The wireframes were created using Balsamiq.

- [Google DevTools](https://developer.chrome.com/docs/devtools/)

  - Google DevTools was extensively used throughout the project for various styling, testing, and debugging purposes.

- [Am I Responsive](http://ami.responsivedesign.is/)

  - Am I responsive to create the mock-up image presented at the start of this document.

- [W3C Markup Validation service](https://validator.w3.org/)

  - W3C Markup Validation Service has been used to test the HTML codes.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

  - W3C CSS Validation Service has been used to test the CSS codes.

- [Code Beautifier](http://minifycode.com/html-beautifier/)

    -   The tools to minify and beautify JavaScript, CSS, and HTML codes.


## **Testing**

Testing documentation can be found separately at [TESTING.md](TESTING.md)

## **Deployment**

**Deploy To GitHub Pages**

1. Logged into Github account.

2. Select repository.

3. Select connectfour.

4. On the top right navigation click on settings.

5. Under the settings section, scroll down to the GitHub Pages section.

6. Select Main Branch from the source dropdown menu.

7. Click save.

8. Once clicked, this publishes the project to GitHub Pages and displays the site URL. Click on the URL to view the live site.

**Making a clone or download zip to run locally**

1. Log into GitHub account.

2. Select repository.

3. Select connectfour.

4. Click on the Code dropdown button next to the green Gitpod button.

5. Click on the clipboard icon to copy the clone URL.

6. Open Git Bash.

7. Change the current working directory to the location where you want the cloned directory.

8. Type "git clone" in the Command Line and then paste the URL copied in step 5.

9. Press enter to create your local clone.

10. Alternately, click on Download ZIP, unpack locally, and open with a local code editor.

**Forking the GitHub Repository**

1. Log into GitHub.

2. Select repository.

3. Select connectfour.

4. At the very top right corner click "fork".

5. You will have a copy of the original repository in your own GitHub account.

## **Credits**

Connect four is a classic game and my kids love to play this game in their spare time. 
As my son used to play with Pokeball when I got an idea to make this game with a Pokeball theme.
So would like to give credit to my kids for providing me an idea.
All the codes are written by myself after learning from resources. 
The resources and the links I used to learn each concept are the following:

**Code**

- [w3schools](https://www.w3schools.com/) 
    - [audio](https://www.w3schools.com/html/html5_audio.asp)
    - [setTimeout](https://www.w3schools.com/js/js_timing.asp)
    - [CSS background-image](https://www.w3schools.com/cssref/pr_background-image.asp)
    - [Animation using Jquery](https://www.w3schools.com/jquery/jquery_animate.asp)
    - [Hide scrollbar for a page](https://www.w3schools.com/howto/howto_css_hide_scrollbars.asp)

- [Bootstrap](https://getbootstrap.com/)
    -[Bootstrap modal](https://getbootstrap.com/docs/5.0/components/modal/)
    -[Buttons](https://getbootstrap.com/docs/5.0/components/buttons/)

- [Jquery](https://jquery.com/)
    - Jquery overall documentation used to understand concepts mainly for creating and updating DOM, animation, and event handler.

- [MDN Resources](https://developer.mozilla.org/en-US/docs/Web/Reference)
    - MDS resources are used to understand concepts mainly for creating and updating DOM, animation, and event handler.

- For continuous animation of Pokeball at Index.html page help is taken from [this link](https://css-tricks.com/using-multi-step-animations-transitions/)

- For rotation of Pokeball while falling help is taken from [this link](https://css-tricks.com/almanac/properties/t/transform-origin/) 

- Transfering opponent player information from index.html to game.html, help is taken from [this link](https://www.aspsnippets.com/Articles/Redirect-to-another-Page-with-multiple-Parameters-using-JavaScript.aspx)

**Color**

- Color codes taken pokemon theme color palette at [this link](https://brandpalettes.com/pokemon-color-codes/)

- Apart from the above color white and whitesmoke colors are used.

- When all coins are filled in a particular column rgba(197, 192, 192, 0.9) color is used to indicate not possible to enter any coin.

**Media**

- Index page background image taken from [this link](https://wallpapercave.com/w/HrO79ZR)

- Pokeball images extracted from the image found at [this link](https://www.clipartkey.com/search/pokeball/)

- Music file while playing the game is downloaded from [this link](https://www.bensound.com/royalty-free-music/track/ukulele)

- Error page background image is taken from [freepik website](www.freepik.com) and image is downloaded from [this link](https://www.freepik.com/vectors/clouds)
        

## **Acknowledgements**

I would like to thank:

- My mentor Akshat Garg for his encouragement and valuable comments for this project. 
Thanks to his guidance and tips to improve my code.

- Lessons from code institute helped. Used regularly to check if I am following the correct method of coding.

- Help from in the Slack community.

- Tutor support and student care team.

- My kids because of whom I came up with the idea of this project.

Should you have any queries please reach me at rajendradanve@gmail.com.
