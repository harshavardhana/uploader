from minio import Minio

client = Minio('localhost:9000',
               access_key='minio',
               secret_key='minio123',
               secure=False,
)

def upload(bucket_name, object_name, file_path):
    print("uploading {} => {}/{} ..".format(file_path, bucket_name, object_name))
    etag = client.fput_object(bucket_name, object_name, file_path)
    print("uploaded {}/{} .. {}".format(bucket_name, object_name, etag))
    return etag
