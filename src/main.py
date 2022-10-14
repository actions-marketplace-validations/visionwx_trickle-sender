from unitls import getEnvPara
from blocks import renderBlock
from trickle import TrickleClient
import json

TRICKLE_BLOCK = "trickle"
COMMENT_BLOCK = "comment"

try:
    trickleToken = getEnvPara(parameterName="trickleToken")
    workspaceId  = getEnvPara(parameterName="workspaceId")
    memberId     = getEnvPara(parameterName="memberId")
    channelId    = getEnvPara(parameterName="channelId", raiseExceptionIfNone=False)
    trickleId    = getEnvPara(parameterName="trickleId", raiseExceptionIfNone=False)
    blockData     = getEnvPara(parameterName="blockData")
    blockType     = getEnvPara(parameterName="blockType", raiseExceptionIfNone=False, default=TRICKLE_BLOCK)

    # check block type
    if blockType not in [TRICKLE_BLOCK, COMMENT_BLOCK]:
        raise Exception("BlockTypeNotSupport")

    # block data path
    blockDataFile = "data/example.json"

    # block render
    # blocks = renderBlock(json.load(open(blockDataFile)))
    blocks = renderBlock(json.loads(blockData))
    print(blocks)

    tc = TrickleClient(token=trickleToken)

    if blockType == TRICKLE_BLOCK:
        if channelId is None:
            raise Exception("channelId not provide")
        tc.createTrickle(
            workspaceId=workspaceId,
            memberId=memberId,
            channelId=channelId,
            blocks=blocks
        )
    else:
        if trickleId is None:
            raise Exception("trickleId not provide")
        tc.createTrickleComment(
            workspaceId=workspaceId,
            memberId=memberId,
            trickleId=trickleId,
            blocks=blocks
        )

except Exception as e:
    raise SystemExit(str(e))