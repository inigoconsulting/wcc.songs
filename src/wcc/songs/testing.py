from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import wcc.songs


WCC_SONGS = PloneWithPackageLayer(
    zcml_package=wcc.songs,
    zcml_filename='testing.zcml',
    gs_profile_id='wcc.songs:testing',
    name="WCC_SONGS")

WCC_SONGS_INTEGRATION = IntegrationTesting(
    bases=(WCC_SONGS, ),
    name="WCC_SONGS_INTEGRATION")

WCC_SONGS_FUNCTIONAL = FunctionalTesting(
    bases=(WCC_SONGS, ),
    name="WCC_SONGS_FUNCTIONAL")
