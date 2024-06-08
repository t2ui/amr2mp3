# AMR to MP3 Conversion API

This is a simple Flask API to convert AMR files to MP3 using FFmpeg.

## Build and Run with Docker

1. Build the Docker image:
   ```sh
   docker build -t amr-to-mp3 .
   ```

2. Run the Docker container:
   ```sh
   docker run -d -p 5000:5000 amr-to-mp3
   ```

3. The API will be available at `http://localhost:5000/convert`.

## API Endpoint

### `POST /convert`

#### Request
- Form-data with a file field named `file`.

#### Response
- On success: the converted MP3 file.
- On failure: JSON with an error message.
