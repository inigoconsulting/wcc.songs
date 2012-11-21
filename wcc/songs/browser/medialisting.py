from five import grok
from Products.ATContentTypes.interfaces.folder import IATFolder
from hurry.filesize import size as readable_size
from hurry.filesize import alternative
from Acquisition import aq_inner
import os

grok.templatedir('templates')


class MediaListing(grok.View):
    grok.context(IATFolder)
    grok.name('media_listing')
    grok.require('zope2.View')
    grok.template('media_listing')

    def get_size(self, content):
        return readable_size(len(content.data), system=alternative)

    def get_audio(self, content):
            return content.getField('file').get(content)

    def href(self, content):
        content = aq_inner(content)
        ext = ''
        url = content.absolute_url()
        filename = content.getFilename()
        if filename:
            extension = os.path.splitext(filename)[1]
            if not url.endswith(extension):
                ext = "?e=%s" % extension
        return content.absolute_url() + ext
