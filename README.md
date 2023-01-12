# Table of Contents

- [Hangman Game](#hangman-game)
    - [Live Site](#live-site)
    - [Repository](#repository)
    - [Author](#author)
    - [How To Play/Use](#how-to-playuse)
    - [Features](#features)
      - [Implemented Features](#implemented-features)
      - [Future Features](#future-features)
    - [Data Model/ Classes](#data-model-classes)
    - [Testing](#testing)
      - [Validation Testing](#validation-testing)
      - [Manual Testing](#manual-testing)
      - [Defect Tracking](#defect-tracking)
      - [Commenting Code](#commenting-code)
    - [Deployment](#deployment)
      - [Fork the repository](#fork-the-repository)
      - [Heroku](#heroku)
    - [Credits](#credits)
      - [Media](#media)

## Hangman Game

- Hangman is a guessing game where players try to guess the English words chosen by the computer, the player suggests letters and they have a number of tries.

![image](https://user-images.githubusercontent.com/112726044/212087774-b4314842-23d0-4388-9f67-70c779082bf3.png)

## Live Site
https://hangmangames.herokuapp.com/

## Repository 
https://github.com/naragurgel/hangmangame

## Author
Nara Gurgel

## How To Play/Use
- A random word is chosen by the computer.
- The user can type a letter o a word to guess the work chosen by the computer.
- The user can see how many tries they have.
- When the user types a letter, it will show as correct then the letter appear in the word or else it will take a life from the hangman.
- The user can continue typing until the word is guessed or they run out of tries.
- If the user guess the correct word, the game will show a well done message. If the user does not guess it, the game shown a message saying that.
- The user can choose to play again and a new random word will be chosen by the computer.

## Features

### Implemented Features

- User input is transformed to uppercase & leading and trailing spaces are stripped so user has a greater chance of successful input
- Invalid entries are in RED to let user know they had an issue visually
- Successful Guesses are in GREEN to let the user know they had success
- Screen Clears between guesses to avoid user confusion of some previous messaging showing from previous guesses
- Prompts are in BLUE to draw out a different to user
- Other text is in WHITE
- Letters Avaiable are updated based on user’s guesses
- Guessed Letters are updated based on user’s guesses
- Guessed Words are updated based on user’s guesses
- Number of Tries and Stage of Hangman as updated as user makes an incorrect guess

### Future Features
- Require users to login then track wins & losses.
- Top 5 players score with googlesheet.

## Data Model/ Classes
| Class: Hangman Game                          |                                                                                                              |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Parameters:**                              | Type                                                                                                         |
| word                                         | string: word from words list                                                                                 |
| **Methods:**                                 | Retrieve user input in uppercase and stripped                                                                |
| retrieve_yes_no_response(input_value)        | Outputs a boolean value based on the user response (Y/N)                                                     |
| username()                                   | Retrieve username and print greeting in the screen                                                           |
| username()                                   | Retrieve username and print greeting in the screen                                                           |
| display_goodbye()                            | Print goodbye in the screen                                                                                  |
| __init__(self, word)                         | Initialize method, it starts the class off with default parameters as if a user just started to play a game. |
| run_game(self)                               | Run the game until the user ran out of tries or won the game                                                 |
| display_hangman(self)                        | Display all the visual cues for the user to play the game                                                    |
| resolve_guessed_letter(self, guessed_letter) | Decides if the guessed letter existe in the word and update the game                                         |
| resolve_guessed_word(self, guessed_word)     | Decides if the word is the one chosen by the computer                                                        |
| reveal_letters(self, guessed_letter)         | Update the display word to show the position of the guessed letter                                           |
| main()                                       | Greets the user and ask the user if they wants to play the game or not                                       |
|                                              |                                                                                                              |

## Testing

### Validation Testing

- run.py
![image](https://user-images.githubusercontent.com/112726044/212104486-b8cac9ab-8a05-4cf6-af8f-a1d37dc23bce.png)

- words.py
![image](https://user-images.githubusercontent.com/112726044/212104578-4cb052be-5b62-480b-b173-04a4b4fa0da8.png)

- stages.py
![image](https://user-images.githubusercontent.com/112726044/212104641-1279b26c-0480-49de-b4b7-49d43608cacc.png)

### Manual Testing

**Feature 1**
- Welcome message is working.
- Input asking user name is working.
- Input with the question "are you ready to to play" Y/N is working.
- Input to type the letter or word tries is working.
- Number of tries is changine everytime when the users is incorrect. 
- Letters guessed list is working.
- Words guessed list is working.
- Alert when the use insert a invalid input working.
- Alert when the user run out of tries.
- Input asking if the user wants to play again Y/N working.
- Good Bye message working.

### Defect Tracking

- Do you want to Play should have a line return for user input gathering
- If user does invalid input, the message should be RED
- Successful guesses should have messages in GREEN
- Prompts for user input should be BLUE
- Word looks like 1 long line in browser

### Commenting Code
Example of a comment on the code.

![image](https://user-images.githubusercontent.com/112726044/212105048-fc9e80c8-ff96-4a8a-8525-8630c7253ebe.png)

## Deployment
The site was deployed to Heroku pages. The steps to deploy are as follows:

- Log in Heroku.
- Click New and select 'Create new app'
- Choose a name for the app, region and click on 'Create app'.
- Only 'Deploy' and 'Settings' are relevant from the menu section. Starting with the 'Settings' first.
- Now Buildpacks need to be added. They install future dependencies that are needed outside of the requirements file. The first is Python and the second is node.js. Python needs to be selected first and then node.js. Save this selection.
- Now the 'Deploy' section needs to be selected from the menu and connect it to github.
- Enter the name of the repository we want to connect it with and click 'Connect'
- The choice appears now to either deploy using automatic deploys or manual deployment, which deploys the current state of the branch.
- Click deploy branch.

#### Fork the repository
https://github.com/naragurgel/hangmangame

![image](https://user-images.githubusercontent.com/112726044/212092918-9546c3ea-efc3-4bf1-9766-f4dc68ec39dc.png)

### Heroku
🚨**Required** 

1.  New App
Log into Heroku and create a new App  and name it. 

![image](https://user-images.githubusercontent.com/112726044/212093170-04ebd75c-ca49-424c-bee0-8fab26cc4dd2.png)
![image](https://user-images.githubusercontent.com/112726044/212093236-377c61e1-5a54-4c0a-991b-ed2a79af9218.png)

2.  Settings
**Build Packs**

![image](https://user-images.githubusercontent.com/112726044/212093470-52606a0a-a847-41ad-9cbc-516ca6f324ce.png)

  add Python Then Node.js

3. Deploy
A. Set up to github and select the correct repository:

![image](https://user-images.githubusercontent.com/112726044/212093645-99b6e711-2b12-4f0d-88b7-71184fb3a3ac.png)

B. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/112726044/212093733-8f4bf006-7bb7-4bbd-b2be-2f49cf8b7752.png) 

## Credits 

- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.
- [How to build HANGMAN with Python](https://www.youtube.com/watch?v=m4nEnsavl6w)
- [Python Project: Coding Hangman](https://www.youtube.com/watch?v=Ff--def_1q0)
    - Videos from Youtube as inspiration.
- [StackOverflow](https://stackoverflow.com/)
    - General questions about the code.
-[Hangman Stages](https://inventwithpython.com/invent4thed/chapter8.html)
- I would like to say thank you to my mentor Malia, she's very patient, always available to help in the best way possible.

### Media

-[Fontes](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
    - Blog explain how to import fonts to the comand.

