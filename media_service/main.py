from fastapi import FastAPI, UploadFile, File, HTTPException

from media_service.utils import MinioClient

app = FastAPI()

minio_client = MinioClient(
    endpoint_url="http://minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    bucket_name="memes"
)


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        file_url = minio_client.upload_file(file.file, file.filename)
        return {"url": file_url}
    except HTTPException as e:
        return {"error": str(e.detail)}


@app.delete("/delete/{filename}")
async def delete_image(filename: str):
    try:
        minio_client.delete_file(filename)
        return {"detail": "File deleted"}
    except HTTPException as e:
        return {"error": str(e.detail)}
