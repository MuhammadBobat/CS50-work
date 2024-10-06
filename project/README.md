    # SECURE PASSWORD GENERATOR
    #### Video Demo:  https://youtu.be/oqdkopSvQDc
    #### Description:
    My name is Muhammad Bobat (from Manchester, England) and this is my CS50P final project!


    1. The main() function
       >> This is where the program allows a user to input a software that they need a secure password for.

    2. The check_app() function
       >> The return value is inputted into the check_app function to ensure that the user's input is suitable for a software/application.
       >> As well as this, the first letter of the software/application name is saved under the 'first' variable.
       >> This will become the first letter of the subsequent password to act as an indicator.

       >> The main() function then prompts the user for their preferred password length.

    2. The validate() function
       >> This takes in the length variable and ensures that it is an integer between 7 and 15 digits (inclusive), as this is the convential length of passwords.
       >> If these requirements are met, 'True' is returned to the main() function, which triggers the generate() function.

    3. The generate() function
       >> The generate() function takes in the variables 'length' and 'first' as parameters.
       >> Using the string module, a list of alphanumeric characters and other ASCII characters are added to the 'character' array.
       >> This array is then shuffled to ensure a randomized selection of characters for the password.
       >> According to the length of the password inputted by the user, characters from the 'character' array are randomly added to the 'code' array.
       >> This is then outputted as a sequence of randomly generated characters that equate the required length of the password.

    4. The file() function
       >> After printing the new password, the user is prompted with a question that allows them to access an external file with all saved passwords.
       >> If the user inputs 'yes' (or equivalent), then the generated password is appended to the end of the 'passwords.txt' file.
       >> The password is appended in the format - 'Application: Password'
       >> The file is then opened as an external file, available for the user to read.
       >> If the user input 'no' (or equivalent), then the program will end with sys.exit(), printing a final message.

    5. The email_sender() function
       >> After saving the new password to the 'passwords.txt' file, the program calls the email_sender() function from another file that I wrote named 'send_email.py'
       >> This file uses the smtplib, os, and email modules to send an automated email to the user's email containing their saved passwords.
       >> The program firsts prompts the user for their email, then reads the contents of the updated 'passwords.txt' file, before sending it's contents as an email.

    5. The test_project.py file
       >> This file uses pytest to test functions imported from the project.py file.
       >> This ensures that all errors are accounted for and expected results are indeed accurate.
