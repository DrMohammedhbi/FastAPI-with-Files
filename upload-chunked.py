from fastapi import FastAPI, UploadFile

app = FastAPI()
# Chunked reading for large files
@app.post("/upload-chunked/")
async def upload_chunked(file: UploadFile):
  CHUNK_SIZE = 1024  # 1KB chunks
  contents = []
  while chunk := await file.read(CHUNK_SIZE):
      contents.append(chunk)
  return {"chunks_received": len(contents)}