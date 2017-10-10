from django import forms
from link.models import Link, BoxObj


class NewLinkForm(forms.ModelForm):
    class Meta:
        model = BoxObj
        fields = ('name', 'url', 'is_link', )

    def save(self):
        is_link = not self.data['is_link']
        try:
            parrent = BoxObj.objects.get(pk=self.data.get('parrent'))
        except BoxObj.DoesNotExist:
            parrent = None
        BoxObj.objects.create(
            name=self.data.get('name'),
            is_link=is_link,
            url=self.data.get('url'),
            parrent_boxes=parrent,
        )
