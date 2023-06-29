#  This project displays an automation infrastructure for multi-platform quality assurance automated testing to demonstrate my knowledge & capabilities in QA Automation

## About</h2>
This project was built to serve as an automation infrastructure with Selenium WebDriver framework and a Page-Object-Model for testing applications on multiple platforms. 
The infrastructure provides an easy, simple, and quick way to add new tests, and is easily expandable & maintained.     
This work contains testing on 2 different websites in the right way by infrastructural division.    
The project has also the option to read from CSV and XML files and play with their data.    
Jenkins is used to scheduling executions of the Test Suites profiles for each platform (more profiles can be easily added to create different test scenarios) linked into a pipeline.
The Allure Report system is used as the main reporting system.

## Overview
This project performs automated testing of various applications and platforms:

    - Web-based application
    - Web-based application with a DB connection
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
  
  <img width="939" alt="allure with failed test" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/85ec64ce-4204-4b00-98a5-517d1509190b">

- Support for different client browsers 
- Visual testing - Applitools  
- Web Driver  
- Appium Studio integration (Android and IOS)  
- API support
  
<img width="396" alt="api data" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/6057bb72-80c4-46e1-93ce-a0792b68e9f8">

- Electron and Desktop driver
- Database support 
- CI & CD support

<img width="756" alt="ocean jenkins view" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/19ed9fd4-bd10-4ea9-be62-1e29f9626bf3">


### Applications tested:

- **Rottentomatoes and Saucedemo-** Websites that were tested with WebDriver
- **UK Mortgage Calculator-** Mobile application tested with Appium
  
https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/db160237-bd92-4e17-b3fe-d2427ae87507

- **Students-** API server tested with request and response JSON
- **TodoList-** Desktop application tested with ElectronDriver

https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/f6731b65-1c3a-4acc-816e-eed0f65b65e8

- **Windows Calculator-** Desktop application tested with WinAppDriver

https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/236fa6e2-f05b-45ca-a00c-0fefea4f89ee

### Tools & Frameworks:

- Selenium Framework Automation testing on browsers 
- Pytest- Testing Framework 
- REST Assured for API Testing

https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/e684a45a-dc92-429d-9b37-81280a6725a9

- Appium Studio for Mobile Testing
- MySQL Free online Database to store Login Credentials for the Saucedemo site
  
https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/77575512-19d7-4794-8973-fc082ad9451a

- Listeners - interface for generating Logs
- Open new tabs and switch (windows) on the web

https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/0d072581-a6c0-4662-b6fc-64e97569e0cd
  
- Random - python methods
- Jenkins for Automating Test executions & Test Pipelines

https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/d28fc4b1-f4de-4751-a2f5-5f701a679aba

- Allure Reports - Reporting System 

<img width="944" alt="allure report with mobile_electron_desktop" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/a16eb9dd-2422-4f9b-8e65-738211a49d44">

#### Important points:

1. User can't run on the same time the mobile and the desktop tests, because the Appium Studio and the desktop app are working on the same port of 4723. Only if you change the port of one of them you can run them on the same time
2. The JSON server - students.jar was added and is located in the libs folder
3. Configuration file & DB credentials have been redacted - Adding images of them
![image](https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/41707969-1447-4b2f-b6cb-ac717a460943)
![image](https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/6b24d3c4-1453-45c6-9ac4-650483c2028b)
4. Adding the Jenkins general and specific commands for the API, Electron, and desktop tests (they need special options before/after the test):
- The general directory path for all the jobs:

<img width="400" alt="general directory path" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/86b2fa02-ff62-4232-aad9-065963351cba">

- Commands For API:

<img width="634" alt="build steps for api" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/d8d3b5ba-c360-4119-903d-dc74fed04f2b">

- Commands For Electron:

<img width="625" alt="build step for electron" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/5366eafb-7cae-4c82-8605-3158af5b6466">

- Commands For Desktop:
  
<img width="632" alt="build step for desktop" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/b29d60c9-fc3d-446d-9e44-18d93db3beaf">

- Allure command on Jenkins (after you download the plugin)

<img width="631" alt="allure option on jenkins" src="https://github.com/Batela24/Test_Automation_Final__project/assets/135311137/b3b0d1e1-e1fe-4e7b-a5da-f595e137216b">
