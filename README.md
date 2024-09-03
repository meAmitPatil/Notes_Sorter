Notes Sorter
Overview
The Notes_Sorter is a Python-based tool designed to automate the sorting of images containing colored Post-it notes into specific folders on Google Drive. It detects the color of the Post-it notes using image processing techniques and uploads the images to the corresponding folder on Google Drive.
Features
Color Detection: Detects Post-it note colors using OpenCV.
Google Drive Integration: Uploads sorted images to specified folders on Google Drive.
Prerequisites
Python 3.x
Libraries: opencv-python, numpy, pydrive
Google Drive API credentials
Installation
Clone the Repository
bash
Copy code
git clone https://github.com/meAmitPatil/Notes_Sorter.git
cd Notes_Sorter


Install Dependencies
Install the required Python libraries:
bash
Copy code
pip install opencv-python numpy pydrive


Setup Google Drive API
Follow Google Drive API quickstart guide to set up your project and obtain client_secrets.json.
Place the client_secrets.json file in the project directory.
Usage
Update Configuration
Replace the parent_folder_id in the script with the ID of your parent folder on Google Drive.
Update folder IDs in the get_folder_id function for Yellow, Pink, and Blue folders.
Run the Script
Run the main script to detect the color of Post-it notes in an image and upload it to the corresponding folder:
bash
Copy code
python main.py


File Paths
Ensure that your image files (blue.jpg, pink.jpg, yellow.jpg) are located in the project directory.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
OpenCV for image processing.
PyDrive for Google Drive integration.

