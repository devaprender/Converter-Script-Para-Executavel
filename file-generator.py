import os


class FileGenerator:
    def __init__(self):
        pass

    def Start(self):
        self.make_initial_folders()
        self.create_files_per_folders()

    def make_initial_folders(self):
        os.mkdir('Folder 1')
        os.mkdir('Folder 2')
        os.mkdir('Folder 3')
        os.mkdir('Folder 4')

    def create_files_per_folders(self):
        base_directory = os.getcwd()
        os.chdir('Folder 1')
        with open('text_file.txt', 'w') as file:
            file.write('Hello Pythonista')
            pass

        os.chdir(base_directory)
        os.chdir('Folder 2')
        with open('text_file.txt', 'w') as file:
            file.write('Hello Pythonista')
            pass

        os.chdir(base_directory)
        os.chdir('Folder 3')
        with open('text_file.txt', 'w') as file:
            file.write('Hello Pythonista')
            pass

        os.chdir(base_directory)
        os.chdir('Folder 4')
        with open('text_file.txt', 'w') as file:
            file.write('Hello Pythonista')
            pass


generator = FileGenerator()
generator.Start()
