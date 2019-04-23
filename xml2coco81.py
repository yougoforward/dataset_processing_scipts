import xml.etree.ElementTree as ET
import os
import json

def load_image_labels(imageset, IMAGE_PATH, LABEL_PATH, class_names=[]):
    # temp=[]
    images=[]
    type="instances"
    annotations=[]
    # categories = [
	# 	{
	# 		"id" : 1,
	# 		"name" : "Pedestrian",
	# 		"supercategory" : "object"
	# 	},
     #    {
     #        "id": 2,
     #        "name": "Cyclist",
     #        "supercategory": "object"
     #    },
     #    {
     #        "id": 3,
     #        "name": "Car",
     #        "supercategory": "object"
     #    },
     #    {
     #        "id": 4,
     #        "name": "Van",
     #        "supercategory": "object"
     #    },
     #    {
     #        "id": 5,
     #        "name": "Truck",
     #        "supercategory": "object"
     #    },
	# ]
    categories= [{"supercategory": "person", "id": 1, "name": "person"},
                   {"supercategory": "vehicle", "id": 2, "name": "bicycle"},
                   {"supercategory": "vehicle", "id": 3, "name": "car"},
                   {"supercategory": "vehicle", "id": 4, "name": "motorcycle"},
                   {"supercategory": "vehicle", "id": 5, "name": "airplane"},
                   {"supercategory": "vehicle", "id": 6, "name": "bus"},
                   {"supercategory": "vehicle", "id": 7, "name": "train"},
                   {"supercategory": "vehicle", "id": 8, "name": "truck"},
                   {"supercategory": "vehicle", "id": 9, "name": "boat"},
                   {"supercategory": "outdoor", "id": 10, "name": "traffic light"},
                   {"supercategory": "outdoor", "id": 11, "name": "fire hydrant"},
                   {"supercategory": "outdoor", "id": 13, "name": "stop sign"},
                   {"supercategory": "outdoor", "id": 14, "name": "parking meter"},
                   {"supercategory": "outdoor", "id": 15, "name": "bench"},
                   {"supercategory": "animal", "id": 16, "name": "bird"},
                   {"supercategory": "animal", "id": 17, "name": "cat"},
                   {"supercategory": "animal", "id": 18, "name": "dog"},
                   {"supercategory": "animal", "id": 19, "name": "horse"},
                   {"supercategory": "animal", "id": 20, "name": "sheep"},
                   {"supercategory": "animal", "id": 21, "name": "cow"},
                   {"supercategory": "animal", "id": 22, "name": "elephant"},
                   {"supercategory": "animal", "id": 23, "name": "bear"},
                   {"supercategory": "animal", "id": 24, "name": "zebra"},
                   {"supercategory": "animal", "id": 25, "name": "giraffe"},
                   {"supercategory": "accessory", "id": 27, "name": "backpack"},
                   {"supercategory": "accessory", "id": 28, "name": "umbrella"},
                   {"supercategory": "accessory", "id": 31, "name": "handbag"},
                   {"supercategory": "accessory", "id": 32, "name": "tie"},
                   {"supercategory": "accessory", "id": 33, "name": "suitcase"},
                   {"supercategory": "sports", "id": 34, "name": "frisbee"},
                   {"supercategory": "sports", "id": 35, "name": "skis"},
                   {"supercategory": "sports", "id": 36, "name": "snowboard"},
                   {"supercategory": "sports", "id": 37, "name": "sports ball"},
                   {"supercategory": "sports", "id": 38, "name": "kite"},
                   {"supercategory": "sports", "id": 39, "name": "baseball bat"},
                   {"supercategory": "sports", "id": 40, "name": "baseball glove"},
                   {"supercategory": "sports", "id": 41, "name": "skateboard"},
                   {"supercategory": "sports", "id": 42, "name": "surfboard"},
                   {"supercategory": "sports", "id": 43, "name": "tennis racket"},
                   {"supercategory": "kitchen", "id": 44, "name": "bottle"},
                   {"supercategory": "kitchen", "id": 46, "name": "wine glass"},
                   {"supercategory": "kitchen", "id": 47, "name": "cup"},
                   {"supercategory": "kitchen", "id": 48, "name": "fork"},
                   {"supercategory": "kitchen", "id": 49, "name": "knife"},
                   {"supercategory": "kitchen", "id": 50, "name": "spoon"},
                   {"supercategory": "kitchen", "id": 51, "name": "bowl"},
                   {"supercategory": "food", "id": 52, "name": "banana"},
                   {"supercategory": "food", "id": 53, "name": "apple"},
                   {"supercategory": "food", "id": 54, "name": "sandwich"},
                   {"supercategory": "food", "id": 55, "name": "orange"},
                   {"supercategory": "food", "id": 56, "name": "broccoli"},
                   {"supercategory": "food", "id": 57, "name": "carrot"},
                   {"supercategory": "food", "id": 58, "name": "hot dog"},
                   {"supercategory": "food", "id": 59, "name": "pizza"},
                   {"supercategory": "food", "id": 60, "name": "donut"},
                   {"supercategory": "food", "id": 61, "name": "cake"},
                   {"supercategory": "furniture", "id": 62, "name": "chair"},
                   {"supercategory": "furniture", "id": 63, "name": "couch"},
                   {"supercategory": "furniture", "id": 64, "name": "potted plant"},
                   {"supercategory": "furniture", "id": 65, "name": "bed"},
                   {"supercategory": "furniture", "id": 67, "name": "dining table"},
                   {"supercategory": "furniture", "id": 70, "name": "toilet"},
                   {"supercategory": "electronic", "id": 72, "name": "tv"},
                   {"supercategory": "electronic", "id": 73, "name": "laptop"},
                   {"supercategory": "electronic", "id": 74, "name": "mouse"},
                   {"supercategory": "electronic", "id": 75, "name": "remote"},
                   {"supercategory": "electronic", "id": 76, "name": "keyboard"},
                   {"supercategory": "electronic", "id": 77, "name": "cell phone"},
                   {"supercategory": "appliance", "id": 78, "name": "microwave"},
                   {"supercategory": "appliance", "id": 79, "name": "oven"},
                   {"supercategory": "appliance", "id": 80, "name": "toaster"},
                   {"supercategory": "appliance", "id": 81, "name": "sink"},
                   {"supercategory": "appliance", "id": 82, "name": "refrigerator"},
                   {"supercategory": "indoor", "id": 84, "name": "book"},
                   {"supercategory": "indoor", "id": 85, "name": "clock"},
                   {"supercategory": "indoor", "id": 86, "name": "vase"},
                   {"supercategory": "indoor", "id": 87, "name": "scissors"},
                   {"supercategory": "indoor", "id": 88, "name": "teddy bear"},
                   {"supercategory": "indoor", "id": 89, "name": "hair drier"},
                   {"supercategory": "indoor", "id": 90, "name": "toothbrush"}]

    anno_id=0
    typeall=[]
    # load ground-truth from xml annotations
    label_files_dir = imageset + LABEL_PATH
    for image_id, label_file_name in enumerate(os.listdir(label_files_dir)):
        label_file=imageset + LABEL_PATH + label_file_name
        # image_file =imageset + IMAGE_PATH + label_file_name.split('.')[0]+'.jpg'
        image_file = ('.').join(label_file_name.split('.')[0:-1]) + '.png'
        tree = ET.parse(label_file)
        root = tree.getroot()
        width = float(1624)
        height = float(1200)
        label = []

        # for child in root:
        #     if child.tag=='size':
        #         width=child.find('width').text
        #         height=child.find('height').text


        images.append({
            "file_name": image_file,
			"height": height,
			"width": width,
			"id": image_id
		})# id of the image. referenced in the annotation "image_id"

        objs = root.find('OBJECTS')
        for obj in objs.iter('OBJECT'):
            if obj.find('TYPE').text=='DontCare':
                continue
            for subobj in obj:
                'Pedestrian', 'Cyclist', 'Car', 'Van', 'Truck'
                if subobj.tag == 'TYPE':
                    cls_name = subobj.text
                    if cls_name=='Pedestrian':
                        cls_name = 'person'
                    if cls_name=='Cyclist':
                        cls_name = 'person'
                    if cls_name=='Car':
                        cls_name = 'car'
                    if cls_name=='Van':
                        cls_name = 'bus'
                    if cls_name=='Truck':
                        cls_name = 'truck'
                    typeall.append(cls_name)
                    cls_id = class_names.index(cls_name)
                elif subobj.tag == 'RECT':
                    xmin = float(subobj.attrib['X'])
                    ymin = float(subobj.attrib['Y'])
                    xlen = float(subobj.attrib['W'])
                    ylen = float(subobj.attrib['H'])
                    xmax = xlen+xmin
                    ymax = ylen+ymin
            annotations.append({"id": anno_id,
                                "image_id" : image_id,
                                "category_id" : cls_id,
                                "segmentation" : [[xmin, ymin, xmin, ymax, xmax, ymax, xmax, ymin],],
                                "area" : xlen*ylen,
                                "bbox" : [xmin, ymin, xlen, ylen],
                                "iscrowd" : 0})
            anno_id=anno_id+1
            # label.append([image_file,image_id, cls_id, xmin, ymin, xlen, ylen])
            print([image_file, image_id, cls_id, xmin, ymin, xlen, ylen])
    settype=set(typeall)
        # temp.append(np.array(label))
    return {"images":images,"type":type,"annotations":annotations,"categories":categories}

ROOT_PATH = '/home/hlzhu/data/qiyan6000/'
IMAGE_PATH ='Images/'
NEW_PATH = 'Annotations/'
# imageset=ROOT_PATH+['train','test']

# classes=['__background__','Pedestrian','Cyclist','Car','Van','Truck']
classes = [
        '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
        'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
        'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
        'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
        'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
        'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
        'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass',
        'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich',
        'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake',
        'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ]

# for dirlist in ['train',]:
#     # decode_xml(subpath, XML_PATH, NEW_PATH)
#     subpath =ROOT_PATH+dirlist
#     label_dict = load_image_labels(subpath,IMAGE_PATH,NEW_PATH,classes)
#     with open(ROOT_PATH+'coco_annotations/'+dirlist+'.json','w') as json_file:
#         json_file.write(json.dumps(label_dict, ensure_ascii=False))
#         json_file.close()

label_dict = load_image_labels(ROOT_PATH,IMAGE_PATH,NEW_PATH,classes)
with open(ROOT_PATH+'coco81_annotations/'+'train'+'.json','w') as json_file:
    json_file.write(json.dumps(label_dict, ensure_ascii=False))
    json_file.close()







