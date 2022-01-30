# SVIP_Hackathon

## Description
This repo was created during a Hackathon for the SVIP (Silicon Valley Internship Program). It contains sample code for training a Logistic Regression model to classify if someone wears a mask or not and a basic Flask API.

## Dependencies
Run the following command to install the dependencies
```
pip3 install -r requirements.txt
```

## Starting the server
To start the server run the following command
```
flask run
```

## Using the API
To POST an image to the server use the following command
```
curl \
  -F "image=@PATH_TO_IMAGE" \
  127.0.0.1:5000/has_mask
```

## Future Steps
* Upgrade the model with a Convolutional Neural Network
* Dockerize the Flask App
* Refactor the code
* Tests
