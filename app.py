import os
import http.server
import socketserver
import json

PORT = 7860
DIRECTORY = "dist"

# Generate config.js from environment variables
config = {
    "AI_PROVIDER": os.environ.get("AI_PROVIDER", ""),
    "AI_API_KEY": os.environ.get("AI_API_KEY", ""),
    "AI_BASE_URL": os.environ.get("AI_BASE_URL", ""),
    "AI_MODEL": os.environ.get("AI_MODEL", ""),
    "SUPABASE_URL": os.environ.get("SUPABASE_URL", ""),
    "SUPABASE_ANON_KEY": os.environ.get("SUPABASE_ANON_KEY", "")
}

# Debug: Print environment variable status
print("=" * 60)
print("Environment Variables Check:")
print("=" * 60)
for key, value in config.items():
    if "KEY" in key or "API" in key:
        # Don't print full keys, just show if they're set
        status = "[SET]" if value else "[NOT SET]"
        print(f"{key}: {status}")
    else:
        print(f"{key}: {value if value else '[NOT SET]'}")
print("=" * 60)

# Check if Supabase config is missing
if not config["SUPABASE_URL"] or not config["SUPABASE_ANON_KEY"]:
    print("⚠️  WARNING: SUPABASE_URL or SUPABASE_ANON_KEY is not set!")
    print("Please configure these environment variables in your deployment platform:")
    print("  - SUPABASE_URL (not VITE_SUPABASE_URL)")
    print("  - SUPABASE_ANON_KEY (not VITE_SUPABASE_ANON_KEY)")
    print("=" * 60)

config_js_content = f"window.ENV = {json.dumps(config)};"

# Ensure dist directory exists
if not os.path.exists(DIRECTORY):
    print(f"Error: {DIRECTORY} directory not found.")
    exit(1)

# Write config.js to dist
config_js_path = os.path.join(DIRECTORY, "config.js")
with open(config_js_path, "w") as f:
    f.write(config_js_content)

print(f"✓ Generated config.js at: {config_js_path}")
print(f"✓ Config keys: {list(config.keys())}")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Serve index.html for SPA routing if file not found
        # But allow /config.js and assets to be served correctly
        path = self.translate_path(self.path)
        
        # If it's a file that exists, serve it
        if os.path.exists(path) and not os.path.isdir(path):
            return super().do_GET()
            
        # Otherwise serve index.html
        self.path = '/index.html'
        return super().do_GET()

print(f"Serving at port {PORT}")
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.serve_forever()
