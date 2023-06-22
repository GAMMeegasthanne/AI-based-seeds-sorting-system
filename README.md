# AI-based-seeds-sorting-system
Developed an AI seed sorting system using Keras, TensorFlow,(Deep Learning) Arduino and Python. Detects good/bad seeds and uses servo motor for sorting.


https://github.com/GAMMeegasthanne/AI-based-seeds-sorting-system/assets/80336398/29b769af-f998-46ee-9654-836e0b41ea0f

Project Description:

This project focuses on developing an AI-based seed sorting system specifically tailored for rubber seeds. The system utilizes computer vision, machine learning, and microcontroller programming to automate the sorting process of rubber seeds based on their quality.

Using the Keras library and TensorFlow, a deep learning model is trained on a labeled dataset of rubber seed images. This model is capable of classifying rubber seeds as either good or bad based on their visual characteristics. The Python code captures video frames from a webcam, preprocesses the frames, and feeds them into the trained model for inference.

The Arduino board, equipped with a servo motor and an infrared sensor, is utilized for physically sorting the rubber seeds. The Arduino code reads the state of the infrared sensor to detect the presence of a seed, activating the servo motor to sort the seed based on the classification received from the Python code. Visual feedback in the form of LEDs is provided to indicate whether the seed is classified as good or bad.

The GitHub repository includes the Python code (`seed_sorting.py`), the Arduino code (`seed_sorting.ino`), and the trained model file (`RUBBER_seed_classifier.h5`). Additionally, a detailed README file is provided, offering step-by-step instructions for setting up the system, listing the required dependencies, and providing guidelines for usage.

This project specifically targets rubber seeds, which are widely used in the rubber industry for cultivating rubber trees. The AI-based seed sorting system can significantly improve efficiency and productivity in rubber seed processing by automating the sorting process. By utilizing computer vision and machine learning techniques, this system ensures consistent and reliable classification of rubber seeds, enabling seed producers to maintain high-quality standards.

The combination of computer vision, machine learning, and microcontroller programming showcased in this project serves as an example of how AI technologies can be applied to agricultural processes. The developed system has the potential to enhance the rubber seed industry and inspire similar applications in other seed sorting domains, benefiting farmers, seed producers, and researchers alike.
