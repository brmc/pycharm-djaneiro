### Forms

|abbreviation|template|
|:--|:--|
|fbool|<pre>$VAR1$ = forms.BooleanField($VAR2$)$END$</pre>|
|fchar|<pre>$VAR1$ = forms.CharField($VAR2$)$END$</pre>|
|fchoice|<pre>$VAR1$ = forms.ChoiceField($VAR2$)$END$</pre>|
|fcombo|<pre>$VAR1$ = forms.ComboField($VAR2$)$END$</pre>|
|fdate|<pre>$VAR1$ = forms.DateField($VAR2$)$END$</pre>|
|fdatetime|<pre>$VAR1$ = forms.DateTimeField($VAR2$)$END$</pre>|
|fdecimal|<pre>$VAR1$ = forms.DecimalField($VAR2$)$END$</pre>|
|fduration|<pre>$VAR1$ = forms.DurationField($VAR2$)$END$</pre>|
|femail|<pre>$VAR1$ = forms.EmailField($VAR2$)$END$</pre>|
|ffile|<pre>$VAR1$ = forms.FileField($VAR2$)$END$</pre>|
|ffilepath|<pre>$VAR1$ = forms.FilePathField($VAR2$)$END$</pre>|
|ffloat|<pre>$VAR1$ = forms.FloatField($VAR2$)$END$</pre>|
|fimg|<pre>$VAR1$ = forms.ImageField($VAR2$)$END$</pre>|
|fint|<pre>$VAR1$ = forms.IntegerField($VAR2$)$END$</pre>|
|fmochoice|<pre>$VAR1$ = forms.ModelChoiceField($VAR2$)$END$</pre>|
|fmomuchoice|<pre>$VAR1$ = forms.ModelMultipleChoiceField($VAR2$)$END$</pre>|
|fmuchoice|<pre>$VAR1$ = forms.MultipleChoiceField($VAR2$)$END$</pre>|
|fmuval|<pre>$VAR1$ = forms.MultiValueField($VAR2$)$END$</pre>|
|fnullbool|<pre>$VAR1$ = forms.NullBooleanField($VAR2$)$END$</pre>|
|Form|<pre><br>class $VAR1$(forms.Form):<br>    $VAR2$# TODO: Define form fields here}<br>    $END$</pre>|
|fregex|<pre>$VAR1$ = forms.RegexField($VAR2$)$END$</pre>|
|fsdatetime|<pre>$VAR1$ = forms.SplitDateTimeField($VAR2$)$END$</pre>|
|fslug|<pre>$VAR1$ = forms.SlugField($VAR2$)$END$</pre>|
|ftchoice|<pre>$VAR1$ = forms.TypedChoiceField($VAR2$)$END$</pre>|
|ftime|<pre>$VAR1$ = forms.TimeField($VAR2$)$END$</pre>|
|ftmuchoice|<pre>$VAR1$ = forms.TypedMultipleChoiceField($VAR2$)$END$</pre>|
|furl|<pre>$VAR1$ = forms.URLField($VAR2$)$END$</pre>|
|ModelForm|<pre><br>class $VAR1$Form(forms.ModelForm):<br>    class Meta:<br>        model = $VAR1$= ('$VAR2$',)<br>    $END$</pre>|
|fgip|<pre>$VAR1$ = forms.GenericIPAddressField($VAR2$)$END$</pre>|
|fip|<pre>$VAR1$ = forms.GenericIPAddressField($VAR2$)$END$</pre>|
|fuuid|<pre>$VAR1$ = forms.UUIDField($VAR2$)$END$</pre>|
