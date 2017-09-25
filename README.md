# us-ignite

**Deployment**

*STAGING*

The site is hosted on Heroku, using Heroku Pipelines as the main deployment platform. 
The staging site (https://us-ignite-staging.herokuapp.com) is linked directly with Github Master Branch. So whenever 
the code is pushed or merged into the Github repo master branch. The staging site will rebuild itself with the latest 
code automatically.

You do not need to push to Heroku Git separately.

The URL of the Heroku Pipeline is (https://dashboard.heroku.com/pipelines/df0690de-a024-43ba-a087-697449c4d2b2/)

*REVIEW APPS*

When you are building a new feature, please set up a new branch and work from there, when you are ready to review them, 
please submit a merge request (but not merging it). The pipeline will build a *"review app"* automatically from the 
new branch with the settings carried over from the staging environment. You can find the review app URL from the 
pipeline homepage.

When you are ready to implement the new feature, simply merge it into the master branch, and it will be in the staging
site automatically once it is rebuilt.

*DEPLOY TO PRODUCTION*

Deploy to production env is extremely easy, simply click the *"Promote to Production"* button, then you are good to go!

*PIPELINE SETTINGS*

You can update the pipeline settings in *"app.json"* file. For more information, please refer to the official Heroku 
documentation here: (https://devcenter.heroku.com/articles/pipelines)

