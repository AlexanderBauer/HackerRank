read n
arr=($(cat))
total=0
for num in "${arr[@]}"; do
    (( total += num ))
done
printf "%.3f\n" $(bc -l <<< "$total/$n")