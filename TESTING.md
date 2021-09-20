This document is made as a part of testing section of ReadWise website.

For live website [click here](https://read-wise.herokuapp.com/)

For GitHub repository [click here](https://github.com/rajendradanve/readwise)

## **HTML**
HTML is validated using online [HTML Validator](https://validator.w3.org/) tool.
All pages showing errors which can be ignored. Errors are shown for jinja and flask templates 

## **CSS**
CSS is validated using online [CSS Validator](https://validator.w3.org/) tool.
-   **style.css :** 
CSS validator did not found any errors. 

## **Javascript**
Javascript is validated using online [JSHint](https://jshint.com/) tool.
-   **script.js :** all JS and jQuery has been passed through the Validator, however, various warnings were presented with regards to the $ in jQuery. This was expected and considered that code is okay to pass.

## **Python**
- **app.py :** Python code with flask template is checked using [PEP8 Online](http://pep8online.com/). No errors found with the code. 


## ** Manual Testing Based on User Stories**

### ** General Testing **
- Chrome Developer Tools were used to test responsiveness on different screen sizes.
- Checked website on different devices available to me which includes desktop, mobile phones.
- Checked website on different browsers such as Google Chrome, Safari, Edge and Firefox.
- Asked friends and family members to go through website to know the issues if any.
- Tested all links working properly.
- All CRUD functions were tested to make sure that they work as intended.

Lighthouse test report
![Lighthouse test report](./static/images/readwise-lighthouse-result.png)

Previously accessibility score was low for the site. Below are the actions taken to improve the score.

- Background colors adjusted to increase contrast. 
- Aria, Aria-label added to the links

### **Non Register User**

- Verified that home page, all book and register user page available for non register users.
- Verified that profile page is not accessible to the non register users.
- Verified that non register user can not submit review before sign up.
- Checked that when non register user tries to register username will be unique. 
- Checked that password is validated before user is register.


### **Register User**

- Verified that user correctly sign in after entering correct username and password.
- Verified that register page is not available to sign in user.
- Verified that review form available to the sign in user as each book page if user did not submitted reviews already.
- Verified that user who has reviewed the book gets message that he already reviewed book.
- Verified that add book and profile pages available for sign in page.
- Verified that after adding book profile page shows book added by user with possibility to edit or delete book.
- Verified that user who added book able to edit book or delete it. 

    
### **Admin**
- Verified that admin correctly sign in after entering correct username and password.
- Verified that all books open correctly for admin and shows edit and delete buttons.
- Verified that review form available for admin and admin can add reviews for the book.
- Verified that add book link showed "featured book" switch option in the form.
- Verified that profile page shows cards for category and langauge with add and delete buttons.
- Verified that add category and delete category works properly.
- Verified that add language and delete language works properly.
- Verified that new language and categories shows in add book form.
- Verified that deleted category and langages removed from add book form.
- Verified that admin can add and edit book. 

### **Adult**
-   Need some brain activity while relaxing
    The game is quite simple and just need to think logically before playing your moves.
    Few controls to enter the game.

Some of the testing cases for parents and adults are already covered in general players and kids players.

## **Further Testing**
*   The Chrome extension [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en) has been run and checked.
*   Website tested on [Mobile-Friendly Test - Google Search Console](https://search.google.com/test/mobile-friendly) and validated correctly.
*   Run style sheet code through [Autoprefixer CSS online](http://autoprefixer.github.io/) and pasted prefixed code back into the style sheet.
*   The website has been checked on devices such as large screens, laptops, tablets, and Android phones of different sizes.
*   The website has been opened on Safari, Chrome, and Mozilla both on phones and laptops to check for any display issues across browsers.
*   My kids, wife, and friends have been asked to provide feedback and if any potential major issues.
*   Website performance is tested using [Google Lighhouse](https://developers.google.com/web/tools/lighthouse) and below are the screenshot from the result
    *   index.html page

        ![Index Page Lighthouse Report](./assets/images/lighthouse-index.png)

    *   game.html page

        ![Game Page Lighthouse Report](./assets/images/lighthouse-game.png)
        
## **Manual Testing**
*   **Index Page**
    *   Checked animation on index page for different screen sizes and if Pokeball size changes with screen. 
    *   Checked if the "New Game" button works properly and opens the modal to choose an opponent player. 
    *   Checked if game instructions buttons "How To Play" works properly and text in the modal is okay in all sizes. 
    *   Checked hovering effect for all buttons works properly. 
    *   Checked if the game redirects correctly to the game page after choosing an opponent player.

*   **Game Page**
    *   Game tested many times checking different winning and draw cases to test if all conditions work. 
        Received the wrong result once while testing but not able to replicate the same case again. Played the game much time afterward to check all cases.
    *   Played game with kids and family members to test game if works as intended.
    *   Checked if all links work properly.
    *   Checked if the music toggle works properly. 
    *   Checked if tooltip text works properly.
    *   Checked if game board layout changed based on screen size (after refresh)

## **Known Bugs**
When computer is playing as a second player and first player perform frequent left clicks very fast it sometime creates problem in terms of number of turns each players get. 
It was not a frequest issue and will be worked on future update of this game. 
    


