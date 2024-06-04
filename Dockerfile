# Use Python with Miniconda as the base image
FROM continuumio/miniconda3:latest

# Set environment variables
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install transitive dependencies
RUN apt-get update \
    && apt-get install -y git libspatialindex-dev libgdal-dev libproj-dev gcc

# Clone the repository
RUN git clone https://github.com/rushirajnenuji/viz-3dtiles.git $APP_HOME/viz-3dtiles

# Set the working directory to the repository
WORKDIR $APP_HOME/viz-3dtiles

# Create conda environment with a custom prefix
RUN conda env create -n viz_3d --file environment.yml

# Activate the conda environment
SHELL ["/bin/bash", "-c"]
RUN echo "conda activate viz_3d" >> ~/.bashrc

# Command to run the application
CMD ["python"]
