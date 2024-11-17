import os
from werkzeug.utils import secure_filename

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_file(file, config):
    """Save a file to the specified directory based on the config."""
    if file and allowed_file(file.filename, config["allowed_extensions"]):
        filename = secure_filename(file.filename)
        file_path = os.path.join(config["path"], filename)

        # Check file size
        if len(file.read()) > config["max_size"]:
            raise ValueError("File exceeds maximum allowed size")
        
        # Save the file
        file.seek(0)  # Reset file pointer after size check
        file.save(file_path)
        return file_path
    else:
        raise ValueError("Invalid file format")