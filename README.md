As part of the QA Experts course, I worked on a project to solve a code with cipher letters.


<!-- TOC -->
* [Deciphering](#deciphering)
  * [**Part 1: Text mapping**](#part-1-text-mapping)
  * [**Part 2: Text decoding**](#part-2-text-decoding)
  * [**Part 3: File decoding**](#part-3-file-decoding)
<!-- TOC -->

I received a message with ciphertext and solved it using several methods:

# Deciphering

## **Part 1: Text mapping**
Given a ciphertext and a lookup table, I was requested to decipher the text. 

**Solution:**

The code receives ciphertext and passes it to the `get_dictionary_mapping` function, whose purpose is probably to create a mapping of characters or words (such as a mapping for deciphering ciphertext).
The output of the function is printed to the screen.

**For example:**

Given the ciphertext:
`Uif tfdsfu dpef!`

and the mapping (assuming simple Caesar cipher):

<p align="center">
  <img src="images\mapping.jpg" width="700">
</p>

The final result is written the next part


## **Part 2: Text decoding**
The encrypted text encrypted_text is passed to the decipher_text function, which is supposed to decrypt it.
The decrypted text is printed to the screen.

for example:

Ciphertext:
Uif tfdsfu dpef!

Decrypted Text:
The secret code!


## **Part 3: File decoding**
The decipher_file function is loaded on the message.txt file, probably to decrypt its contents.

for example:

Original Encrypted File (message.txt):
Uif tfdsfu dpef!

Decrypted File Content:
The secret code!


Part 4: Data analysis from the file
The get_longest_word_in_a_file function finds the longest words in the results.txt file.
for example:

File Content (results.txt):
The quick brown fox
jumped over the lazy dog

Longest Word:
jumped

The get_number_of_rows_in_a_file function counts the number of rows in the file results.txt.
for example:

Number of Rows:
2

The results are printed to the screen.