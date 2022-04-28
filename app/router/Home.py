from fastapi import APIRouter

router=APIRouter()

@router.get('/' , tags=['Home'])
async def Home():
    return {
        'all things is good2'
    }