build:
	pip install -r requirements.txt

run-flickr:
	echo "Running Flickr Download Script"
	python3 src/flickr_download_script.py
	python3 src/flickr_download_script.py
	python3 src/flickr_download_script.py
	python3 src/flickr_download_script.py
	python3 src/flickr_download_script.py
	 
run-preprocess:
	echo "Running Image Preprocessing Script"
	python3 src/preprocess_images.py