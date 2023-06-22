# AI-based-seeds-sorting-system
Developed an AI seed sorting system using Keras, TensorFlow,(Deep Learning) Arduino and Python. Detects good/bad seeds and uses servo motor for sorting.


https://github.com/GAMMeegasthanne/AI-based-seeds-sorting-system/assets/80336398/29b769af-f998-46ee-9654-836e0b41ea0f


## Seed Quality Detection System

This project implements a seed quality detection system using computer vision and machine learning techniques. It aims to identify whether a seed is good or bad based on its visual characteristics. The system consists of two main components: a Python script for image capture and classification, and an Arduino sketch for controlling the motor and LEDs.

### Prerequisites

To run the Python script, you need to have the following dependencies installed:

- OpenCV (cv2)
- NumPy
- TensorFlow
- Serial (pyserial)

To run the Arduino sketch, you need the Arduino IDE and the Servo library.

### Getting Started

1. Clone this repository to your local machine.
2. Connect the camera to your computer and upload the Arduino sketch to the Arduino board.
3. Install the required Python dependencies using pip: `pip install opencv-python numpy tensorflow pyserial`.
4. Make sure the camera is properly configured and recognized by the system.
5. Run the Python script `seed_quality_detection.py` to start the seed quality detection system.

### Usage

1. The script will capture frames from the camera and display them in a window.
2. Press the 'q' key to quit the program.
3. The Arduino board controls the motor and LEDs based on the seed capture status.
4. If a good seed is detected, the green LED will light up and the motor will be turned off.
5. If a bad seed is detected, the red LED will light up and the motor will be turned on.

### Adjustments

You can adjust the following parameters to customize the system:

- Camera settings: resolution, frame rate, etc.
- Model threshold: change the threshold value to adjust the classification sensitivity.
- Motor and LED pin assignments: modify the pin numbers according to your setup.

### Contributing

Contributions to this project are welcome. If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to the terms of the license.

### Acknowledgments

This project was developed as part of [your name]'s [thesis/project] at [your institution]. Special thanks to [supervisor/mentor] for their guidance and support.

### Contact

For any questions or inquiries, please contact [unitysldeveloper@gmail.com].

Enjoy using the seed quality detection system!


Project Description:

This project focuses on developing an AI-based seed sorting system specifically tailored for rubber seeds. The system utilizes computer vision, machine learning, and microcontroller programming to automate the sorting process of rubber seeds based on their quality.

Using the Keras library and TensorFlow, a deep learning model is trained on a labeled dataset of rubber seed images. This model is capable of classifying rubber seeds as either good or bad based on their visual characteristics. The Python code captures video frames from a webcam, preprocesses the frames, and feeds them into the trained model for inference.

The Arduino board, equipped with a servo motor and an infrared sensor, is utilized for physically sorting the rubber seeds. The Arduino code reads the state of the infrared sensor to detect the presence of a seed, activating the servo motor to sort the seed based on the classification received from the Python code. Visual feedback in the form of LEDs is provided to indicate whether the seed is classified as good or bad.

The GitHub repository includes the Python code (`seed_sorting.py`), the Arduino code (`seed_sorting.ino`), and the trained model file (`RUBBER_seed_classifier.h5`). Additionally, a detailed README file is provided, offering step-by-step instructions for setting up the system, listing the required dependencies, and providing guidelines for usage.

This project specifically targets rubber seeds, which are widely used in the rubber industry for cultivating rubber trees. The AI-based seed sorting system can significantly improve efficiency and productivity in rubber seed processing by automating the sorting process. By utilizing computer vision and machine learning techniques, this system ensures consistent and reliable classification of rubber seeds, enabling seed producers to maintain high-quality standards.

The combination of computer vision, machine learning, and microcontroller programming showcased in this project serves as an example of how AI technologies can be applied to agricultural processes. The developed system has the potential to enhance the rubber seed industry and inspire similar applications in other seed sorting domains, benefiting farmers, seed producers, and researchers alike.
