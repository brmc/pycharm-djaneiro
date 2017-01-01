###Models

|abbreviation|template|
|:--|:--|
|fk|<pre>$VAR$ = models.ForeignKey($VAR2$)</pre>|
|m2m|<pre>$VAR$ = models.ManyToManyField($VAR2$)</pre>|
|mauto|<pre>$VAR$ = models.AutoField($VAR2$)</pre>|
|mbigint|<pre>$VAR$ = models.BigIntegerField($VAR2$)</pre>|
|mbool|<pre>$VAR$ = models.BooleanField($VAR2$)</pre>|
|mchar|<pre>$VAR$ = models.CharField($VAR2$, max_length=50)</pre>|
|mcoseint|<pre>$VAR$ = models.CommaSeparatedIntegerField($VAR2$)</pre>|
|mdate|<pre>$VAR$ = models.DateField($VAR2$)</pre>|
|mdatetime|<pre>$VAR$ = models.DateTimeField($VAR2$)</pre>|
|mdecimal|<pre>$VAR$ = models.DecimalField($VAR2$, max_digits=5, decimal_places=2)</pre>|
|mduration|<pre>$VAR1$ = models.DurationField($VAR2$)</pre>|
|memail|<pre>$VAR$ = models.EmailField($VAR2$)</pre>|
|mfile|<pre>$VAR$ = models.FileField($VAR2$)</pre>|
|mfilepath|<pre>$VAR$ = models.FilePathField($VAR2$)</pre>|
|mfloat|<pre>$VAR$ = models.FloatField($VAR2$)</pre>|
|mimg|<pre>$VAR$ = models.ImageField($VAR2$)</pre>|
|mint|<pre>$VAR$ = models.IntegerField($VAR2$)</pre>|
|mip|<pre>$VAR1$ = models.GenericIPAddressField(protocol='$VAR2$', unpack_ipv4=$VAR3$)$END$</pre>|
|mnullbool|<pre>$VAR$ = models.NullBooleanField($VAR2$)</pre>|
|Model|<pre><br>class $VAR1$(models.Model):<br><br>    class Meta:<br>        verbose_name = "$VAR1$"<br>        verbose_name_plural = "$VAR1$s"<br><br>    def __str__(self):<br>        pass<br>    </pre>|
|Model_full|<pre><br>class $VAR1$(models.Model):<br>    $VAR2$# TODO: Define fields here}<br><br>    class Meta:<br>        verbose_name = "$VAR1$"<br>        verbose_name_plural = "$VAR1$s"<br><br>    def __str__(self):<br>        pass<br><br>    def save(self):<br>        pass<br><br>    @models.permalink<br>    def get_absolute_url(self):<br>        return ('')<br><br>    $VAR3$# TODO: Define custom methods here}<br><br>    </pre>|
|mphone|<pre>$VAR$ = models.PhoneNumberField($VAR2$)</pre>|
|mposint|<pre>$VAR$ = models.PositiveIntegerField($VAR2$)</pre>|
|mpossmallint|<pre>$VAR$ = models.PositiveSmallIntegerField($VAR2$)</pre>|
|mslug|<pre>$VAR$ = models.SlugField($VAR2$)</pre>|
|msmallint|<pre>$VAR$ = models.SmallIntegerField($VAR2$)</pre>|
|mtext|<pre>$VAR$ = models.TextField($VAR2$)</pre>|
|mtime|<pre>$VAR$ = models.TimeField($VAR2$)</pre>|
|murl|<pre>$VAR$ = models.URLField($VAR2$)</pre>|
|musstate|<pre>$VAR$ = models.USStateField($VAR2$)</pre>|
|mxml|<pre>$VAR$ = models.XMLField($VAR2$)</pre>|
|o2o|<pre>$VAR$ = models.OneToOneField($VAR2$)</pre>|
|mbigauto|<pre>$VAR1$ = models.BigAutoField($VAR2$)$END$</pre>|
|mbin|<pre>$VAR1$ = models.BinaryField($VAR2$)$END$</pre>|
|mdur|<pre>$VAR1$ = models.DurationField($VAR2$)$END$</pre>|
|mgip|<pre>$VAR1$ = models.GenericIPAddressField(protocol='$VAR2$', unpack_ipv4=$VAR3$)$END$</pre>|
|muuid|<pre>$VAR1$ = models.UUIDField($VAR2$)$END$</pre>|
