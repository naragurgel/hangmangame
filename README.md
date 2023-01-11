# Table of Contents

- [Hangman Game](hangman-game)
    - [Live Site](#live-site)
    - [Repository](#repository)
    - [Author](#author)
    - [Table of Contents](#table-of-contents)
    - [How To Play/Use](#how-to-playuse)
    - [Features](#features)
      - [Implemented Features](#implemented-features)
      - [Future Features](#future-features)
    - [Flow Chart](#flow-chart)
    - [Data Model/ Classes](#data-model-classes)
      - [Class X](#class-x)
    - [Libraries used](#libraries-used)
    - [Testing](#testing)
      - [Validation Testing](#validation-testing)
      - [Manual Testing](#manual-testing)
      - [Defect Tracking](#defect-tracking)
      - [Defects of Note](#defects-of-note)
      - [Outstanding Defects](#outstanding-defects)
      - [Commenting Code](#commenting-code)
    - [Deployment](#deployment)
      - [Fork the repository](#fork-the-repository)
      - [Requirements](#requirements)
      - [Gitpod](#gitpod)
      - [Heroku](#heroku)
    - [Credits](#credits)
      - [Content](#content)
      - [Media](#media)
      - [Acknowledgments](#acknowledgments)

# Hangman Game
- Hangman is a guessing game where players try to guess the English words chosen by the computer, the player suggests letters and they have a number of tries.

GIF

## Live Site
https://hangmangames.herokuapp.com/

## Repository 
https://github.com/naragurgel/hangmangame

## Author
Nara Gurgel

## Table of Contents

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

### Home Screen
- This is the home screen when the user open the game.

### Failed tries
- The failed message saying to the user the try was wrong.

### Guessed tries
- The message saying the letter is correct.

### Letters used 
-All letters already used are displayed on the screen.

### Not valid message
- Not valid input.

### Run out of try message
- When the user does not guess the word and run out of tries.

### You won message
- When the user guess the word.

### Play Again option
- The user can choose whether or not to play again.

### Future Features
- Require users to login then track wins & losses.
- Top 5 players score with googlesheet.

## Data Model/ Classes
In this section write our your data model(s) or classes. 

You might want to include subsections that include how the data in the model is initialized and then the methods that you created to update it through the program.


You can create a table and take a screenshot, or you can write up subsections in markdown:

![image](https://user-images.githubusercontent.com/23039742/130148204-b56406bf-0fff-48f3-9dee-2f3cdbe67cc5.png)

### Class X
To better group the game as an object, I wrote a class representing its properties and had method functions to update those properties: 

**Properties**
- property 1: is a {string} it represents {something} 
- property 2: is a {string} it represents {something} 

**Methods**
- **\_\_init\_\_**: Initialize method, it starts the class off with default parameters as if a user just started to play a game.
- **\_\_str\_\_**: Returns a string representation of the class/object

## Libraries used

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your features and ensure that they all work as intended in an easy and straightforward way for the users to achieve their goals.


### Validation Testing
You should try to ensure you code is valid and follows proper indentation.  In this section you should write up any websites you used to validate your code. As your projects becomes more complex these tools may change.

For each python file in your project, run it through the pep8online validator

- [PEP8 Validator](http://pep8online.com/) include a screenshot of results

Note any errors or warnings you are ignoring and why. 

If the line is too long just add 
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

### Manual Testing

Use Markdown to track how you tested each bit of user input for each valid option, various invalid entries and leading/trailing spaces

**Feature 1**
- [ ] invalid entry, says sorry and repropts
- [ ] no entry, says sorry and reprompts
- [ ] alpha when numeric expected, sorry and reprompts
- [ ] valid entry with leading spaces, trimmed and shows proper next stage
- [ ] valid entry with trailing spaces, trimed and shows proper next stage

You should also call out how you tested any other features such as:
- Welcome Message, recaps user name
- Score update shows current score
- color change for correct vs incorrect
- google sheet updated properly

If you prefer spreadsheets, create a googlesheet and link to it in this section, just make sure you update the permissions to allow anyone to view it.

### Defect Tracking

Try to create issues in real time as it better reflects the daily life of a developer.

The easiest way to track defects is by using GITHUB's Issues to track these as it's really easy to copy/paste screenshots in and then write up how you closed them. At this stage you don't need a custom template or labels, that comes in P4.

### Outstanding Defects
It's ok to not resolve all the defects you found as long as:
- it does not impacting a user from completing a vital function on the website
- it only affects a very small subset of users
- is an extreme edge case that very few users would try

If you know of something that isn't quite right, create an issue and  link to it here and explain why you chose not to resolve it. 

Sometimes it's as simple, word wrapping issue that makes the site look odd at a certain screensize that you just didn't have time to fix due to the impending deadline and lack of skills. It's best to mention it but note why you allowed it to go live than let asccessors think you didn't notice it. 

### Commenting Code

Make sure you  use triple double quotes to document fuctions and classes.
 Here'a  documentation worthy example:
```$python
def yes_no(question):
    """
    Function to ask a simple yes no question of the user.
    :param question: String displayed as the question
    :return: answer: String equal to "1" or "2" representing yes or no respectfully
    """
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1", "2"):
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer

```

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
Make a fork so you have a copy of the repository in your own git hub account: https://github.com/maliahavlicek/portfolio_project_03

![image](https://user-images.githubusercontent.com/23039742/132136504-eb79a6f3-0205-4c82-80c2-eef136ec7e4c.png)


### Gitpod
🚀 **merit & beyond**

This section should describe the process someone would have to go through to get the local working in gitpod.  Such as install requirements.txt  and setting up a creds.json file that is in the gitignore and keeping their workspace.

If you have project settings required such as a creds.json file from the GOOGLE DRIVE API acess, please provide an example of that file in the writeup with the project key values:
```$python
{
    "type": "service_account",
    "project_id": "<YOUR_VALUE>",
    "private_key_id": "<YOUR_VALUE>",
    "private_key": "<YOUR_VALUE>",
    "client_email": "<YOUR_VALUE>",
    "client_id": "<YOUR_VALUE>",
    "auth_uri": "https://accoutns.google.com/0/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cer_url": "https://www.googleapis.com/oauth2/v1/certs",
    "clien_x509_cert_url": "<YOUR_VALUE>"
}
```

If you have any dependencies, you should instruct users to install them
```$python
pip3 install -r requirements.txt
```

### Heroku
🚨**Required** 

This section should describe the process you went through to deploy the project to Heroku. Include screenshots if you think they would make the process easier.

You may want to re-watch the [python essentials deployment video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/?child=first) when writing up this section.


If you have project settings required for Heroku, provide a table of the keys and values.
Do not share your personal keys but either cut them out of the screen shot or say <YOUR_VALUE> and include links on how the user would obtain such values.

1. Fork the repository

Make a fork so you have a copy of the repository in your own git hub account: https://github.com/maliahavlicek/portfolio_project_03

![image](https://user-images.githubusercontent.com/23039742/132136504-eb79a6f3-0205-4c82-80c2-eef136ec7e4c.png)


2.  New Project
Log into Heroku and create a new project. Name it something like XXX_coders_bistro.


3.  Settings
On the settings tab you have to address two things:
A. **Config Vars**

  ![image](https://user-images.githubusercontent.com/23039742/132135869-215d2e0f-805d-40a8-a8c2-fb1098e2645d.png)

  At a bar minimum you should show the user that they need to add the PORT. 8000 key value pair.


B. **Build Packs**

  ![image](https://user-images.githubusercontent.com/23039742/132135918-28cac112-7766-4277-905c-4a4963d8442d.png)

  add Python Then Node.js


4. Deploy
A. Set up to github and select the correct repository:

  ![image](https://user-images.githubusercontent.com/23039742/132136113-c257c921-d10c-4ccc-af09-6a1d25136395.png)

B. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/23039742/132136241-9d76fabb-39f0-4696-bc5f-047398fdaf41.png) 


## Credits

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did. 

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

### Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.
