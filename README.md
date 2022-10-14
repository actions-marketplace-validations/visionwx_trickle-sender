# TricklerSender

## Description
this action is used to create trickle or trickle comment on trickle.
Trickle is a workplace for team to align information. https://www.trickle.so, if you dont have a trickle account, please visit this site for accoutn sign up.


## Usage
- Create a Trickle
```
- name: Send trickle
  uses: visionwx/trickle-sender@v1.0.0
  with:
    trickleToken: xxxx
    workspaceId: xxxx
    memberId: xxxx
    channelId: xxxx
    blockData: '[{"type":"h3","value":"Hello World"},{"type":"text","value":"this is text deajiofjoawejfojoewfjow"}]'
```

- Create a Trickle from local blockdata.json
```
## workflow.yml
# Get block data json
- name: Get block data json
  id: getBlockData
  run: |
    content=`python3 loadJson.py -f blockdata.json`
    echo "::set-output name=blockDataJson::$content"

# Get block data json
- name: Send trickle
  uses: visionwx/trickle-sender@v1.0.0
  with:
    trickleToken: xxxx
    workspaceId: xxxx
    memberId: xxxx
    channelId: xxxx
    blockData: '${{ steps.getBlockData.outputs.blockDataJson }}'

## loadJson.py
import argparse
import json

def parseArgs():
    # 获取脚本参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--jsonFile", required=True, 
        type=str, default=None, help="local json file")
    args = vars(ap.parse_args())
    return args

def main():
    # 获取脚本参数
    args = parseArgs()

    r = json.load(open(args['jsonFile'],'r'))

    print(json.dumps(r))


if __name__ == "__main__":
    main()
```

## Inputs
- trickleToken: the token of your trickle account
- workspaceId: the workspaceId you want to send trickle or comment
- memberId: the memberId on this workspace
- channelId: the channelId you want to send trickle or comment on this workspaceId
- blockData: the trickle content in block format

## Block
- Headline1
```
{
    "type": "h1",
    "value": "This is headline1"
}
```
- Headline2
```
{
    "type": "h2",
    "value": "This is headline2"
}
```
- Headline3
```
{
    "type": "h3",
    "value": "This is headline3"
}
```
- Normal Text
```
{
    "type": "text",
    "value": "This is normal text"
}
```
- Bullet Point
```
{
    "type": "bulletpoint",
    "value": [
        "bullet point 1, jiajifejaowefaq",
        "bullet point 2, jaiejofaejfoawefoawee",
        "bullet point 3, ajiodfjoawjfowjeofjwoefjioewof"
    ]
}
```
- Number Point
```
{
    "type": "numberpoint",
    "value": [
        "number point 1, ajsifjoawiefiowae",
        "number point 2, jiafjoejaowiejfowjieofowefoqw",
        "number point 3, jaisjeofijaowejfiowjeofjwqoeijfoqwejfoqiwejofi"
    ]
}
```
- Check box
```
{
    "type": "checkbox",
    "value": [
        "checkbox 1",
        "checkbox 2",
        "checkbox 3"
    ]
}
```
- Gallery
```
{
    "type": "gallery",
    "value": [
        "https://resource.trickle.so/upload/images/30810c9e-1e0e-4a0b-a927-a81eb083eec1.png",
        "https://resource.trickle.so/upload/images/30810c9e-1e0e-4a0b-a927-a81eb083eec1.png"
    ]
}
```
- Embed
```
{
    "type": "embed",
    "value": "https://devres.trickle.so/miniapps/bubble-gradient.html"
}
```
- Bookmark
```
{
    "type": "bookmark",
    "value": "https://www.trickle.so"
}
```

## Blockdata Example
```
[
  {
    "type": "h3",
    "value": "This is title"
  },
  {
    "type": "text",
    "value": "This is a description"
  },
  {
    "type": "bulletpoint",
    "value": [
      "bullet point 1, jiajifejaowefaq",
      "bullet point 2, jaiejofaejfoawefoawee",
      "bullet point 3, ajiodfjoawjfowjeofjwoefjioewof"
    ]
  },
  {
    "type": "numberpoint",
    "value": [
      "number point 1, ajsifjoawiefiowae",
      "number point 2, jiafjoejaowiejfowjieofowefoqw",
      "number point 3, jaisjeofijaowejfiowjeofjwqoeijfoqwejfoqiwejofi"
    ]
  },
  {
    "type": "checkbox",
    "value": [
      "checkbox 1",
      "checkbox 2",
      "checkbox 3"
    ]
  },
  {
    "type": "gallery",
    "value": [
      "https://resource.trickle.so/upload/images/30810c9e-1e0e-4a0b-a927-a81eb083eec1.png",
      "https://resource.trickle.so/upload/images/30810c9e-1e0e-4a0b-a927-a81eb083eec1.png"
    ]
  },
  {
    "type": "embed",
    "value": "https://devres.trickle.so/miniapps/bubble-gradient.html"
  },
  {
    "type": "embed",
    "value": "https://devres.trickle.so/miniapps/mix-timeline-finance.html"
  },
  {
    "type": "bookmark",
    "value": "https://www.trickle.so"
  }
]
```