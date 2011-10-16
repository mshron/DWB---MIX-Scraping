#!/bin/bash
#Pull pages

i=870
while true
  do i=$(($i+1))
  wget http://drs-sfd.gouv.sn:8083/sig-demo/index.php/detail/index/gid/$i
  sleep 2s
done
