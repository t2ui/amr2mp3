from flask import Flask, request, send_file, jsonify
import os
import subprocess
import uuid

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    
    input_filename = f"{uuid.uuid4()}.amr"
    output_filename = f"{uuid.uuid4()}.mp3"
    input_filepath = os.path.join('/tmp', input_filename)
    output_filepath = os.path.join('/tmp', output_filename)
    
    file.save(input_filepath)
    
    try:
        subprocess.check_call(['ffmpeg', '-i', input_filepath, output_filepath])
        return send_file(output_filepath, as_attachment=True, download_name=output_filename)
    except subprocess.CalledProcessError as e:
        return jsonify(error="Conversion failed"), 500
    finally:
        os.remove(input_filepath)
        if os.path.exists(output_filepath):
            os.remove(output_filepath)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
