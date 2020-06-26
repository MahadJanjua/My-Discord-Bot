import discord
import numpy as np
from discord.ext import commands
import requests
import shutil
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import vgg16

class ImageClassify(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.model = None
    
    @commands.command(name='predict', pass_context=True)
    async def predict(self, ctx, url: str):
        """Takes in a url and downloads"""
        response = requests.get(url, stream=True)
        local_file = open('image_to_classify.jpg', 'wb')
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, local_file)
        local_file.close()
        del response

        self.model = vgg16.VGG16(weights='imagenet')

        original = load_img('image_to_classify.jpg', target_size = (224, 224))
        numpy_image = img_to_array(original)
        image_batch = np.expand_dims(numpy_image, axis=0)
        processed_image = vgg16.preprocess_input(image_batch)

        predictions = self.model.predict(processed_image)

        label_vgg = decode_predictions(predictions)

        await ctx.send(str(label_vgg[0][0][2]) + "% chance of the image being part of the " + str(label_vgg[0][0][1]) + " category.")


def setup(client):
    client.add_cog(ImageClassify(client))