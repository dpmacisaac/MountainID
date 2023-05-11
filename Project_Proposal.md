## Mountain Identification Project Proposal

3. Project Proposal
The project proposal is a well-written, well-organized, and grammatically-correct narrative (e.g. not a bulleted list) describing:

### Questions: 
- What is the main motivation and purpose of the project… essentially, “so what?”
- Who are stakeholders (users/groups that are impacted by the outcome of the project) interested in this project?
- How does it meet the project requirements (e.g. original, substantial, etc., see above)
- What is the tech stack and how much of it are you familiar with
- What are the data source(s), how are they timely, and how are you going to ingest them
- What are your major analyses and anticipated findings/results
- What does deployment look like for your project (e.g. how will people “use” it?)
- What cloud platforms/tools will you be using and how much will the app/system cost
- Note that cloud resources can get expensive and it is NOT expected that you pay for any services to deploy your project. Since we are in the non-commercial/academic sector, we can often apply for free academic credits for major cloud providers like GCP, AWS (update: perhaps not AWS), etc; however, this is the most variable part of each project and I anticipate flexibility and what “deployment” looks like for each part.
- You will need to provide a budget for the various parts and on an appropriate scale (e.g. per hour, per day, etc.)
- What are the risks of the project and what are your mitigation plans

### Motivations:

Having gone adventuring throughout the mountains in Washington, Idaho, and California many times, one problem I've experienced is that it can be difficult to identify mountains. For this reason, I thought that a mountain identification system could be a very useful program. Though this program won't be as real life applicable due to scope limiations, I find this project would be a good start to developing this system and testing the limiations of computer vision and machine learning,

Additionally, I find computer vision and machine learning to be exetermely interesting topics that I haven't had much of a chance to utilize yet. This project felt like a good place to experiement because it combines those three interests: mountains, computer vision, and machine learning!

### Stakeholders:

The stakeholders of this project are myself and hikers. I have a stake in this project because it will teach me skills that I would love to learn. Hikers would also be interested in this project because it has the potential to help them identify mountains by simply snapping a pic. This could prove benefitial for both understanding where they might be aswell as help to ensure that they are looking at what they think they are looking at. 

### Project Requirements:

Data Focused: This project will need to obtain and utilize thousands of labeled mountain images to train a CNN Model. This data is the only way this project is possible and a big focus of the project will be mining and preprocessing the images. 

Substantial: This project will involve multiple different technologies that are new to me. I believe that getting the model to be accurate will take a lot of time and effort to refine it. I also believe, due to my limited experience, that creating a hosted site will take me a while. 

Timely: All the data I will be using is live data off of Flickr. I will be utilizing their API to download photos in batch. If time allows, I may try to setup an actual schedule to download new images off Flickr and train the model more with that new data.

Deployment: My end product will be a live site that will allow the user to upload an image and it will output a prediction of which mountain it is. 

### Tech Stack

Flickr API: I will be using the Flickr API to mine labeled images. Having researched it now, I feel familiar with it and am confident it provides the solution I am looking for.

OpenCV: I will be using the OpenCV library to do image preprocessing to normalize the image data for machine learning. Having researched this, I feel familiar enough with it that I do not think it will pose a challenge. 

Pretrained Convolutional Neural Network: I will be using a pretrained CNN model as a starting point for my machine learning model. I am looking at testing with VGG-16, ResNet-50, Inception-v3, and EfficientNet. These are all very strong pretrained models and I am hoping to discover which one will work best for my project. I am familiar with creating neural network models in PyTorch but I have never used a pretrained model so this will be where I spend a good amount of time. I believe that tuning the model to increase accuracy will take a good portion of my time.  

Flask: I think I will be using flask to create my web app. I haven't done extensive research into exactly how to create the site yet but since the app will be fairly simple I am not worried. 

GCP: I will be hosting my model and the site on GCP. Having watched tutorials (along with following along with the ones demonstrated in class) to connect GCP with flask apps with a NN model I think this will difficult but doable. This may be difficult since both these technologies are very new to me so I think there will be a bit of a learning curve but from my research of these over this period I am confident I can overcome these. 

### Anticipated Findings:

I anticipate that I will be able to achieve a 50%+ accuracy but I think it will be difficult achieve 70%+ accuracy. 

I believe that contours, edges, as well as the colors histograms will be the most significant features used to differentiate the mountains. The ridges and edges of the mountains define their shape and will be the main way that I want my program to differentiate between the mountains. But since I am choosing a number of mountains that are far away from eachother, I believe that the scenery (the colors of the trees, rocks, etc) in the surrounding area of the photo might help to more easily identify each mountain aswell. 

### Deployment:

As described earlier, I will be hosting a site where the user can upload a picture and the program will then predict which mountain it is an display it. It may also say the confidence that it has with that prediction. Additionally, there will be a page which outputs information such as the accuracy of the model. 

### Cloud Platforms:

I will be using GCP to host the site. I intend on training the model on my own computer. For this reason I am not worried about the cost of the project. Though, if I discover that my computer processing power does not cut it, I may have to shift plans and try and use GCP to train the model. This would add the risk of a cost being incurred. I am unsure about how much this would cost so I am going to avoid it as much as I can. 

### Risks:
Low accuracy. The accuracy might be low for a few reasons:
    (1) The data might be difficult to process. From my exploration of images on Flickr given a search term, there are sometimes many images that are not the actual mountain but rather other things such as people by a sign or a road or area near the mountain. This data needs to be processed out as it is mislabeled and isn't the actual mountain. 
    (2) The mountain features might be so similar that unless I had 10's of thousands of images the differences won't be noticeable by the model. This is why I may have to spend lots of time fine tuning the model. 

Offloading the training to GCP. If the training of the model is more computationally intense than I initially plan, I will have to offload the training to GCP. This has the added risks of time spent learning this aswell as the risk of incurring charges. If I have to do this I will be careful to set budgets so I don't go over the educational credits I have. I will also use the Privacy app if I have to use a credit card because this creates a new card to be used with spending limits. This way I don't risk spending an insane amount of money. 