# Notes Sorter

This project is a Python-based tool that categorizes images of pages with Post-it notes based on the color of the Post-it and sorts them into corresponding folders in Google Drive.

## Features

- Detects the color of Post-it notes (Yellow, Blue, Pink) in images.
- Uploads the images to specific folders in Google Drive based on the detected color.
- Uses Google Drive API for authentication and file management.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`
- PyDrive: `pip install PyDrive`
- Google Drive API credentials

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/meAmitPatil/Notes_Sorter.git
    cd Notes_Sorter
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up Google Drive API credentials:

   - Create a project in the Google Developers Console.
   - Enable the Google Drive API.
   - Download the `client_secrets.json` file and place it in the project directory.

### Usage

1. Place the images you want to sort in the project directory.
2. Run the script:

    ```bash
    python main.py
    ```

3. Authenticate with Google Drive when prompted.
4. The script will detect the color of each image and upload it to the corresponding folder in your Google Drive.

## Folder Structure

- `main.py`: The main script to run the note sorter.
- `client_secrets.json`: Google Drive API credentials.
- `blue.jpg`, `pink.jpg`, `yellow.jpg`: Sample images for testing.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
