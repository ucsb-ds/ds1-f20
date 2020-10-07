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

-----

## Tab completion doesn't work 

If you start typing a variable name, press TAB on the keyboard, and nothing happens, there is probably no variable or function that starts with what you typed.

The TAB completion depends on _running the previous cell_ where the variable or function is defined. 
Make sure you run that cell first, and then try again and hit TAB. 
Occasionally, you need to press TAB twice for it to work correctly.



