# Use Label Studio's Docker image as base
FROM heartexlabs/label-studio:1.12.0

# Switch to root user for permissions
USER root

# Set /ls-cli as working directory
WORKDIR /ls-cli

# Copy current directory to /ls-cli in Docker image
ADD . /ls-cli

# Install the Python package in current directory
RUN pip install -e .[dev]

# Reset working directory to Label Studio's
WORKDIR $LS_DIR

# Switch back to non-root user
USER 1001

# Uncomment below lines to set entrypoint and command
# ENTRYPOINT ["./deploy/docker-entrypoint.sh"]
# CMD ["label-studio"]