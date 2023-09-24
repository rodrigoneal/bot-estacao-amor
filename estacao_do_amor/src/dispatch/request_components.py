from typing import Self
import yaml


class RequestHandler:
    yaml_file: str = "stories.yml"
    yaml_data: dict[str, str] = None

    def __new__(cls, *args, **kwargs) -> Self:
        with open(cls.yaml_file, "r") as file:
            cls.yaml_data = yaml.safe_load(file)
            return super().__new__(cls)

    def __init__(self, func_name: str) -> None:
        self.func_name = func_name

    def can_handle(self):
        func_name = self.func_name.rsplit("_handler", 1)[0]
        for stories in self.yaml_data["stories"]:
            story = stories["story"].rsplit("_story", 1)[0]
            if story == func_name:
                breakpoint()
                return


                
