# application-deployement-with-login-credentials
It's an application based on NLP model which is deployed online having a login page where users can track and see their previous searches.

requirements.txt contains all the libraries and their versions used for the application.

model.pkl & transformation.pkl are the pickle files excrated from the NLP model file using pickle.

The application is deployed using AWS EC2 instance .
Using MySQL DB all the login information and the previous searches done from the respective user is saved and displayed in the account.

For the EC2 instance,i have used pm2 application which helps keeping the server up and running.

Used:

Language- Python

DataBase- MySQL

Cloud to deploy- AWS EC2 instance

OperatingSystem- Linux 

Other 3rd party apps- Pm2 (https://www.npmjs.com/package/pm2)



