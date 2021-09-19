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


## **Testing Based on User Stories**

### **Non Register User**


### **Kids**
- For kids aim was to have a simple and easy screen layout.
  The main page has only 2 buttons with attractive background. One button to enter a new game which provides an option to choose an opponent player. 
  The second button provides instructions about how to play the game. It is assumed that parents will explain instructions to the kids who can not read.
  Images are provided to show different possibilities of winning the game.
  The game page has 3 buttons and the main game layout. The game can be played with only a simple left-click to the correct row. 
  Maximum available spaced tried to use for the game board. 

-   Game with few controls.
    On the main page, there are 2 main buttons and buttons to choose the player. 
    On the game page, there are 3 buttons to refresh/restart the game, go to the homepage and music toggle button. 
    The game can be played simply left-click at the column where the user wanted to put a Pokeball coin.

-   Game which can be played alone or with a friend/family
    Pokeball connects four is a 2 player game. But the option is provided to play against the computer. 
    Currently, the computer is taking random places to put a coin. In a future version of the game, some more logic can be added to computer moves to make the game more challenging.

-   Game to teach strategic thinking
    A basic aim of the game to make strategic moves of the coin to win. Kids will learn to think and observe before making decisions.
    
### **Parents**
-   Destraction free layout
    The layout is quite simple and aims to increase focus while playing the game. On the main page, some animation was added to generate interest. 
    On the game page, big icons are added and most of the space is used for the game board. This page has only 3 controls. 
    Fancy looks and a lot of animation are avoided. 

-   Able to develop logical thinking while playing.
    This game is a logical game and the player has to think before playing his moves. 

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
    


