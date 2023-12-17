{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03862ce2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from PIL import Image\n",
    "import numpy as np\n",
    "\n",
    "def normalize_image(image_path, output_path):\n",
    "    \"\"\"\n",
    "    Normalize the pixel values of an image to the range [0, 1] and save it to output_path.\n",
    "    \"\"\"\n",
    "    with Image.open(image_path) as img:\n",
    "        img_array = np.array(img).astype(np.float32) / 255.0\n",
    "        normalized_img = Image.fromarray(np.uint8(img_array * 255))\n",
    "        normalized_img.save(output_path)\n",
    "\n",
    "def normalize_all_images(input_directory, output_directory):\n",
    "    \"\"\"\n",
    "    Normalize all images in the input_directory and save them to output_directory.\n",
    "    \"\"\"\n",
    "    if not os.path.exists(output_directory):\n",
    "        os.makedirs(output_directory)\n",
    "\n",
    "    for filename in os.listdir(input_directory):\n",
    "        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):\n",
    "            input_path = os.path.join(input_directory, filename)\n",
    "            output_path = os.path.join(output_directory, filename)\n",
    "            normalize_image(input_path, output_path)\n",
    "\n",
    "# Replace these paths with your actual directories\n",
    "input_directory = '/path/to/your/input/images'\n",
    "output_directory = '/path/to/your/output/images'\n",
    "\n",
    "normalize_all_images(input_directory, output_directory)\n",
    "print(\"All images have been normalized and saved to the output directory.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
