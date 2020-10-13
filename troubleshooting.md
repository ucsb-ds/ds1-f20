---
layout: home
title: Troubleshooting
nav_exclude: false
seo:
  type: Course
  name: DS1 Troubleshooting
---

# Common Troubleshooting Tips
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## NameError: name 'ok' is not defined

If you get an error
```
NameError: name 'ok' is not defined
```

**Solution**: run the code cell that says `from client.api.notebook import Notebook` in it (in Lab01 this cell is in section `1.5 Submitting your work`). You will need to run this cell _every time_ you start a new Jupyter session or restart the kernel. 


## NameError: name 'variable_name' is not defined

If you run your tests and recieve a lot of errors of the form:
```
NameError: name 'variable_name' is not defined
```
you may not have run the cells where these variables were defined. Or, you may have run the cells but then closed the session. 

**Solution**: run the notebook from top to bottom. 
```
Cell -> Run All
```

## TypeError: 'float' object is not callable

Alternatively, you might get `TypeError: 'int' object is not callable`.

This error happens when the variable that we are trying to assign is not correctly defined, which means that something is off on the right side of the assignment sign. 

For example, in Python, we cannot write `y = 2x`, because `2` is a _literal_ and `x` is a _variable_, so we need to make sure that there is an operator between them, which in this case should be a multiplication. 
Re-writing the expression as `y = 2*x` fixes the error.

-----

## Tab completion doesn't work 

If you start typing a variable name, press TAB on the keyboard, and nothing happens, there is probably no variable or function that starts with what you typed.

The TAB completion depends on _running the previous cell_ where the variable or function is defined. 
Make sure you run that cell first, and then try again and hit TAB. 
Occasionally, you need to press TAB twice for it to work correctly.

_Update Oct.8_: We noticed that the tab completion only works within the cell in which the variable is defined. 
We are looking into it to see if the Jupyter notebooks got updated to remove this feature or if it is a setting that we need to change.
Stay tuned!

------

## I downloaded the notebook file but it saves as the (.ipynb.json) extension, so whenever I upload it to Gradescope, it fails.

You need to verify that the extension of the saved notebook file is `.ipynb`.

Occasionally, your operating system will rename it to be `.ipynb.json`, so you need to change it into `.ipynb` with nothing following it.


--------

# Frequently Asked Questions (FAQ)

## I am unable to add this course on GOLD, the error is saying that the 4 digit code is invalid.

Verify that you are registering for the correct section of the class.
You can try registering for another section and see if it works. Note: You can go ahead and attend the lab session that works best for you; no need to switch the registration.

If you are running into a different issue, send an email to the CS Undergraduate Advisor (ugradhelp @ cs.ucsb.edu) to see if we can get some explanation and/or assistance with this issue **and CC Prof. K on your email**. Make sure to include your **PERM number** in that email.


## Where / when the lecture recordings will be posted?

Lecture recordings will be linked on the Schedule page for each corresponding lecture. 

If we are in Weeks 1-2 and you don't see the recordings, that means we haven't been able to upload them just _yet_. 
Please, don't email us or post on Piazza asking about the recordings, doing so will **not** make them appear any faster, since we are trying our best to get them uploaded as quickly as we are able (and as our Internet allows).

We apologize for any inconvenience the delay might have caused. 
We thank you for your patience and understanding. 


## I haven't received an email about being added to Gradescope / Piazza. What should I do?

Please make sure that you are registered for this course on GOLD.

If you are having an issue with your registration, see the question above about adding this course on GOLD.

If you verified that you are enrolled in this course, send Prof. K an email including **[DS 1]** in the subject line and letting her know that you need to be added to Piazza and/or Gradescope.

## I am unable to see the class when I log into Gradescope.

Make sure that you created your account using `@umail.ucsb.edu` (not `@ucsb.edu`).

SBCC students: check which address the Gradescope email was sent to; verify that you are using the email that was in the Gradescope's "To:" field.

## I am unable to see the class when I log into Piazza.

Make sure that you created your account using `@umail.ucsb.edu` (not `@ucsb.edu`).

SBCC students: check which address the Piazza email was sent to; verify that you are using the email that was in the Piazza's "To:" field.

If you have multiple accounts on Piazza with different email addresses, you can add them to you account to merge the accounts:
* (using the browser on the computer), Click the cogwheel in the upper-right corner of the window
* select "[Account/Email Settings](https://piazza.com/account_settings)"
* add your email under "Other emails".

## If we submit our labs onto Gradescope multiple times, will the newest version be the one graded? 

Yes, your latest submission will be the one that's used for grading.

