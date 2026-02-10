FROM modelscope-registry.cn-beijing.cr.aliyuncs.com/modelscope-repo/python:3.10

WORKDIR /home/user/app

# Copy built frontend assets
COPY dist/ ./dist/
COPY app.py .

# Copy requirements.txt (though it's empty for this project)
COPY requirements.txt .

# Expose port
EXPOSE 7860

# Start server
ENTRYPOINT ["python", "-u", "app.py"]
