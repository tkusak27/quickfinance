# QuickFinance (Hackers in the Bazaar Project 03)

Link: [https://quickfinance.vercel.app](quickfinance.vercel.app)

## Purpose
The inspiration for this site is educational websites like IXL, leetcode, and Khan Academy, with the hope of taking the best features of that website.

Currently, LeetCode exists for Computer Science majors to practice their coding assesment skills, but *as far as I know*, no equivalent site exists for business majors. 

The primary purpose of this website is to provide an **interactive, almost "addicting" website where users can learn and refine their core finance skills**.

## Subjects
### To Start
To begin, I plan on trying to perfect the "gameplay" for one, simple skill that requires little prior knowledge: calculating ROI. I plan on giving the user a few variables and prompting the user to calculate the correct ROI. I will draw inspiration from IXL's SmartScore, where the user tries to get to the score 100, with each correct response adding points and each incorrect detracting points.

After I have completed a simple application which allows user to repeatedly practice calculating ROI, I plan on continually expanding the number of subjects to be a more exhaustive overview of a business major.

### Open Source?
Because I am *not* a business major, its safe to say I don't have the most robust knowledge of finance. So, I think a perfect use of open source for this project would be to recruit/invite some of my friends to test the gameplay, and suggest/develop their own skills/problems that could be implemented as a part of this website. This would be in addition to the software being open source, of course.

### Architecture
My plan is to create this web application using Django as a backend, primarily because I have experience with it. Because I am trying to "gamify" learning, the frontend will be built using React, which I have less experience with it (hopefully learning a bit of js in paradigms will be of use). For the actual problem sets themselves, I have not decided how I plan to roll them out, although I figure I will need a database of sorts that allows concurrent reads (sqlite ruled out).

### Presentation
I will be presenting this partly complete (1 skill, basic home page set up) project to my class in December. For the final presentation, I plan on including the following pieces to satisfy the requirements:
* Demonstration of the site
* A slideshow which includes steps on how to download the source code, make changes, and ideally a way to add new problems to the website
  
