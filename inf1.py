from roboflow import Roboflow
import time
import cv2
import argparse

rf = Roboflow(api_key="ASuZDYIQLKcohEdA8UV7")
project = rf.workspace().project("coin_detection-fdkaj")
model = project.version(2).model

def infr(prediction):
    counter = 0
    classes=[]
    box=[]
    conf=[]
    for i in prediction:
        class_val = i["class"]
        l=[]
        x,y,w,h = i["x"],i["y"],i["width"],i["height"]
        l.append(x)
        l.append(y)
        l.append(w)
        l.append(h)
        confid = i["confidence"]
        classes.append(class_val)
        box.append(l)
        conf.append(confid)
        if class_val =="10JD":
            counter+=10
        elif class_val == "5JD":
            counter+=5
        elif class_val == "1JD":
            counter+=1
        elif class_val == "20JD":
            counter+=20
        elif class_val == "50JD":
            counter+=50
        elif class_val == "10coin":
            counter+=0.1
        elif class_val == "25coin":
            counter+=0.25
        elif class_val == "50coin":
            counter+=0.5
        elif class_val == "5coin":
            counter+=0.05
    tot = f"Total = {counter}JD"
    return classes,box,conf,tot

def draw_boxes(image, boxes, confidences, class_labels,tot):
    for box, confidence, class_label in zip(boxes, confidences, class_labels):
        x, y, w, h = box
        start_x = int(x - w / 2)
        start_y = int(y - h / 2)
        end_x = int(x + w / 2)
        end_y = int(y + h / 2)
        color = (0, 255, 0)  
        thickness = 2 
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color, thickness)

        text = f"{class_label}: conf={confidence:.2f}"
        text_top_left = (start_x, start_y+30)
        cv2.putText(image, text, text_top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

        text = tot
        text_TOP_left = (0, 25)
        cv2.putText(image, text, text_TOP_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    return image

def draw_fps(image,fps):
    text = f"fps:{fps:.2f}"
    (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
    text_top_right = (image.shape[0]-200 + text_width, 0 + 30)
    if text_top_right[0] > image.shape[1]:
        text_top_right = (image.shape[1] - text_width - 5, 0 + 30)
    cv2.putText(image, text, text_top_right, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw bounding boxes on an coins.',)
    parser.add_argument('--img', dest='image',type=str, help='Path to the input image',default="test1.jpeg",required=False)
    parser.add_argument('--name', dest='output',type=str, help='Path to the output image',default="predect",required=False)
    parser.add_argument('--type', dest='action',type=str, help='image or video',default="i")

    args = parser.parse_args()
    path = args.image
    output_name = args.output
    types = (args.action).lower()

    if types == "i":
        image = cv2.imread(path)
        predict_result=model.predict(path, confidence=70, overlap=70).json()
        prediction = (predict_result["predictions"])
        classes,box,conf,tot=infr(prediction)
        image_with_boxes = draw_boxes(image.copy(), box, conf, classes,tot)
        cv2.imwrite(output_name+".jpg",image_with_boxes)

    elif types == "v":
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        start_time = time.time()
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            predict_result = model.predict(frame, confidence=80, overlap=50).json()
            prediction = predict_result["predictions"]
            classes, box, conf, tot = infr(prediction)
            annotated_frame = draw_boxes(frame, box, conf, classes, tot)

            
            frame_count += 1
            end_time = time.time()
            elapsed_time = end_time - start_time
            fps = frame_count / elapsed_time
            fps_frame = draw_fps(annotated_frame,fps)
            cv2.imshow("Annotated Frame", fps_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        

    elif types == "c":

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open camera.")
            exit()

        start_time = time.time()
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            predict_result = model.predict(frame, confidence=80, overlap=50).json()
            prediction = predict_result["predictions"]
            classes, box, conf, tot = infr(prediction)
            annotated_frame = draw_boxes(frame, box, conf, classes, tot)

            
            frame_count += 1
            end_time = time.time()
            elapsed_time = end_time - start_time
            fps = frame_count / elapsed_time
            fps_frame = draw_fps(annotated_frame,fps)
            cv2.imshow("Annotated Frame", fps_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
