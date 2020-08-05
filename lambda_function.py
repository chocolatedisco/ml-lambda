import os
import numpy as np
from face_classifier import face_detector
import json
import base64
from PIL import Image
from io import BytesIO

# ローカルでのテスト時はTrue
TEST = os.environ['TEST']

def lambda_handler(event, context):
    if TEST:
        # テストのときはローカルの画像で試す
        image_path = os.path.join("", "asuka.jpg")
        event['body-json'] = base64.b64encode(open(image_path, 'rb').read())
    # base64でencodeしたものを受け取る
    rgb_image = Image.open(BytesIO(base64.b64decode(event['body-json'])))
    rgb_image = np.array(rgb_image.convert('RGB'))
    img, err = face_detector(rgb_image)
    if err==0:
        pilImg = Image.fromarray(np.uint8(img))
        buffered = BytesIO()
        pilImg.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        img_str = img_str.decode('utf-8')
        name = face_classifier(img)
        return json.dumps([img_str, name])
    else:
        return json.dumps(err)


#    return json.dumps(annotations, cls = MyEncoder)


# # numpyの型をdumpできるように変換するため
# class MyEncoder(json.JSONEncoder):
#    def default(self, obj):
#        if isinstance(obj, np.integer):
#            return int(obj)
#        elif isinstance(obj, np.floating):
#            return float(obj)
#        elif isinstance(obj, np.ndarray):
#            return obj.tolist()
#        else:
#            return super(MyEncoder, self).default(obj)