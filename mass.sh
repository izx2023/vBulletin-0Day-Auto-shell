#
# Twitter.com/0x00fy
# 

clear
echo "

---------------------

Twitter.com/0x00fy

---------------------

"

if [ $1 != "" ]; then
FILE="vb.py"
if [ -f "$FILE" ]; then




while read liste ; do

python3 vb.py -l $liste 

done < $1

else
echo "[!] vb.py bulunamadı Lütfen indirin !

"

fi

else 
clear
echo "

---------------------

Twitter.com/0x00fy

---------------------

"


echo "[!] Kullanim : $0 list.txt

"

fi
