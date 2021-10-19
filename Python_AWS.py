import pandas as pd
import boto3
import s3fs

s3_bucket = boto3.resource("s3")
s3_client = boto3.client('s3')

#To create bucket
s3_bucket.create_bucket(Bucket='akashbucket03',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})

#To upload files to any perticular bucket
s3_bucket.meta.client.upload_file(r'/home/akash/Aroha/amazon s3 to mysql connection.docx',Bucket='akashbucket03',Key='file2')

#To delete a file from bucket
s3_bucket.Object('akashbucket03','python_mysql_con_sqlalchemy').delete()

#To delete a file from bucket
s3_client.delete_object(Bucket='akashbucket03',Key='python_mysql_con_sqlalchemy')


#To delete Bucket
s3_client.delete_bucket(Bucket= 'akashbucket03')

#Deleteing multiple file from bucket
list1 = []
for buket in s3_bucket.buckets.all():
    for obj in buket.objects.all():
        #print(obj.bucket_name,obj.key)
        if obj.bucket_name == 'akashbucket03':
            list1.append(obj.key)
for i in list1:
    s3_client.delete_object(Bucket='akashbucket03',Key=i)




