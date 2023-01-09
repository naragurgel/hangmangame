# Hangman Game
- Screenshot of logo/navigation of mobile deployed site
- Hangman is a guessing game where players try to guess the English words chosen by the computer, the player suggests letters and they have a number of tries.

## Author
Nara Gurgel

## Project Overview
- Include a recording of site that shows the terminal interaction.
  https://chrome.google.com/webstore/detail/loom-for-chrome/liecbddmkiiihnedobmlmillhodjkdmb is a very intuitive and free tool to do a web recording.
- Then you can use https://cloudconvert.com/mp4-to-gif to convert the mp4 to a gif and just paste it into the readme via GitHub, and it'll resolve itself.
- One or two sentences providing an overview of your project.
- Include a link to your deployed website

## Table of Contents
Generate after readme is complete for UX and below

## How To Play/Use
- A random word is chosen by the computer.
- The user can type a letter to guess the word.
- The user can see how many tries they have.
- When the user types a letter, it will show as correct then the letter appear in the word or else it will take a life from the hangman.
- The user can continue typing until the word is guessed or they run out of tries.
- If the user guess the correct word, the game will show a well done message. If the user does not guess it, the game shown a message saying that.
- The user can choose to play again and a new random word will be chosen by the computer.

## Features

### Home Screen
- This is the home screen when the user open the game.
![image](https://user-images.githubusercontent.com/112726044/211365887-2569946e-158d-4c98-aee6-6c09a5de780a.png)

### Failed tries
- The failed message saying to the user the try was wrong.
![image](https://user-images.githubusercontent.com/112726044/211366039-ae106287-5775-4fbb-a062-1ba8416d2df8.png)

### Guessed tries
- The message saying the letter is correct.
![image](https://user-images.githubusercontent.com/112726044/211366171-a78e44d0-cb3b-4484-91bb-d49c4496f412.png)

### Not valid message
- Not valid input.
![image](https://user-images.githubusercontent.com/112726044/211366274-da7abd25-760f-46ef-a8d9-b610950e6845.png)

### Run out of try message
- When the user does not guess the word and run out of tries.
![image](https://user-images.githubusercontent.com/112726044/211366457-d50e5d98-077f-43ee-856e-09945fb1d86a.png)

### Future Features
- All letters already used will be displayed on the screen

## Libraries and tools used
- Github to help with the lis of random words
- https://www.online-spellcheck.com/For spell checking

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

**Creating Defects**
1. Click the Issues menu item 
![image](https://user-images.githubusercontent.com/23039742/169566835-240ce89c-6ab1-45b6-8ee8-5f693de70e5d.png)

2. click the Green New Issue button
![image](https://user-images.githubusercontent.com/23039742/169567026-07ff2fb7-ebc0-4ce0-b8a8-38ab7da8844b.png)

3. Fill in the default form
![image](https://user-images.githubusercontent.com/23039742/169567286-c85218d1-1118-4472-93be-04eda040ecc5.png)
 - Fill in a descriptive title
 - add steps to reproduce if it's not straight forward
 - include a screenshot
<img width="967" alt="image" src="https://user-images.githubusercontent.com/23039742/169567840-255b514c-0a1e-4514-8593-9c2aab295b6e.png">
4. click the submit New issue button

**Closing Defects**
1. Go to the issue list in GitHub and click on the issue you have fixed 
<img width="1476" alt="image" src="https://user-images.githubusercontent.com/23039742/169568053-6e34b94c-ff31-4d7f-9faf-1d04286f0397.png">

2. Add a brief write up of what you fixed and include a screenshot if necessary then Click the Close with Comment Button
![image](https://user-images.githubusercontent.com/23039742/169570025-6d559641-d573-4749-bc0f-33a151358481.png)

**Reopening Defects**
1. If you find you didn't fix the issue, you can toggle to the closed items:
![image](https://user-images.githubusercontent.com/23039742/169570117-274898ec-ee02-487a-ac14-4755095d5e8a.png)

2. Click on the issue you want to re-open
3. Scroll down and click the re-open button
![image](https://user-images.githubusercontent.com/23039742/169570383-9fc53595-1761-4117-a369-d798877c7fe2.png)


### Defects of Note
Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and link to them directly here.


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


#### New Project
Log into Heroku and create a new project. Name it something like XXX_coders_bistro.


#### Settings
On the settings tab you have to address two things:
1. **Config Vars**

  ![image](https://user-images.githubusercontent.com/23039742/132135869-215d2e0f-805d-40a8-a8c2-fb1098e2645d.png)

  At a bar minimum you should show the user that they need to add the PORT. 8000 key value pair.


2. **Build Packs**

  ![image](https://user-images.githubusercontent.com/23039742/132135918-28cac112-7766-4277-905c-4a4963d8442d.png)

  add Python Then Node.js


#### Deploy
1. Set up to github and select the correct repository:

  ![image](https://user-images.githubusercontent.com/23039742/132136113-c257c921-d10c-4ccc-af09-6a1d25136395.png)

2. Deploy either manual or automatic

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
