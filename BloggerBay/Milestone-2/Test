# Milestone 2 - Technology proven

## Role: QA test engineer

### Goal: test infrastructure
* test framework
* framework for system testing
* ensure program's basic functionality
* log issues
## Blogger Bay: Test infrastructure
 
Each level of the hierarchy produces increasing levels of detail.  Test planning should always start at the top and work down. This prevents getting lost
in the weeds and running out of time.

A typical medium-sized app can be built in about 1000 hours of engineering time.  This means that about 250 hours should be spent on testing.  The
testing hierarchy acts as a natural budget for how to spent that time.

 
### Testing levels
 
#### Level 1
High level discussion of testing strategy
Outline the major types of testing that will be done
 
  Manual Acceptance Testing - A person uses the application and observes what happens. The test script describes scenarios that the tester must go through.  
  Django unit test - Automatic tests that may start with a blank database. These tests can be very fine grained or run the entire system.
  Hammer test - These tests execute automatic scenarios that exercise the entire system. 
  Quick test - The test is only used during development to iterate on a single function. 
  Page test - This test runs on “requests” Python package and gets web pages from a live server it is used to see if pages on the internet are changing. 
  Selenium Page test - Firefox and Chrome are used to obtain pages and look for specific HTML elements. 
#Testing will include:    
    *Manual Acceptance testing  
    *Quick test 
    
 
#### Level 2 - Test area
This level outlines the testing that will occur on each major block of functionality.
 
    *Product subsystems 
    *Views 
    *Database 
    *Order processing 
    *User accounts 
    *Reports 
    *Diagnostics 

#### Level 3 - User Story test
Each test area is decomposed into a a number of user stories. 
Each user story is defined as a User Experiance (UX) that is documented in requirements. 
A user test story outlines how the UX will be excersized and verified.  
Examples: User Auth UX, Create New Post UX, Create New Comment UX 
   
#### Level 4 - Test Script
Each user story is decompiled into a number of user scenarios.	
A test scenerio outlines how the user scenario will be excercised and verified.    
EX: Student Auth UX    
        *Student can register    
        *Student can login   
        *Student can logout  
        *Only students can see grades    
#### Level 5 - Test Case
Each User Scenarios is decomposed into a number of specific features that the app implements.   
A Test Case outlines specific behavior to be exercised and what the expected results are.   
Examples: Students can register     
         *Successful registration     
         *Error for bad email, name, or already enrolled  
         *Student can login after registering     
         *Errors prevent student from being enrolled  
