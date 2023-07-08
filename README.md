# Coin-Detection-and-Counting

This Python project detects and counts coins from a video feed using computer vision techniques. It utilizes OpenCV and cvzone libraries to preprocess the images, identify coin contours, and estimate their value based on their size.

## Requirements

To run this project, you need to have the following dependencies installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- cvzone (`pip install cvzone`)

## Usage

1. Make sure your webcam or video input device is connected and functional.

2. Run the `coin_detection.py` script.

3. A window will open displaying the video feed from your camera.

4. Adjust the trackbars in the settings window to fine-tune the threshold values for edge detection. This step may require some experimentation to optimize the results.

5. The program will detect and count the coins in the video feed, displaying the estimated total value on the screen.

6. Press any key to exit the program.

## Contributing

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
