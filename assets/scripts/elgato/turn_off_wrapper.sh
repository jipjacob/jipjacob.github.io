#!/bin/bash

# Set the path to your scripts
SCRIPT_DIR="[SET FILE PATH]"
PYTHON_PATH="$SCRIPT_DIR/venv/bin/python" # change to python environment if no virtual env in script directory
LOG_FILE="$SCRIPT_DIR/cron_debug.log"

# Function to log messages
log() {
    echo "$(date): TURN_OFF: $1" >> "$LOG_FILE"
}

# Log start
log "Running turn off wrapper"

# Set up environment variables
# Add typical macOS paths that are available in user sessions but not in cron
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH"

# Make sure Homebrew libs are accessible
if [ -d "/opt/homebrew/lib" ]; then
    export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
fi

# Execute the turn off script
"$PYTHON_PATH" "$SCRIPT_DIR/turn_off_streamdeck.py" >> "$LOG_FILE" 2>&1
STATUS=$?
log "Exit status: $STATUS"

# Done
log "Completed"