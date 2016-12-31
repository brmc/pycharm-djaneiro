# **Djaneiro for Pycharm** #

This is a port of the Djaneiro plugin for Sublime Text to Jetbrains'  
Pycharm IDE and the tools used to transpile the Sublime test snippets  
to Jetbrains live templates.

Full details of how the plugin works can be found at their repo on  
github: [https://github.com/squ1b3r/Djaneiro](https://github.com/squ1b3r/Djaneiro)

It's basically a collection of convenient abbreviations encountered when  
building Django applications (with a couple generic python uses)  
specifically aimed at models, forms, views, templates, properties,  
basic python objects, and other commonly typed patterns.

## Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Changelog (Recent changes only)](#changelog)
  * [v1.1](#v11)
  * [v1.0](#v10)
  * [v0.0.1](#v001)
* [Usage](#usage)
  * [Plugin](#plugin)
  * [Transpiler](#transpiler)
* [Additional abbreviations](additional-abbreviations)
  * [Models](#models)
  * [Forms](#forms)
  * [Widgets](#widgts)
  * [Postgres](#postgres)


## Requirements ##

* computer

* pycharm or jetbrains IDE with python plugin.  (pycharm professional or  
intellij ultimate is required to recognize the django-template context)   
  
* electricity

* the commandline transpiler requires `python3.5+`

## Installation ##

The plugin can be installed directly from the jetbrains plugin repositories

## Changelog

### v1.1

*

### v1.0

* converted to an official plugin

### v0.0.1

* ported expansions for models, forms, completions, templates, and general  
python


## Usage

### Plugin

In either *.py or *.html files, type an abbreviation and press \<TAB\>.

Check here for a list of all the abbreviations/snippets:  
[https://github.com/squ1b3r/Djaneiro](https://github.com/squ1b3r/Djaneiro)

See [below](#additional-abbreviations) for a list of abbreviations not  
included with the original plugin

### Transpiler

**The transpiler requires `python3.5+`**

#### YML Template Syntax

Eventually the transpiler will convert both ways between Jetbrains  
and Sublime Text formats, but right now it only converts from Sublime  
to Jetbrains.

It also allows you to write live templates in a simplified `yml`  
format that will be translated to jetbrains live templates.  

For example, the full `xml` template definition for `mauto` looks  
like this:

    <template name="mauto" toReformat="false" toShortenFQNames="true" value="$VAR1$ = models.AutoField($VAR2$)">
        <variable alwaysStopAt="true" defaultValue="&quot;FIELDNAME&quot;" expression="" name="VAR1"/>
        <variable alwaysStopAt="true" defaultValue="" expression="" name="VAR2"/>
        <context>
            <option name="Python" value="true"/>
        </context>
    </template>

Many of the values are the same for all templates, so this is how it  
would look in the shortened `yml` format:

```
- name: mauto
  raw: $:FIELDNAME$ = models.AutoField($$)
```

The variable names follow the convention: `$<variable name>:<default value>`  
where either and/or both are optional. If no variable name is given,  
a generic name will be generated for each anonymous variable. They follow  
the pattern `VAR<index>` and don't care about you or your dreams, so if  
you creatively name your variables VAR1, VAR2, etc, you run the risk  
of screwing things up. I doubt I will try to do anything about this, so  
 if it's important to you, feel free to override `TemplateDefinition.variable_prefix`  


The point is all of the following are valid and produce the same results:

    $VAR1:FIELDNAME$ = models.AutoField($VAR2$)
    $:FIELDNAME$ = models.AutoField($VAR2:$)
    $1:FIELDNAME$ = models.AutoField($:$)
    $VAR1:FIELDNAME$ = models.AutoField($$)

However if you don't like the default values, you can still explicitly  
define each attribute.  Here's the full example:

```
- name: mauto
  raw: $VAR1$ = models.AutoField($VAR2$)
  toShortenFQNames: True
  toReformat: True
  variables:
    - name: VAR1
      defaultValue: FIELDNAME
      alwaysStopAt: True
      Expression: ''
    - name: VAR2
      defaultValue: ''
      alwaysStopAt: True
      Expression: ''
  context:
    - name: Python
      value: True
```

A couple notes:

1. Most attributes map directly to their `xml` counterparts with the  
 exception of `raw` and `template`. They are different ways to provide  
    the `value` attribute on \<template>  
   * `raw` is intended to be used for simple, one-line pieces of code.  
   It has precedence over `template`  
   * `template` is intended for multi-line code.  It is the path of a  
   file
2. Quotation marks are not needed and should not be used except for  
empty values
3. The `yml` file is a list, so multiple related definitions should be  
placed in the same file.  The name of the file will be used for the  
Template Group name following the convention: `Djaneiro_<filename>.xml`  
4. Variable default values defined explicitly in the `variables:`  
section supersede implicit definitions in `raw` or `template`  

#### Command line usage

    python3.5 transpile.py [all] [Models] [Views] [Forms] [Templates] [Python] [custom=path/to/file.xml]

Each of the command line options (except `all` and `custom`) corresponds  
 to a group of snippets/live templates for Sublime text and PyCharm. 
 
 The Sublime Text snippets will be transpiled first being overwritten  
  by the jetbrains templates afterwards.  This is so changes from  
  upstream can be integrated easily while preserving any tweaks made  
  here.
  
If you want to further tweak these templates, create files corresponding  
to the group you want to modify in `modifications/`:

| Djaneiro group | your file |
|:-----------------|:-----------|  
| Djaneiro_Forms.xml | modifications/Forms.yml |
| Djaneiro_Models.xml | modifications/Models.yml |
| Djaneiro_Python.xml | modifications/Python.yml |
| Djaneiro_Templates.xml | modifications/Templates.yml |
| Djaneiro_Views.xml | modifications/Views.yml |


To create your own group of templates pass the `custom=path/to/file.yml`  
 option when running the transpiler.  It can lie anywhere.

`XML` and `YML` data will be generated in modifications/output

## Additional Abbreviations

### Models

### Forms

### Postgres

### Widgets