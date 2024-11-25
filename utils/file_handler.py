import os
from werkzeug.utils import secure_filename

def save_uploaded_file(file, upload_folder):
    """
    Saves an uploaded file to the specified folder.

    Args:
        file (werkzeug.datastructures.FileStorage): The uploaded file object.
        upload_folder (str): Path to the folder where the file should be saved.

    Returns:
        str: The file path of the saved file.
    """
    try:
        # Ensure the upload folder exists
        os.makedirs(upload_folder, exist_ok=True)

        # Secure the filename
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)

        # Save the file
        file.save(file_path)

        return file_path
    except Exception as e:
        raise RuntimeError(f"Error saving uploaded file: {e}")


def download_file(file_path):
    """
    Prepares a file for download.

    Args:
        file_path (str): Path to the file to be downloaded.

    Returns:
        tuple: A tuple containing the file path and the file's basename.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return file_path, os.path.basename(file_path)


def delete_file(file_path):
    """
    Deletes a file from the file system.

    Args:
        file_path (str): Path to the file to be deleted.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        raise RuntimeError(f"Error deleting file: {e}")
