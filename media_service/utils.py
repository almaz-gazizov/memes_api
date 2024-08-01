import boto3
from fastapi import HTTPException


class MinioClient:
    def __init__(
        self, endpoint_url, access_key, secret_key, bucket_name
    ):
        self.s3_client = boto3.client(
            's3',
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        self.bucket_name = bucket_name
        self.create_bucket_if_not_exists()

    def create_bucket_if_not_exists(self):
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
        except:
            self.s3_client.create_bucket(Bucket=self.bucket_name)

    def upload_file(self, file, filename):
        try:
            self.s3_client.upload_fileobj(file, self.bucket_name, filename)
            return f"{self.bucket_name}/{filename}"
        except Exception:
            raise HTTPException(status_code=500, detail="File upload failed")

    def delete_file(self, filename):
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=filename)
        except Exception:
            raise HTTPException(status_code=500, detail="File deletion failed")
