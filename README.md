# QuickFinance (Hackers in the Bazaar Project 03)

Link: [https://quickfinance.vercel.app](quickfinance.vercel.app)

### Purpose
The inspiration for this site is educational websites like IXL, leetcode, and Khan Academy, with the hope of taking the best features of that website.

Currently, LeetCode exists for Computer Science majors to practice their coding assesment skills, but *as far as I know*, no equivalent site exists for business majors. 

The primary purpose of this website is to provide an **interactive, almost "addicting" website where users can learn and refine their core finance skills**.

### Open Source
Because I am *not* a business major, its safe to say I don't have the most robust knowledge of finance. This project utilizes a **Question Submission Portal**, where members of the QuickFinance community can submit questions to be peer reviewed and potentially added to the site: [Portal Link](https://github.com/tkusak27/quickfinance)

### Architecture
Currently, the site relies on a Django backend, which uses the Django ```model``` class to instantiate Questions, Types, and Answers in the database.

The database is currently a ```sqlite``` database, which I know is ***unfit for production***, however it currently suits my needs. If I were to scale up, I would definitely switch dbs.

The frontend utilizes ```vue```, which I do not have much experience with, although I have gotten a much better grasp on as of late.

### Future Tasks
Obviously, there is a *lot* left to implement. First and foremost, the user experience is nothing short of horrendous. Additionally, the file structure within this repository is terrible, and I will defintiely make future efforts to compartmentalize components of this repository. And lastly, a final goal is to continue iterating on the progress I have made, with a goal of getting to a functional website that at least 1 Notre Dame student finds helpful.

  
