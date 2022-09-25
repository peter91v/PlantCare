# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import plant.care


class PlantCareLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plant.care)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plant.care:default')


PLANT_CARE_FIXTURE = PlantCareLayer()


PLANT_CARE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLANT_CARE_FIXTURE,),
    name='PlantCareLayer:IntegrationTesting',
)


PLANT_CARE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLANT_CARE_FIXTURE,),
    name='PlantCareLayer:FunctionalTesting',
)


PLANT_CARE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLANT_CARE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlantCareLayer:AcceptanceTesting',
)
