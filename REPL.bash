
while true; do

    if ! command -v ./dicke &> /dev/null
    then
        echo "Error: dicke is not installed. Please install dicke before running the REPL."
        break
    fi

    echo -n "\033[1;33m>>>\033[0m" 
    if ! read -r line; then
        break # stop the loop when CTRL+D is pressed
    fi
    echo "$line" > .repl.lastcommand.µ
    ./dicke .repl.lastcommand.µ -µ > .repl.lastoutput
    cat .repl.lastoutput
done

