import json
from ibm_watson import VisualRecognitionV3

#fecha de la version, siempre se sigue ese mismo formato
visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey = 'lsSVfIHXSoEI25f6id3tWvaoRkmeS53-Ia6zHTs_5wYV')

#with --- te crea un contexto(mientras me estes abriendo esta imagen como archivo imagen , hazme este analisis)

with open('./malaika.jpg', 'rb') as image_file:
	faces = visual_recognition.detect_faces(image_file).get_result()
print(json.dumps(faces, indent = 2))

"""
{
  "images": [
    {
      "faces": [
        {
          "age": {
            "min": 20,
            "max": 22,
            "score": 0.9997237
          },
          "face_location": {
            "height": 201,
            "width": 168,
            "left": 249,
            "top": 153
          },
          "gender": {
            "gender": "FEMALE",
            "gender_label": "female",
            "score": 0.9999993. #que tan acertado fue su pronostico
          }
        }
      ],
      "image": "selena.jpg"
    }
  ],
  "images_processed": 1
}

"""