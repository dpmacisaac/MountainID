# MountainID

Welcome to MountainID. The site running this project can be found at: https://mountainid.macisaac.dev

This project has two important files in the /src directory.

The flickr_download_script.py will download 100 images of each mountain in the MOUNTAINS list. Each time you run it, it will update the page it has for that mountain so you don't download the same image multiple times. The pretrained ImageNet model is incorporated and it filters out any images without mountains. 

The preddict.ipynb is used to process the images into test/train sets. Those are then used in DataGenerators to create train, validate, and test generators. The create_model function then creates a model by adjusting the VGG16 pretrained model. You can then train that model and test it with the previously mentioned DataGenerators.

Details about the site that is deployed is in the /flask_app directory

For any inquiries please message me at dmacisaac@zagmail.gonzaga.edu

Thank you!