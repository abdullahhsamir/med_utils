class Organizer:

    def __init__(self, project_name, images_source_dir, labels_source_dir, destination_base_dir):
        self.project_name = project_name
        self.images_source_dir = images_source_dir
        self.labels_source_dir = labels_source_dir
        self.destination_base_dir = destination_base_dir

    def make_dirs(self):
        import os

        project_dir = os.path.join(self.destination_base_dir, self.project_name)
        os.makedirs(project_dir, exist_ok=True)

        images_destination_dir = os.path.join(project_dir, 'images')
        labels_destination_dir = os.path.join(project_dir, 'labels')
        os.makedirs(images_destination_dir, exist_ok=True)
        os.makedirs(labels_destination_dir, exist_ok=True)

        return images_destination_dir, labels_destination_dir

    def copy_images(self):
        import os
        import shutil
        from tqdm import tqdm

        images_destination_dir, _ = self.make_dirs()

        files = os.listdir(self.labels_source_dir)
        image_names = [os.path.splitext(f)[0] for f in files]

        for image_name in tqdm(image_names):
            source_file = os.path.join(self.images_source_dir, image_name + '.jpg')
            destination_file = os.path.join(images_destination_dir, image_name + '.jpg')

            shutil.copy(source_file, destination_file)

    def copy_labels(self):
        import os
        import shutil
        from tqdm import tqdm

        _, labels_destination_dir = self.make_dirs()

        label_names = os.listdir(self.labels_source_dir)

        for label_name in tqdm(label_names):
            source_file = os.path.join(self.labels_source_dir, label_name)
            destination_file = os.path.join(labels_destination_dir, label_name)

            shutil.copy(source_file, destination_file)
