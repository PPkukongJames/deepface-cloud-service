import boto3
import os
session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id='Q3AM3UQ867SPQQA43P2F',
    aws_secret_access_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
    endpoint_url='https://play.min.io',
)

local_base_dir = "/home/ec2-user/deepface-service/deepface-cloud-service/resource/pictures"
def download_files_with_prefix(bucket_name, local_base_dir):
    try:
        # ดึงรายการ Object ทั้งหมดใน Bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                object_key = obj['Key']  # ชื่อไฟล์ใน Bucket
                
                # สร้างโฟลเดอร์ตาม Prefix
                local_file_path = os.path.join(local_base_dir, object_key)
                local_dir = os.path.dirname(local_file_path)
                
                # ตรวจสอบว่าโฟลเดอร์มีอยู่หรือไม่ หากไม่มีให้สร้าง
                if not os.path.exists(local_dir):
                    os.makedirs(local_dir)
                    print(f"Created directory: {local_dir}")
                
                # ดาวน์โหลดไฟล์จาก Bucket
                print(f"Downloading {object_key} to {local_file_path}...")
                s3_client.download_file(bucket_name, object_key, local_file_path)
                print(f"Downloaded {object_key} successfully.")
        else:
            print(f"No objects found in bucket '{bucket_name}'")
    except Exception as e:
        print(f"Error: {e}")

# เรียกใช้ฟังก์ชัน
download_files_with_prefix('cs615-termproject-cloud', local_base_dir)
