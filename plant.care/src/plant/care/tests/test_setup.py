# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plant.care.testing import PLANT_CARE_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plant.care is properly installed."""

    layer = PLANT_CARE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plant.care is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plant.care'))

    def test_browserlayer(self):
        """Test that IPlantCareLayer is registered."""
        from plant.care.interfaces import (
            IPlantCareLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPlantCareLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLANT_CARE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plant.care'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plant.care is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plant.care'))

    def test_browserlayer_removed(self):
        """Test that IPlantCareLayer is removed."""
        from plant.care.interfaces import \
            IPlantCareLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPlantCareLayer,
            utils.registered_layers())
