from unitls import getEnvPara
from blocks import renderBlock
from trickle import TrickleClient
import json

trickleToken = getEnvPara(parameterName="trickleToken")
workspaceId  = getEnvPara(parameterName="workspaceId")
memberId     = getEnvPara(parameterName="memberId")
channelId    = getEnvPara(parameterName="channelId")
trickleId    = getEnvPara(parameterName="trickleId", raiseExceptionIfNone=False)
blockData     = getEnvPara(parameterName="blockData")

# block data path
blockDataFile = "data/example.json"

# block render
# blocks = renderBlock(json.load(open(blockDataFile)))
blocks = renderBlock(json.loads(blockData))
print(blocks)

tc = TrickleClient(token=trickleToken)
tc.createTrickle(
    workspaceId=workspaceId,
    memberId=memberId,
    channelId=channelId,
    blocks=blocks
)