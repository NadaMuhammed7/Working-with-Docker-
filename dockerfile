#base image
FROM python
COPY . /phase2
WORKDIR /phase2
RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN pip install numpy
CMD python python.py