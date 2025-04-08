import subprocess

class LinuxService:
    """Сервис для команд Linux"""
    
    @staticmethod
    def create_and_merge_file():
        """Команды Linux для Задачи 1-2"""
        try:
            # Создать файлы
            with open("ThePet", "w") as f:
                f.write("Dogs\nCats\nRoosters")
            
            with open("PackAnimal", "w") as f:
                f.write("Horses\nCamels\nDonkeys")
            
            # Əmrləri icra et
            subprocess.run("cat ThePet PackAnimal > UnitedFile", shell=True, check=True)
            subprocess.run("mv UnitedFile HumanFriends", shell=True, check=True)
            subprocess.run("mkdir AnimalShelter", shell=True, check=True)
            subprocess.run("mv HumanFriends AnimalShelter/", shell=True, check=True)
            
            return True
        except subprocess.CalledProcessError as e:
            print(f"Ошибка команды Linux: {e}")
            return False