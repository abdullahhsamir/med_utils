class Mpreprocessor:

    """A class for preprocessing PDFs and performing various operations on images."""


    def __init__(self, pdf_directory: str, image_directory: str):
          if not all( isinstance(path, str) for path in [pdf_directory, image_directory]):
            raise TypeError("pdf_directory and image_directory must be strings")

          self.pdf_directory = pdf_directory
          self.image_directory = image_directory


    def convert_pdfs_to_images(self):

          """Convert PDFs to images and save them in the specified image directory."""

          from pdf2image import convert_from_path
          import os
          from tqdm import tqdm


          os.makedirs(self.image_directory, exist_ok=True)
          for filename in tqdm(os.listdir(self.pdf_directory)):
              if filename.endswith('.pdf'):
                  pdf_path = os.path.join(self.pdf_directory, filename)
                  images = convert_from_path(pdf_path)

                  for i, image in enumerate(images):
                      image_path = os.path.join(self.image_directory, f'{filename}_{i+1}.jpg')
                      image.save(image_path, 'JPEG')

          print(f'-Converted Pdfs to Images Successfully, Total generated Images: {len(os.listdir(self.image_directory))} ')


    def rename_images(self):
          import os

          directory = self.image_directory
          files = os.listdir(directory)

          for i, file in enumerate(files):

            new_name = f'image_{i}.jpg'
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)

            os.rename(old_path, new_path)

          print('-Renamed Images Successfully')


    def apply_cleanvision(self):
          from cleanvision import Imagelab

          imagelab = Imagelab(data_path=self.image_directory)
          print(imagelab.find_issues())
          return imagelab


    def visualize_random_samples(self, num_samples=5, figsize = (15, 5)):
          import os
          import random
          import matplotlib.pyplot as plt
          from matplotlib.image import imread

          image_files = [f for f in os.listdir(self.image_directory) if f.endswith('.jpg')]
          random_samples = random.sample(image_files, min(num_samples, len(image_files)))

          plt.figure(figsize=figsize)
          for i, sample_file in enumerate(random_samples, 1):
              image_path = os.path.join(self.image_directory, sample_file)
              img = imread(image_path)

              plt.subplot(1, num_samples, i)
              plt.imshow(img)
              plt.title(f'Sample {i}')
              plt.axis('off')

          plt.show()