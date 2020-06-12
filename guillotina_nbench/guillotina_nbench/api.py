from guillotina import configure
import argparse
import atexit
import json
import ssl

from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim


@configure.service(method='POST', name='@foobar', permission='guillotina.AccessContent')
async def example_service(context, request):
    return {
        'foo': 'bar'
    }


@configure.service(method='POST', name='@listdatastores', permission='guillotina.AccessContent')
async def listdatastores_service(context, request):
    params = await request.json()
    sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslContext.verify_mode = ssl.CERT_NONE
    try:
        service_instance = connect.SmartConnect(host=params['host'],
                                                user=params['username'],
                                                pwd=params['password'],
                                                port=443,
                                                sslContext=sslContext)
        if not service_instance:
            print("Could not connect to the specified host using specified " "username and password")
            return -1

        atexit.register(connect.Disconnect, service_instance)

        content = service_instance.RetrieveContent()
        # Search for all ESXi hosts
        objview = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
        esxi_hosts = objview.view
        objview.Destroy()
        datastores = []
        for esxi_host in esxi_hosts:
            storage_system = esxi_host.configManager.storageSystem
            host_file_sys_vol_mount_info = storage_system.fileSystemVolumeInfo.mountInfo
            for host_mount_info in host_file_sys_vol_mount_info:
                if host_mount_info.volume.type == "VMFS":
                    datastores.append({
                        'host': esxi_host.name,
                        'name': host_mount_info.volume.name,
                        'capacity': host_mount_info.volume.capacity,
                        'blockSize': host_mount_info.volume.blockSize,
                        'uuid': host_mount_info.volume.uuid,
                        'ssd': host_mount_info.volume.ssd,
                        'local': host_mount_info.volume.local,
                        'version': host_mount_info.volume.version
                    })

        return {'datastores': datastores}
    except Exception as e:
        print("Exception")
        print(e)

    return {
        'ERROR': 'Could not do it'
    }
