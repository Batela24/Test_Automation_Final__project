#  This project displays an automation infrastructure for multi-platform quality assurance automated testing to demonstrate my knowledge & capabilities in QA Automation

## About</h2>
This project built to serve as an automation infrastructure with Selenium WebDriver framework and a Page-Object-Model for testing applications on multiple platforms. 
The infrastructure provides an easy, simple, and quick way to add new tests, and is easily expandable & maintained.
This work contains testing on 2 different websites in the right way by infrastructural division.
The project touch also the option to read from CSV and XML files and play with their data.
Jenkins is used to schedule executions of the Test Suites profiles for each platform (more profiles can be easily added to create different test scenarios) linked into a pipeline.
Allure Report system is used as the main reporting system.

## Overview
This project performs automated testing of various applications and platforms:

    - Web based application
    - Web based application with DB connection
    - Mobile application
    - Web API
    - Electron application
    - Desktop application

### Infrastructure includes:

- Project Layers (Extensions, Page objects, Test Cases, Utilities, Workflows) 
- Page object design pattern model 
- External files Support 
- Failure mechanisms 
- Reporting system (including screenshots) 
- Support for different client browsers 
- Visual testing - Applitools  
- Web Driver  
- Appium Studio integration (Android and IOS)  
- API support 
- Electron and Desktop driver 
- Database support 
- CI & CD support

### Applications tested:

- **Rottentomatoes and Saucedemo-** Websites that were tested with WebDriver
- **UK Mortgage Calculator-** Mobile application tested with Appium
- **Students-** API server tested with request and response json
- **TodoList-** Desktop application tested with ElectronDriver
- **Windows Calculator-** Desktop application tested with WinAppDriver

### Tools & Frameworks:

- Selenium Framework Automation testing on browsers 
- Pytest- Testing Framework 
- REST Assured for API Testing 
- Appium Studio for Mobile Testing
- MySQL Free online Database to store Login Credentials for Saucedemo site 
- Listeners - interface for generate Logs
- Open new tabs and switch (windows) on web
- Random - python methods
- Jenkins for Automating Test executions & Test Pipelines 
- Allure Reports - Reporting System 

#### Important points:

1. User can't run on the same time the mobile and the desktop tests, because the Appium Studio and the desktop app are working on the same port of 4723. Only if you change the port of one of them you can run them on the same time.
2. Configuration file & DB credentials have been redacted. Adding images of them.

