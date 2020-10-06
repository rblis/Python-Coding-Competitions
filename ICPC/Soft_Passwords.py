'''
Your favourite social media website is changing their policy on 
login password validation: a slight error when logging in is now 
acceptable! In particular, assuming the password you chose when 
creating the account is S, a password P

entered while logging in will be accepted if any of the following
 conditions are met:

    P

and S

are identical;

S
can be formed from P

by prepending a single digit (0–9);

S
can be formed from P

by appending a single digit;

S
is equal to P after reversing the case of all letters in P

    .

To reverse the case of a string, replace all uppercase letters with 
their equivalent lowercase letters, and all lowercase letters with their 
equivalent uppercase letters, while leaving all other characters the same. 
For example, the case-reversal of pa55WORD is PA55word.

Any other attempted password P
will be rejected. So for example, if S

is c0deninja5, then c0deninja will be accepted, but not C0deninja5 or c0deninja51.

Write a program which, given alphanumeric strings S
and P, determines whether P

should be accepted.
Input

The first line of the input is the string S
, the stored password, and the second line of input is the password P that
 a user has entered while attempting to log in. Each string consists of only
  digits 0–9, lowercase letters a–z, and uppercase letters A–Z. The strings won’t 
  contain spaces or any other extraneous characters, and will each contain at least 
  one and at most 101

characters.
Output

Print Yes if P
should be accepted according to the above rules, and No otherwise.
'''


password = input()
login = input()
if login == password:
    print('Yes')
elif password[0].isdigit() and password[0] + login == password: 
    print('Yes')
elif password[-1].isdigit() and login + password[-1] == password:
    print('Yes')
else:
    if len(login) != len(password):
        print('No')        
    else:
        result = 'Yes'
        for index, char in enumerate(login):
            if char.isalpha() == False and char != password[index]:
                result = 'No'
                break
            elif char.isupper() and char.lower() != password[index]:
                result = 'No'
                break
            elif char.islower() and char.upper() != password[index]:
                result = 'No'
                break
        print(result)
    
    