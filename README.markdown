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
* [Additional abbreviations](#additional-abbreviations)
  * [Models](#models)
  * [Forms](#forms)
  * [Postgres](#postgres)
  * [Widgets](#widgets)


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

* Updated templates from upstream
* Included missing fields for models and forms
* Added Postgres model and form fields
* Added Widgets
* Added transpiler to convert between sublime text and jetbrains
* Created yml format to write live templates

Minor changes:

* Added $END$ variables to all templates

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

**The transpiler isn't really stable.  proceed at your own risk**

requirements: 

    python3.5+  
    pyyaml   
    lxml  

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

    python3.5 transpile.py [all|jetbrains|sublime|modifications] [Models] [Views] [Forms] [Templates] [Python] [custom=path/to/file.xml]

The first command parameter determines the import source of the templates.  
If `all` is passed, sublime text templates will be imported first,  
followed by and overwritten by jetbrains templates, followed by and  
overwritten by any custom modifications. This is so changes from  
  upstream can be integrated easily while preserving any tweaks made  
  here.

The remainder of the commands are a list of specific template groups  
to target.  If none are passed, then they will all be transpiled.
  
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

`XML` and `YML` data will be generated in modifications/output.

Also, a markdown table will be created from any modifications or custom  
group and stored in `modifications/output/markdown`

## Additional Abbreviations

###Models

|abbreviation|template|
|:--|:--|
|mbigauto|$VAR1$ = models.BigAutoField($VAR2$)$END$|
|mbin|$VAR1$ = models.BinaryField($VAR2$)$END$|
|mdur|$VAR1$ = models.DurationField($VAR2$)$END$|
|mgip|$VAR1$ = models.GenericIPAddressField(protocol='$VAR2$', unpack_ipv4=$VAR3$)$END$|
|mip|$VAR1$ = models.GenericIPAddressField(protocol='$VAR2$', unpack_ipv4=$VAR3$)$END$|
|muuid|$VAR1$ = models.UUIDField($VAR2$)$END$|

###Forms

|abbreviation|template|
|:--|:--|
|fgip|$VAR1$ = forms.GenericIPAddressField($VAR2$)$END$|
|fip|$VAR1$ = forms.GenericIPAddressField($VAR2$)$END$|
|fuuid|$VAR1$ = forms.UUIDField($VAR2$)$END$|

###Postgres

#### Forms

|abbreviation|template|
|:--|:--|
|farray|$VAR1$ = SimpleArrayField(base_field=$VAR2$, delimiter=$:','$, max_length=$VAR3$, min_length=$VAR4$)$END$|
|fdaterange|$VAR1$ = DateRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$|
|fdatetimerange|$VAR1$ = DateTimeRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$|
|ffloatrange|$VAR1$ = FloatRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$|
|fhstore|$VAR1$ = HStoreField($VAR2$)$END$|
|fintrange|$VAR1$ = IntegerRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$|
|fjson|$VAR1$ = JSONField($VAR2$)$END$|
|fsplitarray|$VAR1$ = SplitArrayField(base_field=$VAR2$, size=$VAR3$, remove_trailing_nulls=$VAR4$)$END$|

#### Models

|abbreviation|template|
|:--|:--|
|marray|$VAR1$ = fields.ArrayField(base_field=$VAR2$, size=$VAR3$)$END$|
|mbigintrange|$VAR1$ = fields.BigIntegerRangeField($VAR2$)$END$|
|mdaterange|$VAR1$ = fields.DateRangeField($VAR2$)$END$|
|mdatetimerange|$VAR1$ = fields.DateTimeRangeField($VAR2$)$END$|
|mfloatrange|$VAR1$ = fields.FloatRangeField($VAR2$)$END$|
|mhstore|$VAR1$ = fields.HStoreField($VAR2$)$END$|
|mintrange|$VAR1$ = fields.IntegerRangeField($VAR2$)$END$|
|mjson|$VAR1$ = fields.JSONField($VAR2$)$END$|

###Widgets

|abbreviation|template|
|:--|:--|
|wcheck|$VAR1$ = forms.CheckboxInput(check_test=$VAR2$)$END$|
|wcheckmulti|$VAR1$ = forms.CheckboxSelectMultiple($VAR2$)$END$|
|wclearablefile|$VAR1$ = forms.ClearableFileInput($VAR2$)$END$|
|wdate|$VAR1$ = forms.DateInput(format=$VAR2$)$END$|
|wdatetime|$VAR1$ = forms.DateTimeInput(format=$VAR2$)$END$|
|wemail|$VAR1$ = forms.EmailInput($VAR2$)$END$|
|wfile|$VAR1$ = forms.FileInput($VAR2$)$END$|
|whidden|$VAR1$ = forms.HiddenInput($VAR2$)$END$|
|wmultihidden|$VAR1$ = forms.MultipleHiddenInput($VAR2$)$END$|
|wnullbool|$VAR1$ = forms.NullBooleanSelect($VAR2$)$END$|
|wnum|$VAR1$ = forms.NumberInput($VAR2$)$END$|
|wpass|$VAR1$ = forms.PasswordInput(render_value=$VAR2$)$END$|
|wradio|$VAR1$ = forms.RadioSelect($VAR2$)$END$|
|wselect|$VAR1$ = forms.Select(choices=$VAR2$)$END$|
|wselectdate|$VAR1$ = forms.SelectDateWidget($VAR2$)$END|
|wselectmulti|$VAR1$ = forms.SelectMultiple($VAR2$)$END$|
|wsplitdatetime|$VAR1$ = forms.SplitDateTimeWidget(date_format=$VAR2$, time_format=$VAR3$)$END$|
|wsplithiddendatetime|$VAR1$ = forms.SplitHiddenDateTimeWidget($VAR2$)$END$|
|wtext|$VAR1$ = forms.TextInput($VAR2$)$END$|
|wtextarea|$VAR1$ = forms.Textarea($VAR2$)$END$|
|wtime|$VAR1$ = forms.TimeInput(format=$VAR2$)$END$|
|wurl|$VAR1$ = forms.URLInput($VAR2$)$END$|
