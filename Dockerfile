FROM nvcr.io/nvidia/pytorch:23.11-py3
RUN apt-get update && DEBIAN_FRONTEND=noninteractive  apt-get install -y ffmpeg libsm6 libxext6 libglib2.0-0 git ca-certificates && apt-get clean
RUN pip install --upgrade google-cloud-storage