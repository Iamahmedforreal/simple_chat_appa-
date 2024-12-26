# Use the official Nginx image as a base
FROM nginx:latest

# Copy files from the public directory to Nginx's default directory
COPY public/ /usr/share/nginx/html

# Expose port 82
EXPOSE 82

# Add a HEALTHCHECK to monitor the Nginx server
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost:82 || exit 1

# Start the Nginx server and serve content on port 82
CMD ["nginx", "-g", "daemon off;"]
