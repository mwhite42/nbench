from eve import Eve
from pymongo import MongoClient
from flask import render_template
from flask import send_from_directory, redirect, jsonify, request
from flask_cors import CORS
from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim
import ssl
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

client = MongoClient('localhost', 27017)
db = client['nbench']
collection = db['benchmark']
app = Eve(__name__, static_folder='static')
CORS(app, resources={r'/*': {'orgins': '*'}})


@app.route('/api/logger', methods=['GET', 'PUSH'])
def log():
    print(request.args)
    print(request.form)
    logger.info("Logging")
    return jsonify('ok')


@app.route('/ping', methods=['GET'])
def alive():
    return jsonify('nbench is running')


@app.route('/mongotest')
def test_me():
    for doc in collection.find({}):
        print(doc)
    return {'test': 'me'}


@app.route("/api/getDatastores", methods=['GET'])
def get_datastores():
    sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslContext.verify_mode = ssl.CERT_NONE
    try:
        #TODO: Get the connection details from Mongo
        service_instance = connect.SmartConnect(host='10.193.170.145',
                                                user='administrator@vsphere.local',
                                                pwd='NetApp!23',
                                                port='443',
                                                sslContext=sslContext
                                                )
        if not service_instance:
            print("Could not connect")
            return jsonify({'error': 'could not connect'})

        content = service_instance.RetrieveContent()
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
                        'blocksize': host_mount_info.volume.blockSize,
                        'capacity': host_mount_info.volume.capacity,
                        'uuid': host_mount_info.volume.uuid,
                        'local': host_mount_info.volume.local,
                        'version': host_mount_info.volume.version,
                        'ssd': host_mount_info.volume.ssd,
                    })
        return jsonify({'datastores': datastores})
    except Exception as E:
        logger.error("Could not connect: {}".format(E))
        return jsonify({'error': 'Could not connect', 'message': E})


if __name__ == '__main__':
    app.run(debug=True)
