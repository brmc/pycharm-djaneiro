# **Djaneiro for Pycharm** #

This is a port of the Djaneiro plugin for Sublime Text to Jetbrains'  
Pycharm IDE.  Kudos to those guys.  Full details and docs can be found at  
their repo on github: [https://github.com/squ1b3r/Djaneiro](https://github.com/squ1b3r/Djaneiro)

It's basically just a bunch of convenient abbreviations.  To be honest, I  
don't even know if Djaneiro does anything else besides abbreviation  
expansions.  I might should look in to that. In any case the abbreviations  
are the only things that I ported.

My original regex to convert the expansion rules was flawed so I had to go in  
and tweak a couple afterwards.  I think I fixed them all, but I haven't  
tested everything, so there might be a couple that are still a little wonky.  
But they are safe to use.  They won't break anything, and are easy enough to  
uninstall.

## Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Changelog (Recent changes only)](#changelog)
  * [v0.0.1](#v001)

## Requirements ##

* computer

* pycharm  
  *it definitely works for **4.0.1**, but im new to pycharm so I dont know if it  
  works on older versions.  If I understand everything right, it should work  
  on intelliJ as well.*

* electricity

## Installation ##

* Clone this repo or just download the `settings.jar` file.

* In Pycharm navigate to `File -> Import Settings ...`

* Open the `settings.jar` file that you just downloaded or its containing dir 

* Restart pycharm.

* Follow the instructions on [squ1b3r's repo](https://github.com/squ1b3r/Djaneiro)

## Changelog

### v0.0.1

* ported expansions for models, forms, completions, templates, and general  
python

