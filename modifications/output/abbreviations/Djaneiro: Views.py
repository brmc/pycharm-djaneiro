class Admin(admin.ModelAdmin):
    '''
        Admin View for 
    '''
    list_display = ('',)
    list_filter = ('',)
    inlines = [
        Inline,
    ]
    raw_id_fields = ('',)
    readonly_fields = ('',)
    search_fields = ('',)


admin.site.register(, Admin)

context
createview
deleteview
detailview
dispatch
listview
stackedinline
tabularinline


class asdfdf(TemplateView):
    template_name = "asdsd"

    class MODEL_NAMEUpdateView(UpdateView):
        model = MODEL_NAME
        template_name = "TEMPLATE_NAME"


        
view
