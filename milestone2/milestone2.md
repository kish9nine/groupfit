Milestone 2 - Minimal Viable Product
Due Wednesday 1/22/14, 6pm
For this milestone, we would like to see that you've made significant progress towards your final product by looking at your MVP. You may wish to review the technical requirements (link to technical requirements on rules page) to ensure that your site meets these requirements.
Remember, your MVP should capture the essence of your application and include your most important or compelling features. As such, your app should go beyond a simple skeleton or scaffold. Users should be able to get the essence of your application via a fully-functional important feature.
Specifically, by this milestone, you should have, at minimum:
A login system. You should be able to distinguish between the case where no one is logged in and the case where a specific user is logged in using a personal username/password combination or a third-party API such as Facebook
Dynamic content. The site should be able to display different content on the same page under different situations.
A database with a "significant" amount of data. We're not going to define number of lines or entries, as long as your database contains enough data to satisfy the two requirements above and be able to generate sufficiently different content given different situations to support your features.
Your most important or compelling feature implemented. While you may decide to forgo some stylistic or other minor details, the vast majority of the functionality should be present.
Answer the following questions:
Did any of your answers to Milestone 1 change (particularly the Additional Questions and your idea for your site)? Write the numbers for the questions whose answers have changed, and their new answers.
Picture sharing feature gone. We are using Django instead of Express. We are adding in features for motivating users such as notifications on group page or user page on progress. We would also like to encourage all members to contribute to the group progress (e.g. Mimum/maximum of how much one member can contribute to group progress chart?)
Which features are implemented. To what extent are they complete?
We have implemeted user and group creation, login, and playlist creation. As for user creation and login, it’s pretty far from completion as we still need to take care of password security, password retreival, and welcome email. Playlist creation works, but ideally will be hooked up to an external API to retreive song titles. In Create New Group page, users should be able to look up existing members of GroupFit. 
Are there any features you wanted to include in your MVP from Milestone 1 that are not complete? If so, which are they?
I think the newsfeed will either have to go or won’t be in our MVP by Thursday night. Playlist API retrieval may also not be in complete, but it’s almost there.
The progress analytics that displays a graph of the user/group’s progress is not complete. 
What additional features do you wish to implement? How far along on those features are you?
For user creation and login part, I wish to implement login through facebook and gmail. I am looking into the documentations for the time being. User progress analytics.
Groups
What technologies are you using for the back-end? Include any frameworks if relevant.
Django (Python), MySQL, Nginx (for hosting).
What technologies are you using for the front-end? Include Javascript frameworks such as jQuery, templating frameworks such as Handlebars.js, and other client-side frameworks such as Ember.js or Backbone.js.
Mainly just using Bootstrap. Some JQuery is used, as well as JQuery-UI. We might use dojo.
What is the main browser you are targeting? Must be one of our supported browsers.
Chrome, Firefox.
What implementation unknown / risks are you still facing? Consider this an exercise of imagination, not a test of confidence.
There is always the risk that we are targeting a very small fraction of the population that likes exercising (myself not included). 
There is also the risk that the users would find the website less than intuitive. It is a risk allowing users to create groups and automatically invite users to them -- could be seen as spam. Additionally, it is always risky allowing user input that could be displayed on a group or public profile.
Optional question:
If you are currently in the Rookie Division and would like to switch to the main competition, please let us know.
No, we would like to remain in Rookie Division.
Submit a PDF (or a ZIP if you have multiple files) to Stellar that addresses each of the bullet points and numbered questions above. Only one person from your group needs to submit this but make sure your teammates are listed.
In addition, please submit your application's URL and a Github (or other hosted version control system) commit URL to the form found on Stellar.
