from five import grok
from Products.ATContentTypes.interfaces.folder import IATFolder
from hurry.filesize import size as readable_size
from hurry.filesize import alternative
from Acquisition import aq_inner
import os
from Products.ATContentTypes.interfaces.file import IATFile
from Products.ATContentTypes.interfaces.topic import IATTopic
from plone.app.collection.interfaces import ICollection
from zope.interface import Interface
from wcc.songs.song import ISong

grok.templatedir('templates')


class IMediaProvider(Interface):

    def get_size():
        pass

    def get_mediafile():
        pass

    def get_url():
        pass

    def get_embed_code():
        pass

class MediaListing(grok.View):
    grok.context(IATFolder)
    grok.name('media_listing')
    grok.require('zope2.View')
    grok.template('media_listing')

    def get_size(self, content):
        return IMediaProvider(content).get_size()

    def get_audio(self, content):
        return IMediaProvider(content).media

    def href(self, content):
        return IMediaProvider(content).get_url()

    def can_display(self, content):
        try:
            IMediaProvider(content)
        except:
            return False
        return True


class CollectionMediaListing(MediaListing):
    grok.context(ICollection)


class TopicMediaListing(MediaListing):
    grok.context(IATTopic)


class FileAdapter(grok.Adapter):
    grok.context(IATFile)
    grok.implements(IMediaProvider)

    def __init__(self, context):
        self.context = context

    def get_size(self):
        return readable_size(len(self.media.data), system=alternative)

    @property
    def media(self):
        return self.context.getField('file').get(self.context)

    def get_url(self):
        media = aq_inner(self.media)
        ext = ''
        url = self.media.absolute_url()
        filename = self.media.getFilename()
        if filename:
            extension = os.path.splitext(filename)[1]
            if not url.endswith(extension):
                ext = "?e=%s" % extension
        return self.media.absolute_url() + ext

class SongAdapter(grok.Adapter):
    grok.context(ISong)
    grok.implements(IMediaProvider)

    def __init__(self, context):
        self.context = context

    @property
    def media(self):
        return self.context.audio_file

    def get_size(self):
        return readable_size(self.media.getSize(), system=alternative)

    def get_url(self):
        return '%s/@@download/audio_file/%s' % (
                    self.context.absolute_url(),
                    self.media.filename
                )


