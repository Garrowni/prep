#!/usr/bin/env bash

main(){
  returnString=""
  if [ $# -eq 0 ]
  then
    echo "You need to enter a number"
  else
    if (( $1 % 3 == 0 ));
    then
      returnString+="Pling"
    fi
    if (( $1 % 5 == 0 ));
    then
      returnString+="Plang"
    fi
    if (( $1 % 7 == 0 ));
    then
      returnString+="Plong"
    fi
    if (( ( $1 % 3 != 0 ) && ( $1 % 5 != 0 ) && ( $1 % 7 != 0 ) ))
    then
      returnString="$1"
    fi
    echo $returnString
  fi
}

main "$@"
