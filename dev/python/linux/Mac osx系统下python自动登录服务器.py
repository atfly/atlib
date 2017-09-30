
mport os
s = """osascript <<EOD
tell application "iterm"
    activate
    set myterm to (make new terminal)
    tell myterm
        launch session "Default Session"
        tell the last session
            write text "ssh user@ip"
            delay 3
            write text "password"
         end tell
    end tell
end tell
EOD"""
os.system(s)