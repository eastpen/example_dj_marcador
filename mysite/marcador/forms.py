from django.forms import ModelForm

from .models import Bookmark

class BookmarkForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookmarkForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            classes = self.fields[field].widget.attrs.get("class")
            widget = self.fields[field].widget.__class__.__name__

            if widget == "TextInput" or widget == "URLInput" or widget == "Textarea" or widget == "SelectMultiple":
                if classes is not None:
                    classes += " form-control"
                else:
                    classes = "form-control"
                    self.fields[field].widget.attrs.update({'class': classes})

    class Meta:
        model = Bookmark
        exclude = ('date_created', 'date_updated', 'owner')