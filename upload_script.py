import boto3
import os
import mimetypes

# Create S3 client
s3 = boto3.client('s3')

bucket_name = 'your-bucket-name'

website_folder = 'website'

for root, dirs, files in os.walk(website_folder):
    for file in files:
        file_path = os.path.join(root, file)

        s3_path = os.path.relpath(file_path, website_folder)

        content_type, _ = mimetypes.guess_type(file_path)

        s3.upload_file(
            file_path,
            bucket_name,
            s3_path,
            ExtraArgs={
                "ContentType": content_type
            }
        )

print("Website uploaded successfully!")
