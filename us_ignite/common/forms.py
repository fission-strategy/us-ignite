from django import forms
from mezzanine.conf import settings
from mezzanine.utils.static import static_lazy as static
import os


class OrderForm(forms.Form):
    order = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        order_choices = kwargs.pop('order_choices', ())
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['order'].choices = order_choices


class TinyMceWidget(forms.Textarea):
    """
    Setup the JS files and targetting CSS class for a textarea to
    use TinyMCE.
    """

    # if tinymce.settings.USE_FILEBROWSER:
    #     mce_config['file_browser_callback'] = "djangoFileBrowser"
    class Media:
        js = (static("django_tinymce/init_tinymce.js"),
              # static(settings.TINYMCE_SETUP_JS))
              )
        css = {'all': (static("mezzanine/tinymce/tinymce.css"),)}


    def __init__(self, *args, **kwargs):
        super(TinyMceWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "mceEditor"