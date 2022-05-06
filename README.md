# [News API](https://newsdaily22.herokuapp.com/)

## By Sarah Kamunya 4/May/2022

## Description

News API is a web appliction helps users with a  list and preview news articles from various sources.   

With the application, a user will be able to:
* Click on an article and read it fully from the news source
* See various news sources and select the ones they prefer.
* See all news sources from the source they selected.
* See Image description and time the news article was created.


### Prerequisites

You need the following to start working on the project on your local computer:

* A computer installed with the following:

```
-Python version 3.8
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone this repository to your local computer.
* Ensure you have python3.8 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual machine.
* Visit https://newsapi.org/ and register for an API key.
* Create start.sh file and in it write the following lines:
```
 export NEWS_API_KEY='<Your-Api-Key>'
 python3.8 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* Alternatively the application can be accessed by visiting https://newsdaily22.herokuapp.com
## Technologies Used

* Python v3.6
* Boostrap
* Flask

## License

MIT License

Copyright (c) 2022 Sarah Kamunya



