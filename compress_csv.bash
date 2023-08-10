for f in *.csv; do 
    XZ_OPT=-9 tar cJvf $f.xz $f 
done
