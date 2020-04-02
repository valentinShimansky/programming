a=$(grep -E 'chr..\s[0-9]+\s\.\s.\s.\s' $1 | awk '{print $1}' | uniq)
echo $a
for i in ${a[@]}:
do
grep -E "$i\s[0-9]+\s\.\s.\s.\s" $1 | awk '{print $1, $4, $5}' | uniq -c | awk 'BEGIN {OFS="\t"} {print $2, $1, $3, $4}' | sort
done