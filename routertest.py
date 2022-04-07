from fastapi import APIRouter

router = APIRouter(
    tags=["build - test"],

)


@router.get('/testget')
async def testget():
    return "test sererere"