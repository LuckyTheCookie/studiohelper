from flask import Flask, render_template, request, jsonify
import os
from get_infos import get_system_info, get_java_info, get_studio_latest_log, get_studio_local_version, get_studio_latest_version
from downloader import download_and_unzip_github_release

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_info_file', methods=['POST'])
def create_info_file_route():
    try:
        create_info_file()
        return jsonify({'status': 'success', 'message': 'File created successfully.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/update_studio', methods=['POST'])
def update_studio_route():
    try:
        download_and_unzip_github_release()
        return jsonify({'status': 'success', 'message': 'STUdio updated successfully.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/get_java_info', methods=['POST'])
def get_java_info_route():
    try:
        java_info = get_java_info()
        return jsonify({'status': 'success', 'message': java_info})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

def create_info_file():
    with open("full-log.txt", "w") as file:
        file.write(get_system_info())
        file.write("==============================\n")
        file.write(get_java_info())
        file.write("==============================\n")
        file.write(get_studio_local_version())
        file.write("==============================\n")
        file.write(get_studio_latest_log())

if __name__ == "__main__":
    app.run(debug=True)
