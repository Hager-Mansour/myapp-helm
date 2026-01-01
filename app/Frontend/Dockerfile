FROM nginx:alpine

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy index.html
COPY index.html .

# Change ownership of necessary directories to the non-root user
# Nginx needs to write to these locations to run properly
RUN chown -R appuser:appgroup /usr/share/nginx/html && \
    chown -R appuser:appgroup /var/cache/nginx && \
    chown -R appuser:appgroup /var/log/nginx && \
    chown -R appuser:appgroup /etc/nginx/conf.d

# Required: Change PID file location to a writable directory
RUN touch /var/run/nginx.pid && \
    chown -R appuser:appgroup /var/run/nginx.pid

# Switch to the non-root user
USER appuser

# Expose port 8080 (Non-root cannot bind to port 80)
EXPOSE 8080

# Override the default Nginx config to listen on 8080 instead of 80
# You can also copy a custom nginx.conf if you prefer
RUN sed -i 's/listen\(.*\)80;/listen 8080;/' /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

