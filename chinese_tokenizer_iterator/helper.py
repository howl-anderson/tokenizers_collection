import os
import subprocess

from chinese_tokenizer_iterator import ltp_data_base_dir
from chinese_tokenizer_iterator.download_then_unzip import download_extract_zip


def post_install_action():
    # download the latest license for nlpir
    subprocess.call("pynlpir update", shell=True)

    if not os.path.exists(ltp_data_base_dir):
        os.mkdir(ltp_data_base_dir)

    if not os.path.isdir(ltp_data_base_dir):
        raise Exception("{} must be a directory".format(ltp_data_base_dir))

    file_name_object_pairs = download_extract_zip(
        'http://ospm9rsnd.bkt.clouddn.com/model/ltp_data_v3.4.0.zip'
    )

    for file_name, file_object in file_name_object_pairs:
        file_path = os.path.join(ltp_data_base_dir, file_name)

        file_dir = os.path.dirname(file_path)

        if not os.path.exists(file_dir):
            os.mkdir(file_dir)

        with open(file_path, 'wb') as fd:
            fd.write(file_object.read())


def get_ltp_data_file():
    for root, dirs, files in os.walk(ltp_data_base_dir, topdown=False):
        if 'cws.model' in files:
            return os.path.join(root, 'cws.model')

    raise Exception("Not found 'cws.model' in {}".format(ltp_data_base_dir))
