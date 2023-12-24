for i in $(ls old/stage0); do
  if [ ! -e old/stage1/$i ] ; then
     echo Missing $i
  fi
done
