import cv2

def infr(prediction):
    counter = 0
    classes=[]
    box=[]
    conf=[]
    for i in prediction:
        class_val = i["class"]
        l=[i["x"],i["y"],i["width"],i["height"]]
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