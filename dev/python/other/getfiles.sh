for line in `cat filelist`; do
    /usr/bin/wget $line
done
