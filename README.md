# Homework for lecture 4. "Tests"
### **Problem number 1 unit-tests**
From the course "Python: Everyday Programming and Superfast Prototyping" you need to test the program for working with accounting [Lecture 2.1](https://github.com/netology-code/py-homework-basic/tree/master/2.1.functions).
* You should test the basic functions for obtaining information about documents, adding and removing elements from the dictionary.

Test recommendations.
1. If in your functions information was displayed (print), now it is better to return it (return) so that you can test it.
2. Input can be "mocked" with unittest.mock.patch, if there are problems with this, it is better to rewrite the functions so that the data comes through parameters.

### **Problem # 2 Yandex API Autotest**
Let's check the Yandex.Disk REST API is working correctly. Write tests that check the creation of a folder on Drive.
Using the requests library write a unit-test for the correct answer and possible negative tests for the error responses

An example of positive tests:
1. The response code is 200.
2. The result of creating a folder - the folder appears in the list of files.

### **Problem number 3. Additional (optional)**

After using selenium, write a unit-test for authorization on Yandex using the url: https://passport.yandex.ru/auth/

![Bootstrap photo](https://zavistnik.com/wp-content/uploads/2019/12/Testirovshhik.jpeg)