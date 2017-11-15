FROM python:3.6.0
MAINTAINER Anh Do <aqd14@msstate.edu>


# Create the working directory (and set it as the working directory)
RUN mkdir -p /app/web
WORKDIR /app/web

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY requirements.txt /app/web
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /app/web

EXPOSE 5000

CMD ["python", "/app/web/app.py"]
