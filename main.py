import cv2
import numpy as np
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

def detect_colour(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error loading image: {image_path}")
        return None
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    color_ranges = {
        'Yellow': {'lower': (20, 150, 150), 'upper': (30, 255, 255)},
        'Pink': {'lower': (330 // 2, 50, 150), 'upper': (350 // 2, 255, 255)},
        'Blue': {'lower': (85, 50, 50), 'upper': (95, 255, 255)},
    }
    
    detected_color = None
    
    for color, range_dict in color_ranges.items():
        lower_bound = np.array(range_dict['lower'], dtype=np.uint8)
        upper_bound = np.array(range_dict['upper'], dtype=np.uint8)
        
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        cv2.imshow(f'{color} mask', mask)

        if cv2.countNonZero(mask) > 0:
            detected_color = color
            break
    
    cv2.destroyAllWindows()
    
    return detected_color

def get_folder_id(drive, color):
    parent_folder_id = 'Your Parent Folder Id'
    
    folder_list = drive.ListFile({'q': f"'{parent_folder_id}' in parents and title = '{color}' and mimeType = 'application/vnd.google-apps.folder'"}).GetList()
    
    if folder_list:
        return folder_list[0]['id']
    else:
        print(f'Folder {color} not found.')
        return None

def upload_to_drive(file_path, folder_id):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size} bytes")
    
    if file_size == 0:
        print(f"File is empty: {file_path}")
        return

    file_drive = drive.CreateFile({'title': os.path.basename(file_path), 'parents': [{'id': folder_id}]})
    
    try:
        file_drive.SetContentFile(file_path)
        file_drive.Upload()
        print(f'Uploaded {file_path} to folder with ID {folder_id}')
    except Exception as e:
        print(f"Error uploading file: {e}")

def main():
    image_path = "Pink.jpg"
    detected_color = detect_colour(image_path)
    print(f'Detected color: {detected_color}')

    if detected_color:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        folder_id = get_folder_id(drive, detected_color)
        if folder_id:
            upload_to_drive(image_path, folder_id)
        else:
            print('No folder found for the detected color.')
    else:
        print('No color detected.')

if __name__ == '__main__':
    main()
