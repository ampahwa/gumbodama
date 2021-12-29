# The Gumbodama Soup Server Marketplace Service
 
 
## Requirements
Create user\
Delete user\
List their soups\
Add soup to sell\
Purchase soup\
Post Soup Review
 
## Design
Use flask_restx to build an API server\
Handle each major requirement with an API endpoint\
Use Test-Driven-Development to make sure we can test product\
Build server with MongoDB\
Use GitHub actions with Heroku for CI/CD

You can create a user profile by using the /create_user endpoint and providing the username\
You can delete a user profile by using the /delete_user endpoint and providing the username\
You can list all users with /user endpoint\
You can get all the available soups by using the /soup endpoint\
You can add a soup by using the /add_soup endpoint\
You can delete a soup by using the /delete_soup endpoint\
You can add a review for a soup with /post_review endpoint and providing a soup id (not added yet)

## Completed
Six enpoints with tests\
Updated Kanban board\
CI/CD deployment with Github actions\
MongoDB set with remotel access on Heroku



