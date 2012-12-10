from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from wcc.songs import MessageFactory as _
from Products.ATContentTypes.interfaces.folder import IATFolder
from Products.ATContentTypes.interfaces.topic import IATTopic

from hurry.filesize import size as readable_size
from hurry.filesize import alternative
from plone.app.collection.interfaces import ICollection
from plone.multilingualbehavior import directives as pam
from plone.app.dexterity.behaviors.metadata import IBasic

from plone.app.dexterity import PloneMessageFactory as _d
# Interface class; used to define content-type schema.

class ISong(form.Schema, IImageScaleTraversable, IBasic):
    """
    Manage Song
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/song.xml to define the content type
    # and add directives here as necessary.

    pam.languageindependent('title')
    title = schema.TextLine(
        title = _d(u'label_title', default=u'Title'),
        required = True
        )

    pam.languageindependent('description')
    description = schema.Text(
        title=_d(u'label_description', default=u'Description'),
        description = _d(u'help_description', default=u'A short summary of the content.'),
        required = False,
        missing_value = u'',
        )

    pam.languageindependent('audio_file')
    audio_file = NamedBlobFile(
            title=_(u'Audio'),
            description=_('Upload the MP3 or AAC audio file here'),
            required=True,
    )

    pam.languageindependent('score_file')
    score_file = NamedBlobFile(
            title=_(u'Score (PDF)'),
            description=_(u'Upload score PDF of the song here'),
            required=True,
    )

    pam.languageindependent('score_image_file')
    score_image_file = NamedBlobFile(
            title=_(u'Score (TIFF)'),
            description=_(u'Upload score TIFF of the song here'),
            required=True,
    )

    form.order_before(description = '*')
    form.order_before(title = '*')

# View class
# The view will automatically use a similarly named template in
# song_templates.
# Template filenames should be all lower case.

class Index(dexterity.DisplayForm):
    grok.context(ISong)
    grok.template('song')
    grok.require('zope2.View')
    grok.name('view')


class SongListing(grok.View):
    grok.context(IATFolder)
    grok.require('zope2.View')
    grok.name('song_listing')
    grok.template('song_listing')

    def get_size(self, f):
        return readable_size(f.getSize(), system=alternative)


class CollectionSongListing(SongListing):
    grok.context(ICollection)


class TopicSongListing(SongListing):
    grok.context(IATTopic)
