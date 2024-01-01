class ModelWrapper:

    def __init__(self, model_path):
        from ultralytics import YOLO

        self.model_path = model_path
        self.model = YOLO(self.model_path)

    def visualize_img_conf(self, img_path, conf=0.25):
        import matplotlib.pyplot as plt

        results = self.model(img_path, conf=conf)
        plt.figure(figsize=(10, 30))
        plt.imshow(results[0].plot())
        plt.show()

    def visualize_on_dir(self, path, start = 0, end = 1, conf = 0.25):
        import os

        listdir = os.listdir(path)[start:end]
        for i, img in enumerate(listdir):
          f_path = path+'/'+img
          self.visualize_img_conf(f_path, conf)

    def visualize_random_samples(self, path, conf = 0.25,   num_samples=5):
      import random
      import os

      image_files = [f for f in os.listdir(path) if f.endswith('.jpg')]
      random_samples = random.sample(image_files, min(num_samples, len(image_files)))

      for i, sample_file in enumerate(random_samples, 1):
          image_path = os.path.join(path, sample_file)
          self.visualize_img_conf(image_path, conf = conf)
