import kagglehub

# Download latest version
path = kagglehub.dataset_download("utkarsharya/ecommerce-purchases")

print("Path to dataset files:", path)