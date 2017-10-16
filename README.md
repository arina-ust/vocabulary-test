# vocabulary-test
A simple desktop application that checks the knowledge of words from a given vocabulary file.

OS: Mac OS. 

To run the application you need to download the repository and run the application file 'vocabulary_test.app' which can be found in the 'dist' folder.

Preview:  
https://user-images.githubusercontent.com/32638771/31601375-17cb6b0c-b273-11e7-9d69-0e2ebe0eb356.png

I wrote the vocabulary file based on the first twenty episodes of the podcast 'Coffee Break Spanish' https://itunes.apple.com/ru/podcast/coffee-break-spanish/id201598403?l=en&mt=2 (or found here https://radiolingua.com/coffeebreakspanish/).

The format of 'vocabulary.txt' is the following:

1  
palabra en espanol = english translation  
otra palabra = its english translation

where 1 is an episode number (called unit in the app). This number is displayed after checking the translation of each word.

Possible improvements:
- implement uploading a vocabulary file chosen by the user;
- after finishing a session display the list of words with their translations that were translated incorrectly;
- suggestion of words to tanslate based on past results of the user (those that were translated incorrectly appear more frequently);
- Windows app.
