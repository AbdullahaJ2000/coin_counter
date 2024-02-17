# Bounding Box Drawing Tool

This script allows you to draw bounding boxes on images, videos, or live camera feeds using a pre-trained model. It supports various input sources and outputs annotated frames with bounding boxes around detected objects.

## Usage

To use the script, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Navigate to the directory:

    ```bash
    cd your_repository
    ```

3. Run the script:

    ```bash
    python script_name.py --img path/to/input/image --name   path/to/output/image --type input_type
    ```

    Replace `path/to/input/image` with the path to the input image or video. By default, the input image is set to "test1.jpeg" and the output image name is set to "predict". The `input_type` can be specified as "i" for image, "v" for video, or "c" for a live camera feed.

#Additional Functions
##infr(prediction)
This function processes the predictions made by the model. It extracts class labels, bounding box coordinates, confidence scores, and calculates the total amount based on the detected objects.

##draw_boxes(image, boxes, confidences, class_labels, tot)
This function draws bounding boxes around detected objects on the input image. It also annotates each bounding box with the class label and confidence score. Additionally, it displays the total amount calculated by the infr() function.

##draw_fps(image, fps)
This function adds a text overlay indicating the frames per second (FPS) on the annotated image.

## Requirements

- Python 3.x
- OpenCV
- argparse

Install the dependencies using pip:

```bash
pip install opencv-python-headless argparse
