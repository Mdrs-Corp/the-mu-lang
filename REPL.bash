while true; do
    echo -n "\033[1;33m>>>\033[0m " 
    read -r line 
    echo "$line" > .repl.lastcommand.µ
    ./dicke .repl.lastcommand.µ -µ > .repl.lastoutput
    cat .repl.lastoutput
done
