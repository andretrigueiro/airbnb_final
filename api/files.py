import boto3
import logging
import os
from botocore.exceptions import ClientError
from flask import Blueprint, jsonify, request

UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
BUCKET = os.environ.get('BUCKET')

bp = Blueprint('files', __name__, url_prefix='/files')

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        print("object_name before: ", object_name)
        object_name = os.path.basename(file_name)
        print("object_name after: ", object_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# def download_file(file_name, bucket):
#     """
#     Function to download a given file from an S3 bucket
#     """
#     s3 = boto3.resource('s3')
#     output = f"downloads/{file_name}"
#     s3.Bucket(bucket).download_file(file_name, output)

#     return output

def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        contents.append(item)

    return contents

@bp.route("/storage")
def storage():
    contents = list_files(BUCKET)
    response_object = {'status': 'success'}
    response_object['content'] = contents

    return jsonify(response_object)

@bp.route("/upload", methods=['POST'])
def upload():
    response_object = {'status': 'success'}

    if request.method == "POST":
        # f = request.files['file']
        print("Request: ", request.url)
        # f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        # upload_file(f"uploads/{f.filename}", BUCKET)
        response_object['message'] = 'File added!'

        # filename = "house3.jpg"
        # print("type UP: ", type(UPLOAD_FOLDER))
        # print("type FILE: ", type(filename))
        # abs_pathname = os.path.join(UPLOAD_FOLDER, filename)
        # print("path name", abs_pathname)
        # upload_file(abs_pathname, 'airbnb-clone-project')

    return jsonify(response_object)