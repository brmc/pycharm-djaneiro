###Models

|abbreviation|template|
|:--|:--|
|mbigauto|$VAR1$ = models.BigAutoField($VAR2$)$END$|
|mbin|$VAR1$ = models.BinaryField($VAR2$)$END$|
|mdur|$VAR1$ = models.DurationField($VAR2$)$END$|
|mgip|$VAR1$ = models.GenericIPAddressField(protocol='$VAR2$', unpack_ipv4=$VAR3$)$END$|
|mip|$VAR1$ = models.GenericIPAddressField(protocol='$VAR2$', unpack_ipv4=$VAR3$)$END$|
|muuid|$VAR1$ = models.UUIDField($VAR2$)$END$|
