## Table of contents
* [Introduction](#Introduction)
* [Demo](#Demo)
* [Technologies](#technologies)
* [Setup](#setup)
* [CI/CD](#Continues Integration)


## Introduction 
'World Of Games' is a project which demonstrate 3 interactive user games:
* *Memory Game* - a sequence of numbers will appear for 1 second and you have to
guess it back
* *Guess Game* - guess a number and see if you chose like the computer
* *Currency Roulette* - try and guess the value of a random amount of USD in ILS

## Demo
![Alt text](Demo.gif)
	
## Technologies
Project is created with:
* Python 3.10
	
## Setup
To run this project, Download it locally to your Pycharm IDE and Run:
* install python3
* Python3 MainGame.py

## Continues Integration
![Alt text](CI_CD.gif)

## Following stages are demonstrated in the Jenkins pipeline:
1. *Checkout* - repository checkout.
2. *Build* - build our docker image.
3. *Run* - will run our dockerized application. The application will expose the port 8777 on
localhost, and a dummy Scores.txt will be mounted to it in order to server the results for
the tests.
4. *Test* - With our e2e.py file it will selenium test our scores web service and fail the
pipeline if the tests failed.
5. *Finalize* - Will terminate our tested container and push to DockerHub the new image we created.

## Continues integration requires the following prerequisites:
For Jenkins to run all stages successfully
* Master & Node on a Ubuntu 18.04 OS for POC
* To avoid permission issues, you may add jenkins to the sudoers file (Jenkins ALL=(ALL) NOPASSWD: ALL)
* In the 'Tests' folder is the following chromedriver version: 99.0.4844.51-0ubuntu0.18.04.1
* The version of Chrome that will be installed is 99.0.4844.51-0ubuntu0.18.04.1
* 'Finalize - upload image' stage requires changing the 'echo' to 'sh' and adding your own credentials         


Enjoy :smile: 
