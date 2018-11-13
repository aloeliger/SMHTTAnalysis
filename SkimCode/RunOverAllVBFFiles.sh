#!/usr/bin/bash
for path in VBFConfig/*; do
    file=${path:`expr index "$path" \/`}    
    echo $file
    length=`expr index "$file" C`
    let length-=1
    outfile=${file:0:length}    
    echo $outfile
    root -b -q SkimChannel.cc\(\"$path\",\"VBFNtuples/"$outfile".root\"\)
done