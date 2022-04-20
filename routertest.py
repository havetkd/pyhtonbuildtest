from fastapi import APIRouter

router = APIRouter(
    tags=["build - test"],

)


@router.get('/testget')
async def testget():
    return "test sererere"

@router.get('/testget2')
async def testget():
    return "2번쨰 빌드 성공"