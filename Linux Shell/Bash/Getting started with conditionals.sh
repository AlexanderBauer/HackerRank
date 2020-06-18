read x
if [ ${x^^} == 'Y' ];
then
    echo "YES"
fi
if [ ${x^^} == 'N' ];
then
    echo "NO"
fi