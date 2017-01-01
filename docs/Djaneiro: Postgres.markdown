### Postgres

|abbreviation|template|
|:--|:--|
|farray|<pre>$VAR1$ = SimpleArrayField(base_field=$VAR2$, max_length=$VAR3$, min_length=$VAR4$)$END$</pre>|
|fdaterange|<pre>$VAR1$ = DateRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$</pre>|
|fdatetimerange|<pre>$VAR1$ = DateTimeRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$</pre>|
|ffloatrange|<pre>$VAR1$ = FloatRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$</pre>|
|fhstore|<pre>$VAR1$ = HStoreField($VAR2$)$END$</pre>|
|fintrange|<pre>$VAR1$ = IntegerRangeField(min_value=$VAR2$, max_value=$VAR3$)$END$</pre>|
|fjson|<pre>$VAR1$ = JSONField($VAR2$)$END$</pre>|
|fsplitarray|<pre>$VAR1$ = SplitArrayField(base_field=$VAR2$, size=$VAR3$, remove_trailing_nulls=$VAR4$)$END$</pre>|
|marray|<pre>$VAR1$ = fields.ArrayField(base_field=$VAR2$, size=$VAR3$)$END$</pre>|
|mbigintrange|<pre>$VAR1$ = fields.BigIntegerRangeField($VAR2$)$END$</pre>|
|mdaterange|<pre>$VAR1$ = fields.DateRangeField($VAR2$)$END$</pre>|
|mdatetimerange|<pre>$VAR1$ = fields.DateTimeRangeField($VAR2$)$END$</pre>|
|mfloatrange|<pre>$VAR1$ = fields.FloatRangeField($VAR2$)$END$</pre>|
|mhstore|<pre>$VAR1$ = fields.HStoreField($VAR2$)$END$</pre>|
|mintrange|<pre>$VAR1$ = fields.IntegerRangeField($VAR2$)$END$</pre>|
|mjson|<pre>$VAR1$ = fields.JSONField($VAR2$)$END$</pre>|
