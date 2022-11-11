from ssl import HAS_TLSv1_2
import uuid
import json
import pprint

# uuid
def generateUUID():
    return str(uuid.uuid1())

class Block:
    def render(self):
        raise Exception("NoImplement")

class BlockType:
    normalText = "text"
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    bulletpoint = "bulletpoint"
    numberpoint = "numberpoint"
    checkbox = "checkbox"
    gallery = "gallery"
    embed = "embed"
    embedext = "embedext"
    bookmark = "bookmark"

class BlockTextType:
    normalText = "rich_texts"
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"

class BlockText(Block):

    def __init__(self, value, textType,):
        if type(value) is not str:
            raise Exception("BlockText value type error, must be string")
        self.value = value
        self.textType  = textType

    def render(self):
        return [{
            "id": generateUUID(),
            "type": self.textType,
            "isFirst": False,
            "indent": 0,
            "blocks": [],
            "display": "block",
            "elements": [
                {
                    "id": generateUUID(),
                    "type": "text",
                    "text": self.value,
                    "elements": [],
                    "isCurrent": False
                }
            ],
            "isCurrent": False,
            "constraint": "free"
        }]

class BlockBulletPoint(Block):
    def __init__(self, value):
        if type(value) is not list:
            raise Exception("BlockBulletPoint value type error, must be list<string>")
        self.value = value
    
    def render(self):
        out = []
        for pv in self.value:
            out.append({
                "id": generateUUID(),
                "type": "list",
                "isFirst": False,
                "indent": 0,
                "blocks": [],
                "display": "block",
                "elements": [
                    {
                        "id": generateUUID(),
                        "type": "text",
                        "text": str(pv),
                        "elements": [],
                        "isCurrent": False
                    }
                ],
                "isCurrent": False,
                "constraint": "free"
            })
        return out

class BlockNumberPoint(Block):
    def __init__(self, value):
        if type(value) is not list:
            raise Exception("BlockNumberPoint value type error, must be list<string>")
        self.value = value
    
    def render(self):
        out = []
        curNumber = 0
        for pv in self.value:
            curNumber += 1
            out.append({
                "id": generateUUID(),
                "type": "number_list",
                "isFirst": False,
                "indent": 0,
                "blocks": [],
                "display": "block",
                "elements": [
                    {
                        "id": generateUUID(),
                        "type": "text",
                        "text": str(pv),
                        "elements": [],
                        "isCurrent": False
                    }
                ],
                "isCurrent": False,
                "constraint": "free",
                "userDefinedValue": str(curNumber) + ".",
                "computedValue": str(curNumber) + "."
            })
        return out

class BlockCheckbox(Block):

    def __init__(self, value):
        if type(value) is not list:
            raise Exception("BlockCheckbox value type error, must be list<string>")
        self.value = value

    def render(self):
        out = []
        for pv in self.value:
            out.append({
                "id": generateUUID(),
                "type": "checkbox",
                "isFirst": False,
                "indent": 0,
                "blocks": [],
                "display": "block",
                "elements": [
                    {
                        "id": generateUUID(),
                        "type": "text",
                        "text": str(pv),
                        "elements": [],
                        "isCurrent": False
                    }
                ],
                "isCurrent": False,
                "constraint": "free"
            })
        return out

class BlockGallery(Block):

    def __init__(self, value):
        if type(value) is not list:
            raise Exception("BlockGallery value type error, must be list<string>")
        self.value = value

    def render(self):
        out = []
        for pv in self.value:
            if not (pv.startswith("https") or pv.startswith("http")):
                continue
            out.append({
                "id": generateUUID(),
                "type": "image",
                "text": "",
                "value": pv,
                "elements": [],
                "isCurrent": False
            })
        return [{
            "id": generateUUID(),
            "type": "gallery",
            "isFirst": False,
            "indent": 0,
            "blocks": [],
            "display": "block",
            "elements": out,
            "isCurrent": False,
            "constraint": "free"
        }]

class BlockBookmark(Block):
    def __init__(self, value):
        if not (value.startswith("https") or value.startswith("http")):
            raise Exception("BlockBookmark value must be start with https or http")
        self.value = value
    def render(self):
        return [
            {
                "id": generateUUID(),
                "type": "webBookmark",
                "blocks": [],
                "indent": 0,
                "display": "block",
                "isFirst": False,
                "elements": [],
                "isCurrent": True,
                "constraint": "free",
                "userDefinedValue": self.value,
            }
        ]

class BlockEmbed(Block):
    def __init__(self, value, height=300):
        if not (value.startswith("https") or value.startswith("http")):
            raise Exception("BlockEmbed value must be start with https or http")
        self.value = value
        self.height = height
    def render(self):
        return [
            {
                "id": generateUUID(),
                "type": "embed",
                "blocks": [],
                "indent": 0,
                "display": "block",
                "isFirst": False,
                "elements": [],
                "isCurrent": True,
                "constraint": "free",
                "userDefinedValue": {
                    "height": self.height,
                    "src": "<iframe src=\"" + self.value + "\" class=\"w-full\" allow=\"autoplay\" allowfullscreen></iframe>"
                }
            }
        ]


def parseBlockData(block):
    bType = block.get("type", None)
    bValue = block.get("value", None)
    if bType is None or bValue is None:
        raise Exception("BlockDataFormatError")
    return (
        bType,
        bValue
    )

def renderBlock(blocks):
    out = []
    for perBlock in blocks:
        bType,bValue = parseBlockData(perBlock)
        if bType == BlockType.h1:
            out = out + BlockText(
                value=bValue,
                textType=BlockTextType.h1,
            ).render()
        elif bType == BlockType.h2:
            out = out + BlockText(
                value=bValue,
                textType=BlockTextType.h2,
            ).render()
        elif bType == BlockType.h3:
            out = out + BlockText(
                value=bValue,
                textType=BlockTextType.h3,
            ).render()
        elif bType == BlockType.normalText:
            out = out + BlockText(
                value=bValue,
                textType=BlockTextType.normalText,
            ).render()
        elif bType == BlockType.bulletpoint:
            out = out + BlockBulletPoint(
                value=bValue,
            ).render()
        elif bType == BlockType.numberpoint:
            out = out + BlockNumberPoint(
                value=bValue,
            ).render()
        elif bType == BlockType.checkbox:
            out = out + BlockCheckbox(
                value=bValue,
            ).render()
        elif bType == BlockType.gallery:
            out = out + BlockGallery(
                value=bValue,
            ).render()
        elif bType == BlockType.embed:
            out = out + BlockEmbed(
                value=bValue,
            ).render()
        elif bType == BlockType.embedext:
            if type(bValue) is not dict:
                raise Exception("BlockEmbedExt value must be dict")
            src = bValue.get("src","")
            height = bValue.get("height",300)
            out = out + BlockEmbed(
                value=src,
                height=height
            ).render()
        elif bType == BlockType.bookmark:
            out = out + BlockBookmark(
                value=bValue,
            ).render()
    return out


if __name__ == "__main__":
    # block data path
    blockDataFile = "data/example.json"

    # block render
    blocks = renderBlock(json.load(open(blockDataFile)))
    pprint.pprint(blocks)