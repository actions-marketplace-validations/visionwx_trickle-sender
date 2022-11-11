from unitls import getEnvPara
from blocks import renderBlock
from trickle import TrickleClient
import json

# block data path
blockDataFile = "data/block_data_02.json"

# block render
blocks = renderBlock(json.load(open(blockDataFile)))
print(blocks)

tc = TrickleClient(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzMDc2NjA2ODIzMDI1ODY4OSIsImlhdCI6MTY2NTY1NDM2NiwiZXhwIjoxNjk3MTkwMzY2LCJzY29wZSI6ImJyb3dzZXIifQ.8-XY_hmDpXIk60py2_uDkcbScUGPxJvLkfHQUyfZx4g")

tc.createTrickle(
    workspaceId="364397913113100291",
    memberId="364404407103651845",
    channelId="364397913113165830",
    blocks=blocks
)