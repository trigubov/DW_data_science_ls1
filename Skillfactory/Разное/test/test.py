#----------------- Start of code capture -----------------

from pyVmomi import vim
#from com.vmware.vcenter.vcha_client import Cluster
from pyVim.connect import SmartConnect
from tools import service_instance, cli

#si = service_instance.connect(args)
import configparser
config = configparser.ConfigParser()
config.read("config.txt")
si = SmartConnect(**config["VSphere"])


# http://pubs.vmware.com/vsphere-55/topic/com.vmware.wssdk.apiref.doc/vim.SearchIndex.html
search_index = si.content.searchIndex


#---------------CheckClone_Task---------------
vm = search_index.FindByUuid(None, "vm-32292025", True, True)   #SearchIndex
folder = search_index.FindByUuid(None, "group-v1002", True, True)   #SearchIndex
name = 'netbackup-clone-test'
spec = vim.vm.CloneSpec()
spec.template = False
spec.powerOn = False
spec.location = vim.vm.RelocateSpec()
spec_location_disk_0 = vim.vm.RelocateSpec.DiskLocator()
spec_location_disk_0.datastore = search_index.FindByUuid(None, "datastore-1019", True, True)   #SearchIndex
spec_location_disk_0.diskId = 2000
spec_location_disk_1 = vim.vm.RelocateSpec.DiskLocator()
spec_location_disk_1.datastore = search_index.FindByUuid(None, "datastore-1019", True, True)   #SearchIndex
spec_location_disk_1.diskId = 2002
spec_location_disk_2 = vim.vm.RelocateSpec.DiskLocator()
spec_location_disk_2.datastore = search_index.FindByUuid(None, "datastore-1019", True, True)   #SearchIndex
spec_location_disk_2.diskId = 2001
spec.location.disk = [spec_location_disk_0,
spec_location_disk_1,
spec_location_disk_2]
spec.location.folder = search_index.FindByUuid(None, "group-v1002", True, True)   #SearchIndex
spec.location.datastore = search_index.FindByUuid(None, "datastore-1019", True, True)   #SearchIndex
spec.location.deviceChange = []
spec.location.service = vim.ServiceLocator()
spec.location.service.credential = vim.ServiceLocator.SAMLCredential()
spec.location.service.credential.token = 'Sensitive data is not recorded'
spec.location.service.sslThumbprint = 'C7:D6:5D:2B:69:39:69:68:8F:7F:23:C8:DA:E3:BC:BB:47:FF:FD:2F'
spec.location.service.instanceUuid = '6a2099f8-c6c2-4fe7-b7f7-7299259375a3'
spec.location.service.url = 'https://splc-vc02.plc.rshb.ru:443/sdk'
spec.location.host = search_index.FindByUuid(None, "host-1012", True, True)   #SearchIndex
spec.location.pool = search_index.FindByUuid(None, "resgroup-1007", True, True)   #SearchIndex
managedObject.CheckClone_Task(vm, folder, name, spec, None)   # VirtualMachineProvisioningChecker-ProvChecker

