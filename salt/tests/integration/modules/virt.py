# -*- coding: utf-8 -*-
'''
Validate the virt module
'''

# Import Salt Testing libs
from salttesting.helpers import ensure_in_syspath, requires_salt_modules
ensure_in_syspath('../../')

# Import salt libs
import integration


@requires_salt_modules('virt.get_profiles')
class VirtTest(integration.ModuleCase):
    '''
    Test virt routines
    '''

    def test_default_kvm_profile(self):
        '''
        Test virt.get_profiles with the KVM profile
        '''
        profiles = self.run_function('virt.get_profiles', ['kvm'])
        nicp = profiles['nic']['default']
        self.assertTrue(nicp[0].get('model', '') == 'virtio')
        self.assertTrue(nicp[0].get('source', '') == 'br0')
        diskp = profiles['disk']['default']
        self.assertTrue(diskp[0]['system'].get('model', '') == 'virtio')
        self.assertTrue(diskp[0]['system'].get('format', '') == 'qcow2')
        self.assertTrue(diskp[0]['system'].get('size', '') == '8192')

    def test_default_esxi_profile(self):
        '''
        Test virt.get_profiles with the ESX profile
        '''
        profiles = self.run_function('virt.get_profiles', ['esxi'])
        nicp = profiles['nic']['default']
        self.assertTrue(nicp[0].get('model', '') == 'e1000')
        self.assertTrue(nicp[0].get('source', '') == 'DEFAULT')
        diskp = profiles['disk']['default']
        self.assertTrue(diskp[0]['system'].get('model', '') == 'scsi')
        self.assertTrue(diskp[0]['system'].get('format', '') == 'vmdk')
        self.assertTrue(diskp[0]['system'].get('size', '') == '8192')


if __name__ == '__main__':
    from integration import run_tests
    run_tests(VirtTest)
