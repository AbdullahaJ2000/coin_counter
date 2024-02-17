# Bounding Box Drawing Tool

This script allows you to count and draw bounding boxes around coins in images, videos, or live camera feeds using a pre-trained model. It supports various input sources and outputs annotated frames with bounding boxes around detected coins.

## Usage

To use the script, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/AbdullahaJ2000/coin_counter.git
    ```

2. Navigate to the directory:

    ```bash
    cd coin_counter
    ```

3. Run the script for image:

    ```bash
    python .\inf1.py --img path/to/input/image --name   path/to/output/image --type i
    ```

4. Run the script for video:

    ```bash
    python .\inf1.py --img path/to/input/video --type v
    ```

5. Run the script for cam:

    ```bash
    python .\inf1.py --type c
    ```

    Replace `path/to/input/image` with the path to the input image or video. By default, the input image is set to "test1.jpeg" and the output image name is set to "predict". The `input_type` can be specified as "i" for image, "v" for video, or "c" for a live camera feed.

# Additional Functions
## infr(prediction)
This function processes the predictions made by the model. It extracts class labels, bounding box coordinates, confidence scores, and calculates the total amount based on the detected objects.

## draw_boxes(image, boxes, confidences, class_labels, tot)
This function draws bounding boxes around detected objects on the input image. It also annotates each bounding box with the class label and confidence score. Additionally, it displays the total amount calculated by the infr() function.

## draw_fps(image, fps)
This function adds a text overlay indicating the frames per second (FPS) on the annotated image.

## Requirements

- Python 3.8>=
- OpenCV
- argparse

Install the dependencies using pip:

```bash
pip install -r requirements.txt 
```
