Milestone 2 - Minimal Viable Product
=========
Answer the Following Questions
----------
1. Did any of your answers to Milestone 1 change (particularly the Additional Questions and your idea for your site)? Write the numbers for the questions whose answers have changed, and their new answers.
    
Picture sharing feature gone. We are using Django instead of Express. We are adding in features for motivating users such as notifications on group page or user page on progress. We would also like to encourage all members to contribute to the group progress (e.g. Mimum/maximum of how much one member can contribute to group progress chart?)
2. Which features are implemented. To what extent are they complete?
    
We have implemeted user and group creation, login, and playlist creation. As for user creation and login, it’s pretty far from completion as we still need to take care of password security, password retreival, and welcome email. Playlist creation works, but ideally will be hooked up to an external API to retreive song titles. In Create New Group page, users should be able to look up existing members of GroupFit. 
3. Are there any features you wanted to include in your MVP from Milestone 1 that are not complete? If so, which are they?
    
I think the newsfeed will either have to go or won’t be in our MVP by Thursday night. Playlist API retrieval may also not be in complete, but it’s almost there.
The progress analytics that displays a graph of the user/group’s progress is not complete. 
5. What additional features do you wish to implement? How far along on those features are you?
    
For user creation and login part, I wish to implement login through facebook and gmail. I am looking into the documentations for the time being. User progress analytics.

Groups
----------
1. What technologies are you using for the back-end? Include any frameworks if relevant.
    
Django (Python), MySQL, Nginx (for hosting).
2. What technologies are you using for the front-end? Include Javascript frameworks such as jQuery, templating frameworks such as Handlebars.js, and other client-side frameworks such as Ember.js or Backbone.js.
    
Mainly just using Bootstrap. Some JQuery is used, as well as JQuery-UI. We might use dojo.
3. What is the main browser you are targeting? Must be one of our supported browsers.
    
Chrome, Firefox.
4. What implementation unknown / risks are you still facing? Consider this an exercise of imagination, not a test of confidence.
    
There is always the risk that we are targeting a very small fraction of the population that likes exercising (myself not included). 
There is also the risk that the users would find the website less than intuitive. It is a risk allowing users to create groups and automatically invite users to them -- could be seen as spam. Additionally, it is always risky allowing user input that could be displayed on a group or public profile.

Optional question
----------
1. If you are currently in the Rookie Division and would like to switch to the main competition, please let us know.
    
No, we would like to remain in Rookie Division.
