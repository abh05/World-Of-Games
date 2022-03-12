## Table of contents
* [Introduction](#Introduction)
* [Demo](#Demo)
* [Technologies](#technologies)
* [Setup](#setup)

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

$ Python3 MainGame.py

## CI/CD integration requires the following prerequisites:
For Jenkins to run all stages successfully
* Master & Node on a Ubuntu 18.04 OS for POC
* To avoid permission issues, you may add jenkins to the sudoers file (Jenkins ALL=(ALL) NOPASSWD: ALL)
* In the 'Tests' folder is the following chromedriver version: 99.0.4844.51-0ubuntu0.18.04.1
* The version of Chrome that will be installed is 99.0.4844.51-0ubuntu0.18.04.1
* 'Finalize - upload image' stage requires changing the 'echo' to 'sh' and adding your own credentials         



Enjoy :smile: 
