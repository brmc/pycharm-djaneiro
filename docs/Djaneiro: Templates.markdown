### Templates

|abbreviation|template|
|:--|:--|
|autoescape|<pre><br>{% autoescape $VAR1$ %}<br>	$VAR2$$SELECTION}<br>{% endautoescape %}<br> $END$</pre>|
|block|<pre><br>{% block $VAR1$ %}<br>	$VAR2$$SELECTION}<br>{% endblock $VAR1$ %}<br>	$END$</pre>|
|blocktrans|<pre><br>{% blocktrans %}<br>    $VAR1$$SELECTION}<br>{% endblocktrans %}<br> $END$</pre>|
|comment|<pre><br>{% comment %}<br>	$VAR1$$SELECTION}<br>{% endcomment %}<br>	$END$</pre>|
|csrf|<pre>{% csrf_token %}$END</pre>|
|cycle|<pre>{% cycle $VAR1$%}$END$</pre>|
|debug|<pre>{% debug %}$END$</pre>|
|elif|<pre>{% elif %}$END$</pre>|
|else|<pre>{% else %}$END$</pre>|
|ext|<pre>{% extends "$VAR1$$SELECTION}" %}$END$</pre>|
|extends|<pre>{% extends "$VAR1$$SELECTION}" %}$END$</pre>|
|extrahead|<pre><br>{% block extrahead %}<br>    $VAR1$$SELECTION}<br>{% endblock extrahead %}<br>	$END$</pre>|
|extrastyle|<pre><br>{% block extrastyle %}<br>    $VAR1$$SELECTION}<br>{% endblock extrastyle %}<br>	$END$</pre>|
|filter|<pre><br>{% filter $VAR1$%}<br>	$VAR2$$SELECTION}<br>{% endfilter %}<br> $END$</pre>|
|firstof|<pre>{% firstof $VAR1$%}$END$</pre>|
|for|<pre><br>{% for $VAR1$$VAR2$%}<br>	$VAR3$$SELECTION}<br>{% endfor %}<br>	$END$</pre>|
|fore|<pre><br>{% for $VAR1$$VAR2$%}<br>	$VAR3${% empty %}<br>	$VAR4${% endfor %}<br>	$END$</pre>|
|iblock|<pre>{% block $VAR1$ %}$VAR2$$SELECTION}{% endblock $VAR1$ %}$END$</pre>|
|if|<pre><br>{% if $VAR1$%}<br>	$VAR2$$SELECTION}<br>{% endif %}<br>	$END$</pre>|
|ifchanged|<pre><br>{% ifchanged $VAR1$%}<br>	$VAR2$$SELECTION}<br>{% endifchanged %}<br>	$END$</pre>|
|ife|<pre><br>{% if $VAR1$%}<br>	$VAR2${% else %}<br>	$VAR3${% endif %}<br>	$END$</pre>|
|ifelse|<pre><br>{% if $VAR1$%}<br>	$VAR2${% else %}<br>	$VAR3${% endif %}<br>	$END$</pre>|
|ifeq|<pre><br>{% ifequal $VAR1$$VAR2$%}<br>	$VAR3$$SELECTION}<br>{% endifequal %}<br>	$END$</pre>|
|ifequal|<pre><br>{% ifequal $VAR1$$VAR2$%} <br>	$VAR3$$SELECTION}<br>{% endifequal %}<br>	$END$</pre>|
|ifnotequal|<pre><br>{% ifnotequal $VAR1$$VAR2$%}<br>	$VAR3$$SELECTION}<br>{% endifnotequal %}<br>	$END$</pre>|
|inc|<pre>{% include $VAR1$"$VAR2$"} %}$END$</pre>|
|include|<pre>{% include $VAR1$"$VAR2$"} %}$END$</pre>|
|load|<pre>{% load $VAR1$%}$END$</pre>|
|media|<pre>{{ MEDIA_URL }} $END$</pre>|
|now|<pre>{% now "$VAR1$" %}$END$</pre>|
|regroup|<pre>{% regroup $VAR1$$VAR2$$VAR3$%}$END$</pre>|
|spaceless|<pre><br>{% spaceless %}<br>	$VAR1$$SELECTION}<br>{% endspaceless %}<br>	$END$</pre>|
|ssi|<pre>{% ssi $VAR1$$VAR2$ %}$END$</pre>|
|static|<pre>{% static "$VAR1$$SELECTION}" %}$END$</pre>|
|staticu|<pre>{{ STATIC_URL }} $END$</pre>|
|super|<pre>{{ block.super }}$END$</pre>|
|tag|<pre>{% $VAR1$%}$END$</pre>|
|templatetag|<pre>{% templatetag $VAR1$%}$END$</pre>|
|trans|<pre>{% trans "$VAR1$$SELECTION}" %}$END$</pre>|
|url|<pre>{% url $VAR1$%}$END$</pre>|
|var|<pre>{{ $VAR1$$SELECTION} }}$END$</pre>|
|verbatim|<pre><br>{% verbatim %}<br>	$VAR1$$SELECTION}<br>{% endverbatim %}<br>	$END$</pre>|
|widthratio|<pre>{% widthratio $VAR1$ $VAR2$ $VAR3$ %}$END$</pre>|
|with|<pre><br>{% with $VAR1$$VAR2$%}<br>    $VAR3$$SELECTION}<br>{% endwith %}<br>	$END$</pre>|
