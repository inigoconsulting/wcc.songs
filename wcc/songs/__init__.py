from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('wcc.songs')

from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from zope.interface import implements

class HiddenProducts(object):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)

    def getNonInstallableProducts(self):
        return [
            'wcc.songs.upgrades'
        ]

