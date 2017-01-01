### Views

|abbreviation|template|
|:--|:--|
|adminview|<pre><br>class $VAR1$Admin(admin.ModelAdmin):<br>    '''<br>        Admin View for $VAR1$<br>    '''<br>    list_display = ('$VAR2$',)<br>    list_filter = ('$VAR3$',)<br>    inlines = [<br>        $VAR4$Inline,<br>    ]<br>    raw_id_fields = ('$VAR5$',)<br>    readonly_fields = ('$VAR6$',)<br>    search_fields = ('$VAR7$',)<br><br>admin.site.register($VAR1$, $VAR1$Admin)<br>$END$</pre>|
|context|<pre><br>def get_context_data(self, **kwargs):<br>    context = super($VAR1$, self).get_context_data(**kwargs)<br>    return context<br>$END$</pre>|
|createview|<pre><br>class $VAR1$CreateView(CreateView):<br>    model = $VAR1$<br>    template_name = "$VAR2$"<br>$END$</pre>|
|deleteview|<pre><br>class $VAR1$DeleteView(DeleteView):<br>    model = $VAR1$<br>    template_name = "$VAR2$"<br>$END$</pre>|
|detailview|<pre><br>class $VAR1$DetailView(DetailView):<br>    model = $VAR1$<br>    template_name = "$VAR2$"<br>$END$</pre>|
|dispatch|<pre><br>def dispatch(self, request, *args, **kwargs):<br>    return super($VAR1$, self).dispatch(request, *args, **kwargs)<br>$END$</pre>|
|listview|<pre><br>class $VAR1$ListView(ListView):<br>    model = $VAR1$<br>    template_name = "$VAR2$"<br>$END$</pre>|
|stackedinline|<pre><br>class $VAR1$Inline(admin.StackedInline):<br>        '''<br>            Stacked Inline View for $VAR1$<br>        '''<br>      model = $VAR2$$VAR1$}<br>      min_num = $VAR3$<br>      max_num = $VAR4$<br>      extra = $VAR5$<br>      raw_id_fields = ($VAR6$,)<br><br>$END$</pre>|
|tabularinline|<pre><br>class $VAR1$Inline(admin.TabularInline):<br>        '''<br>            Tabular Inline View for $VAR1$<br>        '''<br>      model = $VAR2$$VAR1$}<br>      min_num = $VAR3$<br>      max_num = $VAR4$<br>      extra = $VAR5$<br>      raw_id_fields = ($VAR6$,)<br><br>$END$</pre>|
|templateview|<pre><br>class $VAR1$(TemplateView):<br>    template_name = "$VAR2$"<br>$END$</pre>|
|updateview|<pre><br>class $VAR1$UpdateView(UpdateView):<br>    model = $VAR1$<br>    template_name = "$VAR2$"<br>$END$</pre>|
|view|<pre>def $VAR1$(request):$END$</pre>|
