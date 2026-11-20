from azure.storage.blob import BlobServiceClient

# to connect the storage account in azure
account_name = '1firststorageaccount1'
account_key = 'MorItuLLiIq1d047lEta0Mo2jVRknq7Mqn8U/lt+bCtOTZNdjEdCcEMl1+UTfxhw17yw5DKqBmmx+ASt9WIqCg=='
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# to access to the container in storage account
container_name = '1firstcontainer1'
blob_name = 'ETL.docx'
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)


# to download file content
download_stream = blob_client.download_blob()
blob_content = download_stream.readall()
print(blob_content.decode('utf-8'))

#import codecs

#with codecs.open(blob_content,'r', encoding='utf-8', errors='ignore') as f:
#    print(f)