import os
import fitz  # PyMuPDF
from google.cloud import storage

SOURCE_BUCKET = os.environ.get("SOURCE_BUCKET")
DEST_BUCKET = os.environ.get("DEST_BUCKET")
TASK_INDEX = os.environ.get("CLOUD_RUN_TASK_INDEX", "0")

def extract_pdf_text_to_gcs(pdf_blob_name):
    client = storage.Client()
    source_bucket = client.bucket(SOURCE_BUCKET)
    dest_bucket = client.bucket(DEST_BUCKET)

    # Download PDF to tmp
    local_pdf = f"/tmp/{pdf_blob_name}"
    blob = source_bucket.blob(pdf_blob_name)
    blob.download_to_filename(local_pdf)
    print(f"Downloaded {pdf_blob_name}")

    # Extract text
    doc = fitz.open(local_pdf)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Upload extracted text
    txt_blob_name = pdf_blob_name.replace(".pdf", ".txt")
    dest_blob = dest_bucket.blob(txt_blob_name)
    dest_blob.upload_from_string(text)
    print(f"Extracted and uploaded text for {pdf_blob_name} as {txt_blob_name}")

def main():
    client = storage.Client()
    blobs = list(client.bucket(SOURCE_BUCKET).list_blobs())

    pdf_blobs = [blob.name for blob in blobs if blob.name.endswith(".pdf")]

    task_index = int(TASK_INDEX)
    if task_index < len(pdf_blobs):
        extract_pdf_text_to_gcs(pdf_blobs[task_index])
    else:
        print(f"No PDF to process for task index {task_index}")

if __name__ == "__main__":
    main()
