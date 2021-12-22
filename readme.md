# Pets Shop Backend
* Pets Shop project that is specialized in selling dogs according to breed.
* Project is built using `Dhango RestFramework` and `sqlite DB`
* Testing using `coverage`

## Project Setup
install dependencies `pip install -r requirements.txt`

Iitialize DB:

 1. create model migration files  `python manage.py makemigrations`
 2. Apply migration files to DB `python manage.py migrate`

Create a Super User` python manage.py createsuperuser`


## Action scripts
To run server: `python manage.py runserver`

To run tests: `python manage.py test`

to run coverage tests: `coverage run --source='.' manage.py test`

to generate coverage report: `coverage report`

# API Documentation
Development URL: `http://127.0.0.1:8000`

## Pet
 ### List Breeds
 Description: List all dog breeds  
 Endpoint: `/pet/breed_category/`  
 Request Method: `GET`  

 ### Create New Breed
 Description: Create new dog breed  
 Endpoint: `/pet/breed_category/`  
 Request Method: `POST`  
 Request Body: 
 ```
 {  
    name: string  
 }
 ```

## Dog
 ### List Dogs By Breed
 Description: List all dogs with a given breed
 Endpoint: `/pet/dog_breed/`  
 Request Method: `GET` 
 Query Parameters: 
 * breed_id: `Id (PK) of breed model`

 ### Create New Dog
 Description: Create a new dog
 Endpoint: `/pet/dog_breed/`  
 Request Method: `POST` 
 Request Body: 
 ```
 {  
    age: number,  
    gender: string ("M" for male and "F" for female),  
    breed: number (id of the breed),  
    isVaccinated: boolean  
 }
 ```

 ### Update Dog
 Description: Update dog details
 Endpoint: `/pet/dog_breed/`  
 Request Method: `PUT` 
 Request Body: 
 ```
 {  
    dog_id: number
    age: number --optional--,  
    gender: string ("M" for male and "F" for female)  --optional--,  
    breed: number (id of the breed)  --optional--,  
    isVaccinated: boolean  --optional--   
 }
 ```

 ### Delete Dog
 Description: Update dog details
 Endpoint: `/pet/dog_breed/`  
 Request Method: `DELETE` 
 Request Body: 
 ```
 {  
    dog_id: number
 }
 ```


## Order
 ### Create New Order
 Description: Create a new dog purchase order
 Endpoint: `/order/create/`  
 Request Method: `POST` 
 Request Body: 
 ```
 {  
    price: number,  
    currency: string,  
    dog_id: number (id of the dog)  
 }
 ```




  
