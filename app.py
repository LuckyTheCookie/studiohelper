from flask import Flask, render_template, request, jsonify
import os
from get_infos import get_system_info, get_java_info, get_studio_latest_log, get_studio_local_version, get_studio_latest_version
from downloader import download_and_unzip_github_release
import webbrowser

app = Flask(__name__)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@app.route('/')
def index():
    return render_template("home.html")

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
    print(f"{bcolors.OKCYAN}███████╗████████╗██╗   ██╗██████╗ ██╗ ██████╗     ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ \n\
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔═══██╗    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗\n\
███████╗   ██║   ██║   ██║██║  ██║██║██║   ██║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝\n\
╚════██║   ██║   ██║   ██║██║  ██║██║██║   ██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗\n\
███████║   ██║   ╚██████╔╝██████╔╝██║╚██████╔╝    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║\n\
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝{bcolors.ENDC}")
    
    print(f"{bcolors.OKGREEN}Server started on http://localhost:5241{bcolors.ENDC}")
    webbrowser.open("http://localhost:5241")
    from waitress import serve
    serve(app, host="0.0.0.0", port=5241)    
    
    
