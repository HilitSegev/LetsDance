from flask import Flask, request, jsonify, send_from_directory
from cloud_storage import cloud_manager
from main_processor import process_video
from consts import *
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)


# TODO: load models here so process will be fast

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['video']
        cloud_path = cloud_manager.save_uploaded_file(file)
        response = jsonify({
            'url': cloud_path
        })
    except Exception as e:
        response = jsonify({'error': str(e)})
    return response


@app.route('/process', methods=['POST'])
def process():
    try:
        video_path = request.form['url'] if 'url' in request.form else None
        bg_img_path = RESOURCES_DIR + BACKGROUND_IMAGES_DIR + request.form[
            'background'] if 'background' in request.form else None
        emoji_face = request.form['emoji'] if 'emoji' in request.form else None
        color_pallette = request.form['color_pallette'] if 'color_pallette' in request.form else DEFAULT_COLOR
        print(request.form)
        final_video_path = process_video(video_path, bg_img_path, emoji_face, color_pallette)
        file_name = final_video_path.split("/")[-1]
        response = send_from_directory(OUTPUTS_DIR, file_name)
    except Exception as e:
        response = jsonify({'error': str(e)})
    return response


@app.route('/upload_and_process', methods=['POST'])
def upload_and_process():
    try:
        file = request.files['video']
        video_name = request.form['url'] if 'url' in request.form else None
        video_path = cloud_manager.save_uploaded_file(file, video_name)
        bg_img_path = RESOURCES_DIR + BACKGROUND_IMAGES_DIR + request.form[
            'background'] if 'background' in request.form else None
        emoji_face = request.form['emoji'] if 'emoji' in request.form else None
        color_pallette = request.form['color_pallette'] if 'color_pallette' in request.form else DEFAULT_COLOR
        print(request.form)
        final_video_path = process_video(video_path, bg_img_path, emoji_face, color_pallette)
        file_name = final_video_path.split("/")[-1]
        response = send_from_directory(OUTPUTS_DIR, file_name)
    except Exception as e:
        response = jsonify({'error': str(e)})
    return response


@app.route('/get_video', methods=['GET'])
def get_video():
    try:
        video_name = request.args['url'] if 'url' in request.args else None
        response = send_from_directory(OUTPUTS_DIR, video_name)
    except Exception as e:
        response = jsonify({'error': str(e)})
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
