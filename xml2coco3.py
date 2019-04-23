import xml.etree.ElementTree as ET
import os
import json

def load_image_labels(imageset, IMAGE_PATH, LABEL_PATH, class_names=[]):
    # temp=[]
    images=[]
    type="instances"
    annotations=[]
    categories = [
		{
			"id" : 1,
			"name" : "person",
			"supercategory" : "object"
		},
        {
            "id": 2,
            "name": "car",
            "supercategory": "object"
        },
	]
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
                if subobj.tag == 'TYPE':
                    cls_name = subobj.text
                    if cls_name=='Pedestrian':
                        cls_name = 'person'
                    if cls_name=='Cyclist':
                        cls_name = 'person'
                    if cls_name=='Car':
                        cls_name = 'car'
                    if cls_name=='Van':
                        cls_name = 'car'
                    if cls_name=='Truck':
                        cls_name = 'car'
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

classes=['__background__','person','car']
# classes=['background','Pedestrian','Cyclist','Car','Van','Truck']
# for dirlist in ['train',]:
#     # decode_xml(subpath, XML_PATH, NEW_PATH)
#     subpath =ROOT_PATH+dirlist
#     label_dict = load_image_labels(subpath,IMAGE_PATH,NEW_PATH,classes)
#     with open(ROOT_PATH+'coco_annotations/'+dirlist+'.json','w') as json_file:
#         json_file.write(json.dumps(label_dict, ensure_ascii=False))
#         json_file.close()

label_dict = load_image_labels(ROOT_PATH,IMAGE_PATH,NEW_PATH,classes)
with open(ROOT_PATH+'coco3_annotations/'+'train'+'.json','w') as json_file:
    json_file.write(json.dumps(label_dict, ensure_ascii=False))
    json_file.close()





