from ultralytics import YOLO
import os
from IPython.display import display , Image
from IPython import display


# from roboflow import Roboflow
# rf = Roboflow(api_key="0y74HCiM58YAzsLGKzHN")
# project = rf.workspace("devyansh-pdly4").project("formula-detection-ohttb")
# version = project.version(6)
# dataset = version.download("yolov8")

device = 'cuda'
ROOT_DIR='C:\\Users\\bhatt\\Machine Learning\\Internship_Alstom\\Formula-Detection-6'
if __name__ ==  '__main__':
    model = YOLO("yolov8n.yaml")

    result = model.train( data='C:\\Users\\bhatt\\Machine Learning\\Internship_Alstom\\Formula-Detection-6\\data.yaml',
                     optimizer='Adam',lrf=0.01,epochs=75,batch=10,warmup_epochs=3.0,dropout=0.15)

    Image(filename=f"/content/runs/detect/train9/confusion_matrix.png",width = 600)

    Image(filename=f"/content/runs/detect/train9/confusion_matrix_normalized.png",width = 600)

    Image(filename=f'/content/runs/detect/train9/results.png',width = 600)
    model.save("yolov8n.yaml")
    