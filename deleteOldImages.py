"""
Deletes images from s3 and from the database that are more than 180 days old
"""
import boto3, psycopg2
import psycopg2.extras
from datetime import datetime

conn = psycopg2.connect("dbname='allstaradmin_production' user='username' host='localhost' password='password'")

try:
	with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
		cursor.execute("""SELECT * from image""")
		rows = cursor.fetchall()
		current_time = datetime.now()
		for row in rows:
			image_id = row['id']
			approval_date = row['approval_date']
			s3_bucket = row['s3_bucket']
			file_name = row['file_name']
			#If the image is more than 180 days old, delete it...
			if approval_date and (current_time - approval_date).days > 30*6:
				cursor.execute("""delete from image where id={}""".format(image_id)) #... from the database
				s3 = boto3.resource('s3')
				s3.Bucket(s3_bucket).delete_objects(Delete={'Objects':[{'Key':file_name}]}) #... and from s3
			conn.commit()
finally:
	conn.close()