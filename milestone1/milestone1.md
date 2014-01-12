Milestone 1 - Idea, UI/UX, and MVP Features
=========

User research
----------
1. What problem does your application address, and how does your application address it?

    Our application addresses the lack of group-focused exercise tracking applications. We will create an app that allows different groups of people to track their progress, make goals, and give each other encouragement along the way. 
    
    Existing related applications serve to socialize the individual’s workout experience, whereas our goal is to provide a service for existing groups of friends to organize and monitor their progress and fitness over time.
    
2. What are the killer features of your application?
    
    Allow a group of users to share music and playlists, share their workout progress over time, share a combined group fitness goal, socialize and communicate within the group. Progress charts and statistics allow individuals and groups to quickly and easily see their progress over time.
    
    If we have more time, we would also like to project future progress based on your previous logs.

3. Identify and briefly describe your target demographic. Who do you envision using your site?

    Casual athletic clubs, people who want to get in shape and already have friends to work out with (not find people to work out with).

    With extra time, we plan to expand to more professional athletic groups that give more information to the coach/group leader and have more specific and personalized workouts.

4. Develop at least one use case for your site. This should be a list or table demonstrating a sequence of user actions and website responses that occur when a user attempts to complete a core task on your site. Make sure to indicate the task the user is trying to complete.

    **Use Case: User adds workout log to their personal page.**
    
    Click "Add Workout" button -> Pop up window with Workout Type (Pick from a selected list), Feels (smiley face to frowny face depending on how the user feels), Comment box (any additional comments), Picture uploading, Date (default is today’s date, able to change),
    
    Selects workout type in the pop up window -> Form displays appropriate “additional fields.” Some fields include Duration, Mileage/difficulty/laps (specific to the workout), Weight, Calories burnt (automatically calculated by weight, duration and other difficulty), Picture uploading
    
    Selects “Add Another Workout” button  -> Website expands the existing form with another workout section.
    
    Clicks “Submit” button -> Pop up window will close and progress (individual and group) graph will automatically update

    **Use Case: User creates a new group in home page.**
    
    Click “Create New Group” button on home/landing page -> Redirects to another page dedicated to setting up the group. Form with fields Name of group, Location (optional), Group goal, Member name and email address, Picture
    
    If entered member email in database -> Add profile link and avatar on roster
    
    If entered member email not in database -> Dialog box to invite them to join
    
    Click “Submit” button -> Redirect to new group page

Site Design
---------

1. Draw out, by hand, three different designs for this page. Scan these for your submission. 

    **User Page 1**
    
    ![Alt text](/UserPage1.JPG)

    **User Page 2**

    **User Page 3**

2. Make a list of 3 pros and 3 cons for each design.
    
    **User Page 1**

    Pros- Modular design, Focus on the Progress Chart, Whitespace Cons
    
    Cons- Too much focus on Playlists, scrolling for more logs (finding a specific log could take a really long time), Not enough focus on the progress chart

    **User Page 2**

    Pros - Overall, this design is the simplest. The focus on the Graph and keeps the first page simple,  only has “add workout” button without displaying all input fields, can share playlists with other groups and groups with other friends easily in user page. 
    
    Cons- Can’t easily scroll to display recent logs, might be repetitive to manage groups and playlists on user page and also have separate groups and playlists pages (seemed necessary to manage), Only shows three pictures in carousel.

    **User Page 3**

    Pros - Focus on the progress chart, relatively simple, comments/thoughts box to record whatever the user wants
    
    Cons - Playlists not featured on the page, add workout form is limited, user info is in a weird place (usually on the left)

3. Pick the best design and mock it up using an image editing program (i.e. Photoshop or Gimp) or using HTML/CSS. Submit a screenshot of this mockup.

Minimal Viable Product
-------------
1. What features do you plan to implement? How critical are they to the proper functioning of your application?

    * Creating a group/add members to a group
    * Creating a user
    * Making group and personal goals
    * Keeping track of exercise history
    * Making playlists
    * Sharing music/playlists
    * Group page and Individual User page
    * Uploading pictures
    * Graph for progress

2. What features do you plan to leave out? How critical are they to the proper functioning of your application?
    * Projected progress
    * Community page
    * Option to specify the entries at the making of a group for more professional/personalized groups  
    * Trophies

3. Are there any other aspects of your application that are reduced in your MVP? Examples including limited fake datasets, stylistic concerns, security concerns, etc.
    * Security concerns
    * Stylistic concerns
    * Limited fake datasets

Additional Questions
--------

1. Who is in your team? 
    * Jean Michel Rouly (jrouly@gmu.edu, George Mason University, Computer Science B.S., 2015, Undergraduate)
    * Chae Won Lee (registered for credit, chae_93@mit.edu, 18C taken 6.01 and 6.006, 2015, undergrad)
    * Mirim Yoo (mirim@mit.edu, 6-2, 2016, undergrad)
    * Stephanie New (registered for credit, syqnew@mit.edu, 6-3, 2016, undergrad).

2. Which of the themes does your application match best? Be as brief as you can.

    Theme 2: Health&Fitness.

3. What technology do you plan to use for your server-side programming (e.g. PHP, Ruby on Rails, etc)?

    Node.js

4. What risks do you envision preventing you from successfully implementing your idea? Consider this an exercise of imagination, not a test of confidence.
    
    Website could be slow to load because of too many things on one page, and it might be to complicated/overwhelming to use.

    The users may prefer meeting in person to using the website; we run a risk of failing to create a sense of connection as a group. In order to provide motivation through groups, we will implement features such as group goal, news feed that rewards a group achievement (‘everyone worked out this week!’), and a comments section for group encouragement.

5. Are you planning to participate in the competition? If so, are you competing in the main division or the rookie division? Your answer will solely be used for planning purposes.
    
    Yes. Rookie Division.
