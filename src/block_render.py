import json
import os
from os.path import join, exists, getmtime
from jinja2 import Environment, FunctionLoader, BaseLoader, TemplateNotFound
import uuid

## custom filter: uuid
def to_uuid(value):
    if value == "random":
        return uuid.uuid1()
    return uuid.uuid1()

class LocalLoader(BaseLoader):
    def __init__(self,path):
        self.path = path
    def get_source(self, environment, template):
        path = join(self.path, template)
        if not exists(path):
            raise TemplateNotFound(template)
        mtime = getmtime(path)
        with open(path) as f:
            source = f.read()
        return source, path, lambda: mtime == getmtime(path)

class BlockRender:
    def __init__(self, loader):
        self.env = Environment(loader=loader)
        self.env.filters['jsonify'] = json.dumps
        self.env.filters["uuid"] = to_uuid
    def render(self, templatePath, objectdatas):
        blocks = []
        return blocks

class Jinja2BlockRender(BlockRender):
    def render(self, templatePath, objectdatas:dict):
        template = self.env.get_template(templatePath)
        blocks = template.render(**objectdatas)
        return json.loads(blocks)

if __name__ == "__main__":
    # app webhook templateUri
    templatePath = "base.json"

    # webhook event data from 3rd party
    templateDataPath = "data/base.json"
    templateData = json.load(open(templateDataPath, "r"))

    # init renderObj and perform render
    blockRender = Jinja2BlockRender(loader=LocalLoader(path="./templates"))
    blocks = blockRender.render(templatePath, templateData)
    print(blocks)