{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1b75ed1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from os import listdir\n",
    "from os.path import isfile, join\n",
    "import os\n",
    "from PIL import Image\n",
    "from tqdm import tqdm\n",
    "\n",
    "IMAGE_PATH = '/path/dissertation/images-630-720' #change /path/ with your actual path\n",
    "files = [f for f in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, f))]\n",
    "\n",
    "base_size = None\n",
    "for file in tqdm(files):\n",
    "  file2 = os.path.join(IMAGE_PATH,file)\n",
    "  img = Image.open(file2)\n",
    "  sz = img.size\n",
    "  if base_size and sz!=base_size:\n",
    "    print(f\"Inconsistant size: {file2}\")\n",
    "  elif img.mode!='RGB':\n",
    "    print(f\"Inconsistant color format: {file2}\")\n",
    "  else:\n",
    "    base_size = sz"
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
