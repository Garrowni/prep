#!/usr/bin/env bash

 
   main () {
   name=$1
   if [ $# -eq 0 ]
   then
    echo "One for you, one for me."
   else
    echo "One for $name, one for me."  
   fi
   # if friend likes coo  <name> given
        #"One for <name>, one for me."
    # else no name given
       # "One for you, one for me."
  }

   # call main with all of the positional arguments
   main "$@"
