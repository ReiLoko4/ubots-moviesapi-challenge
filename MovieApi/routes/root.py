from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def root():
    return {'message': "Theres' no endpoint here, go to /docs to see the available endpoints."}
